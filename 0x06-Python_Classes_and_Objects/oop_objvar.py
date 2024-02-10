#!/usr/bin/python3
class Robot:

    '''represents a robot with a name'''
    # a class variable, counting the number of robots
    population = 0
    def __init__(self, name):
        '''initializes the data'''
        self.name = name
        print("(intiliazing {})".format(self.name))
        #when this person is created we count a new robot made
        #adds to the population
        Robot.population += 1

    def die(self):
        '''I am dying'''
        print("{} is dieng".format(self.name))
        #when a robot dies reduce the population by one
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last robot we had".format(self.name))
        else:
            print("luckily we still have {:d} robots".format(Robot.population))
    
    def say_hi(self):
        '''greeting by the robot
          yes the can do that'''
        print("Greeting my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        '''prints the current population'''
        print("we have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
 
#now we destroy them
droid1.die()
droid2.die()

Robot.how_many()

