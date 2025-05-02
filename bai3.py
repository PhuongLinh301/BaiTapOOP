import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y

    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, P=None):
        if P is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)
        else:
            dx = self.__x - P.getX()
            dy = self.__y - P.getY()
            return math.sqrt(dx ** 2 + dy ** 2)

class ColorPoint(Point):
    def __init__(self, x=None, y=None, color=None):
        if x is None and y is None and color is None:
            super().__init__()
            self.__color = "xanh"
        elif isinstance(x, ColorPoint):
            super().__init__(x.getX(), x.getY())
            self.__color = x.__color
        else:
            super().__init__(x, y)
            self.__color = color

    def read(self):
        super().read()
        self.__color = input().strip()

    def print(self):
        super().print()
        print(f": {self.__color}")

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

class C002454:
    
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        A.print()
        print()  

    
    def testCase2():
        B = ColorPoint()
        print("Nhập tọa độ và màu (x y màu):", end=" ")
        B.read()
        B.move(10, 8)
        B.print()
        print()  

    
    def testCase3():
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C)
        D.print()
        print() 
        D.setColor("vàng")
        D.print()
        print()
        C.print()
        print()  

    
    def main():
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()

if __name__ == "__main__":
    C002454.main()
