import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner   # góc dưới bên trái (Point)
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center   # Point
        self.radius = radius   # float

def distance(p1, p2):
    """Tính khoảng cách giữa 2 điểm"""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
  
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return all(point_in_circle(circle, corner) for corner in corners)

def rect_circle_overlap(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return any(point_in_circle(circle, corner) for corner in corners)


center = Point(150, 100)
circle = Circle(center, 75)

rect = Rectangle(Point(140, 90), 20, 20)
point = Point(160, 120)

print("Point in circle:", point_in_circle(circle, point))
print("Rectangle in circle:", rect_in_circle(circle, rect))
print("Rectangle overlap circle:", rect_circle_overlap(circle, rect))
