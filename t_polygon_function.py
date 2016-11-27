"""
Question 4 - Polygon Function
I have a function that takes a point and a polygon and returns True if the point lies inside
the polygon, and False if it does not. The function implementation is shown on the next page.
In a white box testing implement your test cases in python class and consider each test in
a separate method name starts with "test_".
Justify each test case implemented ("Why is this test case important?") and document it.
"""

import unittest

__author__ = 'Stan'

"""
My assumption is that if point laying on the vertices of polygon it is not inside the polygon.
"""


# The function we are need to test:
def _is_point_in_poly(self, x, y, poly):
    """
    Check if the point is inside the polygon or not.
    :param self:
    :param x: X coordinate of the point.
    :param y: Y coordinate of the point.
    :param poly: Polygon for testing.
    :return: True if point is inside the polygon. False if not.
    """
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


# Test data. 5 polygons. Could be more depending on requirements. Usually read from file or from database
def build_polygon(name):
    """
    Choose predefined shape of the polygon from dictionary
    :param name: Name of the polygon to choose in string format
    :return: Vertices of the chosen polygon
    """
    polygons = {'square': [(0,0), (10,0), (10,10), (0,10)],
                'square_with_hole': [(0,0), (10,0), (10,10), (0, 10), (2.5,2.5), (7.5,2.5), (7.5,7.5), (2.5,7.5)],
                'weird_shaped': [(2.5,2.5), (7.5,2.5), (10, 10), (7.5,7.5), (2.5,7.5), (0,10)],
                'hexagon': [(3,0), (7,0), (10,5), (7,10), (3,10), (0,5)],
                'triangle': [(1,1), (4,1), (1,4)]
                }
    return polygons[name]


# Creating error message with debug info if assertion failed
def err_msg(expected, result, poly, x, y):
    """
    Produce error message and debug info if the test case failed.
    :param expected: Expected result of the tested function execution. Boolean type.
    :param result: Actual result of the tested function execution. Boolean type.
    :param poly: Polygon used for testing (vertices).
    :param x: X coordinate when error was raised.
    :param y: Y coordinate when error was raised.
    :return: Error message along with the debug information.
    """
    msg = 'Step Failed! Expected is: ' + str(expected) + '. Actual is: ' + str(result) + '\n'
    debug_info = 'Test polygon: ' + str(poly) + '\nx = ' + str(x) + '. y = ' + str(y)
    return msg + debug_info


# Here is a Class with unit tests inside:
class PointInPolyTest(unittest.TestCase):
    """
    Class to wrap unit tests.
    """

    def test_square_point_inside(self):
        """
        Point is inside the simple square polygon.
        :return: True if test case passed (point is inside the polygon)
        """
        poly = build_polygon('square')
        x, y = 5, 5
        expected = True
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_square_point_outside(self):
        """
        Point is outside the simple square polygon, one of the negative coordinate used.
        :return: True if test case passed (point is outside the polygon)
        """
        poly = build_polygon('square')
        x, y = 15, -5
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_square_vertices(self):
        """
        Vertices are outside the polygon.
        :return: True if test case passed (polygon vertices are not inside the polygon)
        """
        poly = build_polygon('square')
        # Testing vertices
        for vertex in poly:
            x, y = vertex
            expected = False
            result = _is_point_in_poly(self, x, y, poly)
            assert result is expected, err_msg(expected, result, poly, x, y)

    def test_square_with_hole_point_inside(self):
        """
        Point is inside the square with the hole in the middle.
        :return: True if test case passed (point is inside the polygon)
        """
        poly = build_polygon('square_with_hole')
        x, y = 1, 1
        expected = True
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_square_with_hole_point_outside(self):
        """
        Point is outside the outer boundary of the square with the hole in the middle.
        :return: True if test case passed (point is outside the polygon)
        """
        poly = build_polygon('square_with_hole')
        x, y = 11, 11
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_square_with_hole_point_in_the_hole(self):
        """
        Point is outside the polygon but inside the hole in the center of the polygon.
        :return: True if test case passed (point is inside the hole of the polygon)
        """
        poly = build_polygon('square_with_hole')
        x, y = 5, 5
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_square_with_hole_vertices(self):
        """
        Vertices should be outside the polygon.
        :return: True if test case passed (polygon vertices are not inside the polygon)
        """
        poly = build_polygon('square_with_hole')
        # Testing vertices
        for vertex in poly:
            x, y = vertex
            expected = False
            result = _is_point_in_poly(self, x, y, poly)
            assert result is expected, err_msg(expected, result, poly, x, y)

    def test_weird_shaped_point_inside(self):
        """
        Point is inside the polygon.
        :return: True if test case passed (point is inside the polygon)
        """
        poly = build_polygon('weird_shaped')
        x, y = 5, 5
        expected = True
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_weird_shaped_point_outside(self):
        """
        Point is outside the polygon, negative coordinates used.
        :return: True if test case passed (point is outside the polygon)
        """
        poly = build_polygon('weird_shaped')
        x, y = -1, -1
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_weird_shaped_vertices(self):
        """
        Vertices should be outside the polygon.
        :return: True if test case passed (polygon vertices are not inside the polygon)
        """
        poly = build_polygon('weird_shaped')
        # Testing vertices
        for vertex in poly:
            x, y = vertex
            expected = False
            result = _is_point_in_poly(self, x, y, poly)
            assert result is expected, err_msg(expected, result, poly, x, y)

    def test_weird_shaped_below_top_vertices(self):
        """
        Point is outside the polygon, but located below the top vertices.
        :return: True if test case passed (point is outside the polygon)
        """
        poly = build_polygon('weird_shaped')
        x, y = 5, 8
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_hexagon_point_inside(self):
        """
        Point is inside the hexagon.
        :return: True if test case passed (point is inside the polygon)
        """
        poly = build_polygon('hexagon')
        x, y = 5, 8
        expected = True
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_hexagon_point_outside(self):
        """
        Point is outside the hexagon, between the origin and left lower side of the hexagon.
        :return: True if test case passed (point is outside the polygon)
        """
        poly = build_polygon('hexagon')
        x, y = 1, 2
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_hexagon_vertices(self):
        """
        Vertices should be outside the polygon.
        :return: True if test case passed (polygon vertices are not inside the polygon)
        """
        poly = build_polygon('hexagon')
        # Testing vertices
        for vertex in poly:
            x, y = vertex
            expected = False
            result = _is_point_in_poly(self, x, y, poly)
            assert result is expected, err_msg(expected, result, poly, x, y)

    def test_triangle_inside(self):
        """
        Point is inside the triangle
        :return: True if test case passed (point is inside the polygon)
        """
        poly = build_polygon('triangle')
        x, y = 2, 2
        expected = True
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_triangle_outside(self):
        """
        Point is outside triangle, close to hypotenuse.
        :return: True if test case passed (point is outside the polygon)
        """
        poly = build_polygon('triangle')
        x, y = 3, 3
        expected = False
        result = _is_point_in_poly(self, x, y, poly)
        assert result == expected, err_msg(expected, result, poly, x, y)

    def test_triangle_vertices(self):
        """
        Vertices should be outside the polygon.
        :return: True if test case passed (polygon vertices are not inside the polygon)
        """
        poly = build_polygon('triangle')
        # Testing vertices
        for vertex in poly:
            x, y = vertex
            expected = False
            result = _is_point_in_poly(self, x, y, poly)
            assert result is expected, err_msg(expected, result, poly, x, y)


if __name__ == '__main__':
    unittest.main()