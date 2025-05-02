from bai11 import Point
import math

class PointTest:
    def main(self):
        diemA = Point(3,4)
        print(diemA)

        diemB = Point()
        diemB.read()
        print(diemB)

        diemC = Point(-diemB.getX(), -diemB.getY())
        print(diemC)

        print(diemB.distance())

        print(diemA.distance(diemB))

PointTest().main()
