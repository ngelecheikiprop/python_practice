#!/usr/bin/python3
squares = []
#the long method
#for x in range(10)
#    squares.append(x ** 2)

#a simpler way
square = lambda x : x ** 2
squares = list(map(square, range(10)))
print(squares)
