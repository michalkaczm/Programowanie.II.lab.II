import random
class Pudelko:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.size = self.width + self.length + self.height
        if self.size == 3:
            self.capacity = 1
        elif self.size > 3 and self.size < 6:
            self.capacity = 1
        elif self.size == 6:
            self.capacity = 2
        elif self.size > 6:
            self.capacity = 3

    def change_size(self, new_size):
        self.size = new_size

zad1 = Pudelko(1, 1, 1)

class Kosmita:
    def __init__(self, name, age, planet):
        self.name = name
        self.age = age
        self.planet = planet

zad2 = Kosmita("Alien", 30, "C/1788 W1")

class Rakieta:
    def __init__(self, mass, fuel):
        self.mass = mass
        self.fuel = fuel

    def fuel_usage(self, h):
        usage = self.mass * h  #zużycie paliwa 1l na 1m przy 1kg masy
        if usage <= self.fuel:
            print("rakieta poleci")
        else:
            print("rakieta nie poleci")
zad3 = Rakieta(100, 5000)

zad3.fuel_usage(10)

class CrazyStrings:
    def __init__(self, text):
        self.text = text

    def leet(self):
        string = self.text
        new_string1 = string.replace("a", "4")
        new_string2 = new_string1.replace("h", "5")
        new_string3 = new_string2.replace("b", "8")
        new_string4 = new_string3.replace("o", "0")
        new_string5 = new_string4.replace("l", "1")
        return new_string5

    def poke(self):
        counter = 0
        new_text = ""
        for x in self.text:
            if counter %2 == 0:
                new_text += x.upper()
                counter += 1
            else:
                new_text += x.lower()
                counter += 1

        return new_text




    def random(self):
        a = random.randint(1, 100)
        if a %2 == 0:
            return self.poke()
        else:
            return self.leet()


zad4 = CrazyStrings("I love uu")

print(zad4.random())

