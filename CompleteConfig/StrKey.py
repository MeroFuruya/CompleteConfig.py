
class StrKey:
    def __init__(self, value: str):
        self.value: str = value
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        if isinstance(other, StrKey):
            return self.value == other.value
        return str(self) == str(other)
    
    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        return f"\"{self.value}\""
    
    def __repr__(self):
        return f"StrKey({self.value})"
    
    def __add__(self, other):
        if isinstance(other, str):
            return StrKey(self.value + other)
        if isinstance(other, StrKey):
            return StrKey(self.value + other.value)
        return NotImplemented
    
    def __radd__(self, other):
        if isinstance(other, str):
            return StrKey(other + self.value)
        if isinstance(other, StrKey):
            return StrKey(other.value + self.value)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, int):
            return StrKey(self.value * other)
        return NotImplemented
    
    def __rmul__(self, other):
        if isinstance(other, int):
            return StrKey(other * self.value)
        return NotImplemented
    
    def __getitem__(self, key):
        return self.value[key]
    
    def __setitem__(self, key, value):
        self.value[key] = value
        
    def __delitem__(self, key):
        del self.value[key]
    
    def __iter__(self):
        return iter(self.value)
    
    def __contains__(self, item):
        return item in self.value
    
    def __len__(self):
        return len(self.value)
    
    def __lt__(self, other):
        if isinstance(other, str):
            return self.value < other
        if isinstance(other, StrKey):
            return self.value < other.value
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, str):
            return self.value <= other
        if isinstance(other, StrKey):
            return self.value <= other.value
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, str):
            return self.value > other
        if isinstance(other, StrKey):
            return self.value > other.value
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, str):
            return self.value >= other
        if isinstance(other, StrKey):
            return self.value >= other.value
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, str):
            return self.value != other
        if isinstance(other, StrKey):
            return self.value != other.value
        return NotImplemented
    
# Path: CompleteConfig\StrKey.py