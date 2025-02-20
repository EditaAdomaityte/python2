"""
This is Index Python File for all animals
"""
from swimming import Shark, BlueWhale, Dolphin, Fish, SeaTurtle
from slithering import Boa, Eel, Slug, Snake, Worm
from walking import Tiger, Rhino, Pig, Giraffe, Elephant

sea_turtle = SeaTurtle("Shelly", "Green Sea Turtle")
sharky = Shark("Sharky", "White Shark")
whaley = BlueWhale("Whaley", "Blue Whale")
flippy = Dolphin("Flippy", "Bottlenose Dolphin")
goldie = Fish("Goldie", "Goldfish")
boa_constrictor = Boa("Boa", "Boa Constrictor")
electric_eel = Eel("Elliot", "Electric Eel")
slimey = Slug("Slimey", "Garden Slug")
slithery = Snake("Slithery", "King Cobra")
wiggles = Worm("Wiggles", "Earthworm")
tigy = Tiger("Tigy", "Snow Tiger","Morning", "Raw Zebra")
rhorn = Rhino("Rhino", "White Rhino", "Afternoon", "Grass")
porky = Pig("Porky", "Domestic Pig", "Evening", "Corn")
giraffey = Giraffe("Giraffey", "Masai Giraffe", "Morning", "Acacia Leaves")
elephus = Elephant("Elephus", "African Elephant", "Noon", "Bark")

print(sea_turtle)
print(sharky)
print(whaley)
print(flippy)
print(goldie)
print(boa_constrictor)
print(slimey)
print(slithery)
print(wiggles)
print(tigy)
tigy.available()
tigy.feed()
print(rhorn)
rhorn.available()
rhorn.feed()
print(porky)
porky.available()
porky.feed()
print(giraffey)
giraffey.available()
giraffey.feed()
print(elephus)
elephus.available()
elephus.feed()





