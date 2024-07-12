#!/usr/bin/python3

class MyInt(int):
    """MyInt is a rebel. It inverts the == and != operators."""
    
    def __eq__(self, other):
        """Override == operator with != logic."""
        return int(self) != other
    
    def __ne__(self, other):
        """Override != operator with == logic."""
        return int(self) == other
