class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = []
        self.tent_loc.append(tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for each_loc in self.tent_loc:
            if new_tent_loc == each_loc or new_tent_loc.dist_from(each_loc) < 0.5:
                return False
        self.tent_loc.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc not in self.tent_loc:
            raise ValueError
        else:
            self.tent_loc.remove(tent_loc)

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        tent_list = []
        def insertion_sort(alist):
            for i , item_i in enumerate(alist):
                index = i
                while index > 0  and alist[index-1].getX() > item_i.getX():
                    alist[index] = alist[index-1]
                    index -= 1
                alist[index] = item_i
            return alist
        tempcopy = self.tent_loc.copy()
        for item in insertion_sort(tempcopy):
            item_str = '<' + str(item.getX()) + ',' + str(item.getY()) + '>'
            tent_list.append(item_str)

        return tent_list

c = MITCampus(Location(1,2))
print(c.add_tent(Location(-1,2))) #should return True
print(c.add_tent(Location(-1,2))) #should return True
print(c.add_tent(Location(-1,2))) #should return False
print(c.add_tent(Location(-1,2))) #should return False
print(c.get_tents()) #should return ['<0,0>', '<1,2>', '<2,3>']

