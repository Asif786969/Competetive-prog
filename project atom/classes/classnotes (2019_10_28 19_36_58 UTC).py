CLASS INTRO
#1__the class can have functions that are either private ,public or protected
#2__the private functions need to be initialised by"__" and protected membes by"_"
#3__there are 3 other functions normally used that are--
#        i--"__init__(self)".this function initialize the parameters as sooon as the object of this class is created and
#            self is the object of this class that is used inside the class
class Rocket():
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up.
my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)
 Rocket altitude: 0
Rocket altitude: 1
Rocket altitude: 2

# "." operator is used in classes to acess the attributes and variables inside the class





INHERITANCE
#1___the inheritance means normally that you can acess all the functions
# that the parent class have unless it is not private
#2__if the functions of parent and child are same then by default it will access
#the function of the child class but if specifically you need to accces the function
#of the parent class then you need the "super()." function
#3__also in place of super you can use the name of "parent class." function
but it is preferable to use super function
