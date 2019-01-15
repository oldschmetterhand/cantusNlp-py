

class Animal:
    """
    Das ist einDocstring in Python der über pydoc ausgelesen werden kann.
    Hier kommt die Bechreibung der Klasse rein.

    @name default value is zero.
    @legs sooooo many legs...
    @age default is 0.
    """

    planet  = "earth"
    age = 0
    _isLiving = True

    def __init__(self, name, legs, age):
        self.name = name
        self.legs = legs
        self.age = age

    def introduceMyself(self):
        print("Hi my name is: " + self.name + " and I have " + self.legs + " legs. I'm coming from the planet " + self.planet)

    def countMyAge(self):
        count = 0
        while(count<=self.age):
            print("I think I am {}".format(count))
            count += 1


class Dog(Animal):
    race = ""

    def __init__(self, name, legs, age, race):
        super(Dog, self).__init__(name, legs, age)
        self.race = race

    def tellYourRace(self):
        return self.race



