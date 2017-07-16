class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __int__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assume e is an integer and insects e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assume e is an integer
            Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assuems e is an integer and removes e form self
            Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        temp = intSet()
        for item in self.vals:
            if item in other.vals:
                temp.insert(item)
        return temp

    def __len__(self):
        return len(self.vals)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
