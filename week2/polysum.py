import math

def polysum(n, s):
    """
    This function should sum the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.
    :param n: type int, A regular polygon has 'n' number of sides. Each side has length 's'.
    :param s: type float, Each side has length 's'.
    :return: sum of the area and square of the perimeter of the regular polygon.
    """
    def areaPolygon(n, s):
        return 0.25*n*s*s/math.tan(math.pi/n)

    def perimeterPolygon(n, s):
        return n*s

    return float('%.4f' % (areaPolygon(n, s) + perimeterPolygon(n, s)**2,))

