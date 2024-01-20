#!/usr/bin/python3
x = int(input("please enter an interger: "))
if x < 0:
    x = 0
    print("negative changed zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("single")
else:
    print("more")
