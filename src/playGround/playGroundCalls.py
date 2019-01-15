
from src.playGround.PlayGround import *


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