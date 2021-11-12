class Cat:
    color = "default cat color"

    def getColour(self):
        return self.color

    def sleep(self, amount):
        print(f"sleeping for the next {amount} hours")

british = Cat()
british.color = "tabby"
# print(british.getColour())

siberian = Cat()
siberian.color = "red"
# print(siberian.getColour())

# print(Cat.color)

class Puppy:

    def __init__(self, name, breed, months):
        self.name = name
        self.breed = breed
        self.months = months

p = Puppy("Zephyrka", "WSS", 12)
z = Puppy("Greta", "Labrador", 6)
print(p.name, p.breed, p.months)
print(z.name, z.breed, z.months)
