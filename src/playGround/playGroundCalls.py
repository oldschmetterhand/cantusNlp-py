
from src.playGround.PlayGround import *

import xml.etree.ElementTree as Etree;

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


#example for if / else statements

if(soki.age==4):
    print("super!")

if(soki.age==5):
    print("unnice!")
else:
    print("blaa")

