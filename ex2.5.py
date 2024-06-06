class Animal:
    # Class attribute shared by all instances
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initialize the animal with a name and an optional hunger level.

        :param name: The name of the animal.
        :param hunger: The hunger level of the animal, default is 0.
        """
        self.name_ = name
        self.hunger_ = hunger

    def get_name(self):
        """
        Get the name of the animal.

        :return: The name of the animal.
        """
        return self.name_

    def is_hungry(self):
        """
        Check if the animal is hungry.

        :return: True if the animal's hunger level is greater than 0, False otherwise.
        """
        return self.hunger_ > 0

    def feed(self):
        """
        Feed the animal, decreasing its hunger level by 1.
        """
        if self.is_hungry():
            self.hunger_ -= 1

    def talk(self):
        """
        Placeholder method for animal sound. To be overridden by subclasses.
        """
        pass


class Dog(Animal):
    def talk(self):
        """
        Make the dog bark.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Unique method for Dog to fetch a stick.
        """
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        """
        Make the cat meow.
        """
        print("meow")

    def chase_laser(self):
        """
        Unique method for Cat to chase a laser pointer.
        """
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize the skunk with a name, an optional hunger level, and a stink count.

        :param name: The name of the skunk.
        :param hunger: The hunger level of the skunk, default is 0.
        :param stink_count: The stink count of the skunk, default is 6.
        """
        super().__init__(name, hunger)
        self.stink_count_ = stink_count

    def talk(self):
        """
        Make the skunk hiss.
        """
        print("tsssss")

    def stink(self):
        """
        Unique method for Skunk to stink.
        """
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        """
        Make the unicorn speak.
        """
        print("Good day, darling")

    def sing(self):
        """
        Unique method for Unicorn to sing.
        """
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        """
        Initialize the dragon with a name, an optional hunger level, and a color.

        :param name: The name of the dragon.
        :param hunger: The hunger level of the dragon, default is 0.
        :param color: The color of the dragon, default is Green.
        """
        super().__init__(name, hunger)
        self.color_ = color

    def talk(self):
        """
        Make the dragon roar.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Unique method for Dragon to breathe fire.
        """
        print("$@#$#@$")


def main():
    """
    The main function that creates instances of different animals,
    feeds them if they are hungry, makes them talk, and performs
    their unique actions.
    """
    zoo_lst = [
        Dog(name="Brownie", hunger=10),
        Cat(name="Zelda", hunger=3),
        Skunk(name="Stinky", hunger=0),
        Unicorn(name="Keith", hunger=7),
        Dragon(name="Lizzy", hunger=1450)
    ]

    new_animals = [
        Dog(name="Doggo", hunger=80),
        Cat(name="Kitty", hunger=80),
        Skunk(name="Stinky Jr.", hunger=80),
        Unicorn(name="Clair", hunger=80),
        Dragon(name="McFly", hunger=80)
    ]

    zoo_lst.extend(new_animals)

    for animal in zoo_lst:
        while animal.is_hungry():
            print(f"{type(animal).__name__} {animal.get_name()}")
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(f"Zoo name: {Animal.zoo_name}")


if __name__ == "__main__":
    main()
