"""
Создайте игру "Магазин животных". Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена),
   а также методом sound(), который возвращает звук, издаваемый животным. От него унаследуйте классы Dog, Cat и Bird,
   каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.
   Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина),
   а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного.
   Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.
"""
from __future__ import annotations

from typing import TYPE_CHECKING


class Animal:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def sound(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name}'


class Dog(Animal):
    def sound(self):
        print(f'{self.name}: гаф гаф')


class Cat(Animal):
    def sound(self):
        print(f'{self.name}: мяв мяв')


class Bird(Animal):
    def sound(self):
        print(f'{self.name}: чур чур')


class Shop:
    def __init__(self, animals: list[Animal], budget: float):
        self.animals = animals
        self.budget = budget

    def buy_animal(self, animal: Animal):
        if animal.price <= self.budget:
            self.animals.append(animal)
            self.budget -= animal.price
        else:
            print('Недостаточный бюджет')

    def sell_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.budget += self.price
        else:
            print(f'Животного {animal.name} нет в магазине')

    def __str__(self):
        return f'{self.animals} | {self.budget}'


a = Dog('alabay', 100)
b = Cat('garaja', 50)
c = Bird('serchejik', 10)

sklep = Shop(animals=[a, b], budget=200)

print(sklep)

Shop.sell_animal(a)


