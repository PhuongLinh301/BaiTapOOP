from bai11 import Point
from bai21 import LineSegment
import math

class LineSegmentTest:
    def testCase1(self):
        A = Point(2,5)
        B = Point(20,35)
        AB = LineSegment(A,B)
        print(AB)
        AB.move(35,51)
        print(AB)

    def testCase2(self):
        CD = LineSegment()
        print("|CD| = {:.2f}".format(CD.length()))

    def testCase3(self):
        danhsach = []
        n = int(input("Nhập n: "))
        for i in range (n):
            l1 = LineSegment()
            l1.read()
            danhsach.append(l1)

        for item in danhsach:
            print(item)
            print(item.length())

        danhsach.sort(key = lambda dist: dist.length())
        for item in danhsach:
            print(item)
            print(item.length())

        def main(self):
            while True:
                s = input("Nhập kịch bản muốn chạy 1/2/3/exit: ")
                if s == '1':
                    LineSegmentTest().testCase1()
                if s == '2':
                    LineSegmentTest().testCase2()
                if s == '3':
                    LineSegmentTest().testCase3()
                if s == 'exit':
                    break
        
        LineSegmentTest().main()

