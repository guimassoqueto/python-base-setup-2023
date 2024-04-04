from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self) -> None:
        pass


class Dog(Animal):
    def do_say(self) -> None:
        print("Bark")


class Cat(Animal):
    def do_say(self) -> None:
        print("Meow")


class ForestFactory(object):
    def make_sound(self, object_type: str) -> None:
        try:
            return eval(object_type.title())().do_say()
        except:
            print("This animal is not available")


def run():
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)