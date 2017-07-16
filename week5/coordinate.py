class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accssing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Coordinate(%s,%s)" % (self.x, self.y)

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

test = Coordinate(3, 4)
print(test.__repr__())