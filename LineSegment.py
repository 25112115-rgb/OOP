class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.__d1 = Point(args[0].getD1().x, args[0].getD1().y)
            self.__d2 = Point(args[0].getD2().x, args[0].getD2().y)
        else:
            raise ValueError("Tham số không hợp lệ cho LineSegment")

    def getD1(self):
        return self.__d1

    def setD1(self, point):
        self.__d1 = point

    def getD2(self):
        return self.__d2

    def setD2(self, point):
        self.__d2 = point

    def __str__(self):
        return f"Đoạn thẳng từ {self.__d1} đến {self.__d2}"


ls1 = LineSegment()
print(ls1)

p1 = Point(3, 4)
p2 = Point(7, 9)
ls2 = LineSegment(p1, p2)
print(ls2)

ls3 = LineSegment(0, 0, 5, 5)
print(ls3)

ls4 = LineSegment(ls3)
print(ls4)

