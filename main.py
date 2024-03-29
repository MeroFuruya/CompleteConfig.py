from CompleteConfig import *

# define your own config
config_dict = {
    "std_key": "std_value",
    StrKey("str_key"): "str_value",
    Key("comment_key", "comment_key_comment"): "comment_value",
    Key(StrKey("comment_str_key"), "comment_str_key_comment"): "comment_str_value",
    Key("nocomment_key"): "nocomment_value",
    "dict_key": {
        "dict_std_key": "dict_std_value",
        StrKey("dict_str_key"): "dict_str_value",
        Key("dict_comment_key", "dict_comment_key_comment"): "dict_comment_value",
        Key(StrKey("dict_comment_str_key"), "dict_comment_str_key_comment"): "dict_comment_str_value",
        Key("dict_nocomment_key"): "dict_nocomment_value",
        "nested_dict_key": {
            "nested_dict_std_key": "nested_dict_std_value",
            StrKey("nested_dict_str_key"): "nested_dict_str_value",
            Key("nested_dict_comment_key", "nested_dict_comment_key_comment"): "nested_dict_comment_value",
            Key(StrKey("nested_dict_comment_str_key"), "nested_dict_comment_str_key_comment"): "nested_dict_comment_str_value",
            Key("nested_dict_nocomment_key"): "nested_dict_nocomment_value",
        },
    },
    "list_key": [
        "list_std_value1",
        "list_std_value2",
        1,
        1.1,
        False,
        [
            "list_std_value3",
            "list_std_value4",
            2,
            2.2,
            True,
        ]
    ],
    "boolean": True,
    "integer": 123,
    "float": 123.456,
    StrKey("dict_str_key"): {
        "dict_std_key": "dict_std_value",
    },
    Key("dict_comment_key", "dict_comment_key_comment"): {
        "dict_std_key": "dict_std_value",
    },
    Key(StrKey("dict_comment_str_key"), "dict_comment_str_key_comment"): {
        "dict_std_key": "dict_std_value",
    },
}
# and store it to a file
with open("test.conf", "w") as f:
    dump(f, config_dict)

# open an existing config
with open("test.conf", "r") as f:
    config_dict = load(f)

# change something
config_dict["std_key"] = "new_std_value"
config_dict["dict_str_key"]["dict_std_key"] = "new_dict_std_value"

# and save your changes to the file
with open("test.conf", "w") as f:
    dump(f, config_dict)

# Path: main.py