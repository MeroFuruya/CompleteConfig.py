from .StrKey import StrKey

class Key:
    def __init__(self, value: str | StrKey, comment: str | None = None):
        self.value: str | StrKey = value
        self.comment: str | None = comment
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        if isinstance(other, Key):
            return self.value == other.value
        return str(self) == str(other)
    
    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        if self.comment is None:
            return repr(self.value)
        return f"Key({repr(self.value)}, comment='{self.comment}')"
    
    def __repr__(self):
        if self.comment is None:
            return repr(self.value)
        return f"Key({repr(self.value)}, comment='{self.comment}')"
    
# Path: CompleteConfig\Key.py