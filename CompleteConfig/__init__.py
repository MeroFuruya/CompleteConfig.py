from .StrKey import StrKey
from .Key import Key

def _indent(indent: int) -> str:
    return " " * (indent * 4)

def dumps(obj: dict) -> str:
    """Converts a dictionary to a CompleteConfig-string."""
    
    def conv_value(value):
        if isinstance(value, list):
            return "[" + ", ".join([conv_value(v) for v in value]) + "]"
        elif isinstance(value, str):
            return f"\"{value}\""
        elif isinstance(value, bool):
            return str(value).lower()
        else:
            return str(value)
    
    def conf_kv(key, value, indent: int):
        res = ""
        if indent != 0:
            res += "\n"
        res += _indent(indent)
        if isinstance(key, Key):
            if key.comment is not None:
                res += f"# {key.comment}\n" + _indent(indent)
            key = key.value
        if isinstance(value, dict):
            res += f"{key} {conv_dict(value, indent+1)}"
        else:
            res += f"{key}={conv_value(value)}"
        return res
    
    def conv_dict(data: dict, indent: int = 0) -> str:
        if indent == 0:
            return "\n".join([conf_kv(k, v, indent) for k, v in data.items()])
        else:
            return "{" + "".join([conf_kv(k, v, indent) for k, v in data.items()]) + "\n" + _indent(indent-1) +"}"
    
    return conv_dict(obj)

def dump(fp, obj: dict) -> None:
    """Converts a dictionary to a CompleteConfig-string and writes it to a file-like object."""
    fp.write(dumps(obj))

def loads(data: str) -> dict:
    lines = [line.strip() for line in data.split("\n") if line.strip() != ""] # Remove leading and trailing whitespace, split by newlines, Remove empty lines
    
    def conv_value(value: str) -> str | bool | int | float:
        if value.startswith("\"") and value.endswith("\""):
            return value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            res = []
            lines = [line.strip() for line in value[1:-1].split(",") if line.strip() != ""]
            i = 0
            while i < len(lines):
                line = lines[i]
                i += 1
                if line.startswith("["):
                    depth = -1
                    list_lines = []
                    for list_line in lines[i-1:]:
                        if list_line.startswith("["):
                            depth += 1
                        list_lines.append(list_line)
                        if list_line.endswith("]"):
                            if depth == 0:
                                break
                            depth -= 1
                    i += len(list_lines)
                    res.append(conv_value(", ".join(list_lines)))
                else:
                    res.append(conv_value(line))
            return res
        elif value.lower() in ["true", "false"]:
            return value.lower() == "true"
        elif "." in value and value.replace(".", "").isdigit():
            return float(value)
        elif value.isdigit():
            return int(value)
        else:
            return value
    
    def conv_key(key: str) -> str | StrKey:
        if key.startswith("\"") and key.endswith("\""):
            return StrKey(key[1:-1])
        else:
            return key
    
    def parse_lines(lines: list[str]) -> dict:
        res = {}
        comment = None
        is_last_comment = False
        is_comment = False
        i = 0
        # iterate over lines
        while i < len(lines):
            i += 1
            line = lines[i-1]
            # check if line is comment
            if is_last_comment:
                is_last_comment = False
            if is_comment:
                is_comment = False
                is_last_comment = True
            if line.startswith("#"):
                is_comment = True
                comment = line[1:].strip()
                continue
            # check if line is beginning of dict
            if "{" in line:
                dict_lines = []
                depth = 0
                # get all lines of dict
                for dict_line in lines[i:]:
                    if "{" in dict_line:
                        depth += 1
                    dict_lines.append(dict_line)
                    if "}" in dict_line:
                        if depth == 0:
                            break
                        depth -= 1
                # skip lines of dict
                i += len(dict_lines)
                # parse dict and add to result
                if is_last_comment:
                    res[Key(conv_key(line[:line.index("{")].strip()), comment)] = parse_lines(dict_lines)
                else:
                    res[conv_key(line[:line.index("{")].strip())] = parse_lines(dict_lines)
                continue
            # check if line is end of dict
            if "}" in line:
                return res
            # check if line is key-value-pair
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()
                if is_last_comment:
                    res[Key(conv_key(key), comment)] = conv_value(value)
                else:
                    res[conv_key(key)] = conv_value(value)
                continue
        return res
    return parse_lines(lines)

def load(fp) -> dict:
    """Converts a CompleteConfig-string from a file-like object to a dictionary."""
    return loads(fp.read())

# Path: CompleteConfig\__init__.py