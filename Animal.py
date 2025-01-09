class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print('гав-гав')


class BigDog(Dog):

    def speak(self):
        print('ГАВ')


class SmallDog(Dog):

    def speak(self):
        print('гав-гав-гав-гав-гав-гав')


class ToyDog(Dog):

    def speak(self):
        pass


class RobotDog(ToyDog):

    def speak(self):
        print('Гав(искусственным голосом)')


class BigAngryDog(BigDog):

    def speak(self):
        print('(Делает сердитый взгляд)')
        super().speak()
        print('(Хмуриться)')


class SmallAngryDog(SmallDog):

    def speak(self):
        print('(Пискляво)')
        super().speak()


class Cat(Animal):

    def _meow(self):
        print('Мяу')

    def speak(self):
        self._meow()


class CuteCat(Cat):

    def _meow(self):
        print('Мурр')

    def speak(self):
        self._meow()


def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()


list_of_animals = [Cat(), Dog(), CuteCat(), BigAngryDog()]
for animal in list_of_animals:
    animal.speak()

animal = Animal()
animal.speak()

bobik = Dog()
bobik.speak()

pupsik = BigDog()
pupsik.speak()

tobik = SmallDog()
tobik.speak()

toy = ToyDog()
toy.speak()

chipa = RobotDog
chipa.speak()

sharik = BigAngryDog()
sharik.speak()

vaska = Cat()
vaska.speak()

myaut = CuteCat()
myaut.speak()

druzhok = BigDog()
say_n_times(druzhok, 5)

barsik = Cat()
say_n_times(barsik, 5)
