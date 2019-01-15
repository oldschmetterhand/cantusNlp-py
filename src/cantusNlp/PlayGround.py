



class Animal:
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


wale = Animal("Rüdiger", "4", 5)
wale.introduceMyself()
wale.age = 1
wale.countMyAge()

soki = Dog("Sokrates", "4", 13, "Terrier")
soki.introduceMyself()
sokisRace = soki.tellYourRace()
print("My Race? I'm a {}!".format(sokisRace))
soki.age = 4
soki.countMyAge()
