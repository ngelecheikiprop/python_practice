#!/usr/bin/python3
class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("lets get you the height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("please enter a number")

    @property
    def width(self):
        print("lets get you the width")
        return self.__height

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("please enter a number")

    def getArea(self):
        return int(self.__height) * int(self.__width)


def main():
    aSquare = Square()
    height = input("Enter the height of your square")
    width = input("Enter the width of your square")
    aSquare.height = height
    aSquare.width = width
    print("Height: {}".format(aSquare.height))
    print("Weight: {}".format(aSquare.width))
    print("and area: {}".format(aSquare.getArea()))


main()
