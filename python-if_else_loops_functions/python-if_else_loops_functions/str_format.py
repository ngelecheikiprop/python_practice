#!/usr/bin/python3
print("sammy has {} ballons".format(5))
#assign a variable to be equal to the value of a string that has formatter placeholders:
open_string = "sammy loves {}"
print(open_string.format("opensource"))
#using with multiple place holders
new_open_string =  "sammy loves {} {}"
print(new_open_string.format("open source", "software"))
#reordering with positional and keyword arguments
print("sammy the {1} has a pet {0}".format("shark", "pilot fish"))
##Specifying Type
print("sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
#limiting the places
print("sammy ate {0:.3f}".format(75.1234))
#specifying field sizes
print("Sammy has {0:4} red {1:16}".format(5,"ballons"))
#left align
print("left align: {:<5}".format(5))
#center word
print("center word : {:^*20s}".format("david"))
#using formatters to organize data
for i in range(3,13):
    print("{:6d}, {:6d}, {:6d}".format(i, i*i, i * i * i))
