from collections import namedtuple
from dataclasses import dataclass, field
from itertools import product

from pydantic import BaseModel, Field
"""
#1
class Employee:
    first_name: str
    last_name: str
    salary: float

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"My name is {self.first_name} {self.last_name}."


osoba1 = Employee(first_name="Przemyslaw", last_name="Hubacz", salary=7500)

osoba1_info = osoba1.get_full_name()
print(osoba1_info)

class Manager(Employee):
    departament: str

    def __init__(self, first_name: str, last_name: str, salary: float, departament: str) -> None:
        super().__init__(first_name, last_name, salary)
        self.departament = "defender"

    def get_department_info(self) -> str:
        return f"{self.first_name} {self.last_name} manages the department {self.departament}. He earns {self.salary}."

Manager =  Manager(first_name="Arek", last_name="Kowal", salary="15000", departament="defender")
Manager_info= Manager.get_department_info()
print(Manager_info)

#Zad2

Transaction = namedtuple("Transaction", ["tansaction_id", "amount", "currency"])

class BankAccount:
    balance: float

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def apply_transaction(self, transaction: Transaction) -> str:
        self.balance -= transaction.amount
        return f"{self.balance}"



cash = BankAccount(2000000)

transaction = Transaction(1, 2000, BankAccount)

print(cash.apply_transaction(transaction))

#Zad3

@dataclass()
class Book:
    title: str
    author: str
    year: float
    price: float

    def apply_discount(self, discount: float):
        discount = self.price * discount/100
        return self.price - discount

Book = Book("Lalka", "Bolesław Prus", 1850, 200)

discount = int(input("Jaki procent zniżki posiadasz: "))

print(Book.apply_discount(discount))


#Zad4

@dataclass(frozen=True)
class Product:
    name: str
    price: float = Field(ge=0.01)
    category: str = field(default="General")

    def get_info(self) -> str:
        return f"Your product is {self.name} which cost {self.price}."

Product0 = Product(name="chipsy", price="100.0")

Product0_info = Product0.get_info()

print(Product0_info)

#zad5

class Car:
    brand: str
    model: str
    year: float

    def __init__(self, brand: str, model: str, year: float) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def is_classic(self) -> bool:
        if(self.year>25):
            return False
        else:
            return True

car1 = Car("BMW", "M4", 2)

print(car1.is_classic())
Stworzyć klasy ElectricVehicle oraz GasolineVehicle, które mają metodę fuel_type(), 
zwracającą odpowiednio "electric" i "gasoline". Następnie utworzyć klasę HybridCar, 
która dziedziczy po obu i nadpisuje metodę fuel_type(), aby zwracała "hybrid".



#Zad6

class ElectricVehicle:
    def fuel_type(self) -> str:
        return "electric"

class GasolineVehicle:
    def fuel_type(self) -> str:
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self) -> str:
        return "hybrid"

electric_car = ElectricVehicle()
gasoline_car = GasolineVehicle()
hybrid_car = HybridCar()

print(electric_car.fuel_type())
print(gasoline_car.fuel_type())
print(hybrid_car.fuel_type())

Utworzyć klasę Person z metodą introduce(), zwracającą "I am a person". 
Następnie stworzyć klasy Worker i Student, które dziedziczą po Person i 
zmieniają tę metodę na "I am a worker" oraz "I am a student". Następnie 
utworzyć klasę WorkingStudent, która dziedziczy zarówno po Worker, jak i 
Student, i sprawdź, jak Python rozwiąże konflikt metod.


#Zad7

class Person:
    def introduce(self) -> str:
        return f"I am a person."

class Worker(Person):
    def introduce(self) -> str:
        return f"I am a worker."

class Student(Person):
    def introduce(self) -> str:
        return f"I am a student."

class WorkingStudent(Worker, Student):
    pass

person = Person()
worker = Worker()
student = Student()
working_student = WorkingStudent()

print(person.introduce())
print(worker.introduce())
print(student.introduce())
print(working_student.introduce())



#Zad8

class Animal:
    def make_sound(self) -> str:
        return "Some sound."

class Pet:
    def is_domestic(self) -> bool:
        return True


class Dog(Animal, Pet):
    def make_sound(self) -> str:
        return "Bark"


dog = Dog()
print(dog.make_sound())
print(dog.is_domestic())



#Zad9

class FlyingVehicle:
    def move(self) -> str:
        return "I fly."

class WaterVehicle:
    def move(self) -> str:
        return "I sail."

class AmphibiousVehicle(FlyingVehicle, WaterVehicle):
    def move(self, mode: str) -> str:
        if mode == "air":
            return FlyingVehicle.move(self)
        elif mode == "water":
            return WaterVehicle.move(self)
        else:
            return "Invalid mode"


amphibious = AmphibiousVehicle()
print(amphibious.move("air"))
print(amphibious.move("water"))
print(amphibious.move("land"))

"""

#Zad10

class Robot:
    def operate(self) -> str:
        return "Performing task"

class AI:
    def think(self) -> str:
        return "Processing data"

class Android(Robot, AI):
    def self_learn(self) -> str:
        return "Learning new skills"


android = Android()
print(android.operate())
print(android.think())
print(android.self_learn())



