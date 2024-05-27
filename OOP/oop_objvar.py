class Robot:
    """ robot class with robot name"""
    #class var
    population = 0
    def __init__(self, name):
        self.name = name
        print("robot {} is intialized".format(self.name))
        Robot.population += 1
    
    def die(self):
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} is last one".format(self.name))
        else:
            print("there are {:d} still working".format(Robot.population))
    
    def say_hi(self):
        print("Greatings, my master called {}".format(self.name))
    
    @classmethod
    def how_many(c):
        print("we have {:d} robots".format(c.population))

droid1 = Robot("RM")
droid1.say_hi()
Robot.how_many()

