#!/usr/bin/python3
class SchoolMember:
    '''Represents any school member'''
    def __init_(self, name, age):
        self.name = name
        self.age = age
        print('(Intialized School Member: {})'.format(self.name))
    def tell(self):
        '''tell my details'''
        print('Name :"{}" Age""{}"'.format(self.name, self.age), end="")

class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('initiliazed Teacher : {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''represent a school Member'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks  = marks
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Sridivya', 40, 30000)
s = Student("kiprop", 24, 411)

#prints a blank line
print()
members = [t,s]
for member in members:
    member.tell
