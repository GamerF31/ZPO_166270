from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Any
"""
Budowniczy

Przygotować klasę Pizza, która będzie mogła zawierać różne składniki 
(ser, salami, pieczarki, cebula itd.). Zastosować wzorzec budowniczego, aby 
umożliwić stopniowe dodawanie składników do pizzy.

Rozszerzyć istniejącą implementację budowniczego tak, aby umożliwić budowanie 
różnych wariantów obiektów (np. dla pizzy vege, mięsnej, serowej, itd.).

Przygotować klasę Computer, która posiada wiele parametrów przekazywanych w 
inicjalizatorze. Przerobić nastęopnie kod tak, aby zamiast dużego konstruktora użyć wzorca budowniczego
"""
"""
from typing import List


class Pizza:
    def __init__(self):
        self.ingredients: List[str] = []

    def add_ingredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f"Pizza with: {', '.join(self.ingredients)}"



class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def add_base_ingredients(self):
        pass

    def add_cheese(self):
        self.pizza.add_ingredient("Cheese")
        return self

    def add_salami(self):
        self.pizza.add_ingredient("Salami")
        return self

    def add_salami(self):
        self.pizza.add_ingredient("Chicken")
        return self

    def add_mushrooms(self):
        self.pizza.add_ingredient("Mushrooms")
        return self

    def add_onion(self):
        self.pizza.add_ingredient("Onion")
        return self

    def build(self):
        return self.pizza


class PizzaVegeBuilder(PizzaBuilder):
    def add_base_ingredients(self):
        self.pizza.add_ingredient("Cheese")
        self.pizza.add_ingredient("Mushrooms")
        self.pizza.add_ingredient("Onion")
        return self

class PizzaMealBuilder(PizzaBuilder):
    def add_base_ingredients(self):
        self.pizza.add_ingredient("Cheese")
        self.pizza.add_ingredient("Chicken")
        self.pizza.add_ingredient("Salami")
        return self

class PizzaCheeseBuilder(PizzaBuilder):
    def add_base_ingredients(self):
        self.pizza.add_ingredient("Cheese")
        return self


class Computer:
    def __init__(self, Procesor, GraphicCard, Windows, RAM):
        self.procesor = Procesor
        self.graphicCard = GraphicCard
        self.windows = Windows
        self.ram = RAM

    def __str__(self):
        return f"Computer: {self.procesor} and {self.graphicCard} and {self.windows} and {self.ram}"


vege_pizza = PizzaVegeBuilder().add_base_ingredients().build()
builder = PizzaBuilder()
pizza = builder.add_cheese().add_salami().add_mushrooms().build()
computer1 = Computer("Intel I7", "NVIDIA RTX 3070", "Windows 11", 32)
print(pizza)
print(vege_pizza)
print(computer1)


#Zad2

class Document(ABC):
    @abstractmethod
    def type_document(self) -> str:
        pass

class PDFDocument(Document):
    def type_document(self) -> str:
        return "You created PDF"

class WordDocument(Document):
    def type_document(self) -> str:
        return "You created Word"

class DocumentFactory:
    @staticmethod
    def type_document(document_type: str) -> Document:
        if document_type == "docx":
            return WordDocument()
        elif document_type == "pdf":
            return PDFDocument()
        else:
            return "Wront type_document"

doc1 = WordDocument()
print(doc1.type_document())

#b

class Animal(ABC):
    @abstractmethod
    def do_animal(self) -> str:
        pass

class Dog(Animal):
    def do_animal(self) -> str:
        return "You created Dog"

class Car(Animal):
    def do_animal(self) -> str:
        return "You created Cat"
class AnimalFactory:
    @staticmethod
    def do_animal(move: str) -> Animal:
        if move == "Hau Hau":
            return "You created Dog"
        elif move == "Miau Miau":
            return "You created Cat"
        else:
            return "We do not know what you created"

animal1 = AnimalFactory.do_animal("Hau")
print(animal1)

#Zadb

class Car(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass

class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Car:
        pass

    @abstractmethod
    def create_suv(self) -> Car:
        pass





@dataclass
class Wheel:
    diameter: int
    material: str = field(default="aluminium")

@dataclass
class Body:
    color: str
    thickness: float = field(default=0.6)

@dataclass
class Door:
    interior_material: str
    control: str = field(default="manual")

@dataclass
class Seat:
    material: str
    control: str = field(default="manual")



#Zad3

class Car(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass
class HatchBackCar(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass

class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Car:
        pass

    @abstractmethod
    def create_suv(self) -> Car:
        pass

class TeslaSedan(Car):
    def specifications(self) -> str:
        return "Tesla Model S - Elektryczny Sedan"

class TeslaSUV(Car):
    def specifications(self) -> str:
        return "Tesla Model X - Elektryczny SUV"

class BMWSedan(Car):
    def specifications(self) -> str:
        return "BMW Seria 5 - Benzynowy/Dieslowy Sedan"

class BMWSUV(Car):
    def specifications(self) -> str:
        return "BMW X5 - Benzynowy/Dieslowy SUV"

class TeslaFactory(CarFactory):
    def create_sedan(self) -> Car:
        return TeslaSedan()

    def create_suv(self) -> Car:
        return TeslaSUV()

class BMWFactory(CarFactory):
    def create_sedan(self) -> Car:
        return BMWSedan()

    def create_suv(self) -> Car:
        return BMWSUV()

tesla_factory = TeslaFactory()
bmw_factory = BMWFactory()

tesla_sedan = tesla_factory.create_sedan()
tesla_suv = tesla_factory.create_suv()

bmw_sedan = bmw_factory.create_sedan()
bmw_suv = bmw_factory.create_suv()

print(tesla_sedan.specifications())
print(tesla_suv.specifications())
print(bmw_sedan.specifications())
print(bmw_suv.specifications())




@dataclass
class Wheel:
    diameter: int
    material: str = field(default="aluminium")

@dataclass
class Body:
    color: str
    thickness: float = field(default=0.6)

@dataclass
class Door:
    interior_material: str
    control: str = field(default="manual")

@dataclass
class Seat:
    material: str
    control: str = field(default="manual")


@dataclass
class Car:
    wheels: tuple
    body: Body
    doors: tuple
    seats: tuple

@dataclass
class Sedan(Car):
    pass

@dataclass
class SUV(Car):
    pass

@dataclass
class Hatchback(Car):
    pass


class CarFactory(ABC):
    @abstractmethod
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        pass

    @abstractmethod
    def produce_body(self, color: str) -> Body:
        pass

    @abstractmethod
    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        pass

    @abstractmethod
    def produce_seats(self, material: str, amount: int) -> tuple:
        pass


class TeslaFactory(CarFactory):
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        return tuple([Wheel(diameter=diameter, material="carbon") for _ in range(amount)])

    def produce_body(self, color: str) -> Body:
        return Body(color=color, thickness=0.8)

    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        return tuple([Door(interior_material=interior_material, control="electric") for _ in range(amount)])

    def produce_seats(self, material: str, amount: int) -> tuple:
        return tuple([Seat(material=material, control="electric") for _ in range(amount)])


class BMWFactory(CarFactory):
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        return tuple([Wheel(diameter=diameter, material="steel") for _ in range(amount)])

    def produce_body(self, color: str) -> Body:
        return Body(color=color, thickness=1.0)

    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        return tuple([Door(interior_material=interior_material, control="manual") for _ in range(amount)])

    def produce_seats(self, material: str, amount: int) -> tuple:
        return tuple([Seat(material=material, control="manual") for _ in range(amount)])


class AbstractCarFactory:
    _factories = {}

    @staticmethod
    def register_factory(brand: str, factory_class):
        AbstractCarFactory._factories[brand] = factory_class

    @staticmethod
    def get_factory(brand: str):
        factory = AbstractCarFactory._factories.get(brand)
        if not factory:
            raise ValueError(f"Unknown car brand: {brand}")
        return factory()


AbstractCarFactory.register_factory("Tesla", TeslaFactory)
AbstractCarFactory.register_factory("BMW", BMWFactory)


class CarManufacturer:
    client_options: dict

    def __init__(self, client_options: dict) -> None:
        self.client_options = client_options

    def produce_car(self) -> Car:
        factory = AbstractCarFactory.get_factory(self.client_options["brand"])
        wheels, body, doors, seats = self._request_parts(factory)

        if self.client_options["type"] == "Sedan":
            return Sedan(wheels=wheels, body=body, doors=doors, seats=seats)
        elif self.client_options["type"] == "SUV":
            return SUV(wheels=wheels, body=body, doors=doors, seats=seats)
        elif self.client_options["type"] == "Hatchback":
            return Hatchback(wheels=wheels, body=body, doors=doors, seats=seats)
        else:
            raise ValueError("Unknown car type")

    def _request_parts(self, factory) -> tuple:
        wheels = factory.produce_wheels(self.client_options["diameter"], 4)
        body = factory.produce_body(self.client_options["color"])
        doors = factory.produce_doors(self.client_options["doors"], 5)
        seats = factory.produce_seats(self.client_options["seats"], 5)

        return wheels, body, doors, seats


if __name__ == "__main__":
    hatchback_specification = {
        "brand": "Tesla",
        "type": "Hatchback",
        "diameter": 17,
        "color": "blue",
        "doors": "plastic",
        "seats": "leather"
    }

    manufacturer = CarManufacturer(hatchback_specification)
    tesla_hatchback = manufacturer.produce_car()

    print(tesla_hatchback)

    suv_specification = {
        "brand": "BMW",
        "type": "SUV",
        "diameter": 20,
        "color": "black",
        "doors": "leather",
        "seats": "fabric"
    }

    manufacturer = CarManufacturer(suv_specification)
    bmw_suv = manufacturer.produce_car()

    print(bmw_suv)


from copy import deepcopy
from typing import Any

#Zad4
from copy import deepcopy
from typing import Any

class CharacterPrototype:
    def __init__(
            self,
            name: str,
            height: int,
            level: int,
            power: int,
            weight: int,
            owner: str,
            **kwargs: dict,
    ) -> None:
        self.name = name
        self.height = height
        self.level = level
        self.power = power
        self.weight = weight
        self.owner = owner


        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

Mage_player = CharacterPrototype("Mage", 200, 10, 5, 100, "Przemek")
print(Mage_player)

Warrior_player = CharacterPrototype("Warrior", 400, 15, 2, 250, "Andrzej")
print(Warrior_player)


class Prototype:
    def __init__(self) -> None:
        self.objects = dict()

    def add_prototype(self, id_: int, obj: Any) -> None:
        self.objects[id_] = obj

    def del_prototype(self, id_: int) -> None:
        del self.objects[id_]

    def clone(self, id_: int, **kwargs: dict) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")

prototypes = Prototype()
prototypes.add_prototype("1", Mage_player)
another_player = prototypes.clone("1", owner="other")
print(another_player)


#c

class Configuration:
    def __init__(
            self,
            type: str,
            windows: str,
            min_graphic_card: str,
            min_RAM: int,
            author: str,
            **kwargs: dict,




        ) -> None:
        self.type = type,
        self.windows = windows,
        self.min_graphic_card = min_graphic_card,
        self.min_RAM = min_RAM,
        self.author = author


        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

app1 = Configuration("Game", "Windows 10", "NVIDIA GTX 1050", 4, "Przemek Hubacz")
print("Original Configuration:")
print(app1)

class ConfigurationPrototype:
    def __init__(self) -> None:
        self.objects = {}

    def add_prototype(self, id_: str, obj: Configuration) -> None:
        self.objects[id_] = obj

    def clone(self, id_: str, **kwargs: dict) -> Configuration:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")


confprototype = ConfigurationPrototype()
confprototype.add_prototype("1", app1)
app_other_conf = confprototype.clone("1", author = "Bogdan Malanoski", type = "WEB app", min_RAM = 2)
print("Cloned configuration:")
print(app_other_conf)

print()
"""

#Zad5

from typing import Self

class DatabaseConnection:
    _instance: Self = None

    def __new__(cls, *args: list, **kwargs: dict):
        if cls._instance is None:
            instance = super().__new__(cls)
            cls._instance = instance

        return cls._instance

    def __init__(self, db_name: str, host: str, port: int) -> None:

        self.db_name = db_name
        self.host = host
        self.port = port
        print(f"Połączono z bazą danych: {self.db_name} na {self.host}:{self.port}")


    def connect(self):
        print(f"Połączono z bazą danych: {self.db_name} na {self.host}:{self.port}")

    def disconnect(self):
        print(f"Rozłączono z bazą danych: {self.db_name} na {self.host}:{self.port}")

db1 = DatabaseConnection("MyDataBase", "localhost1", 2931)
db2 = DatabaseConnection("AnotherDataBase", "localhost", 2932)

print(f"db1 i db2 to ta sama instancja? {db1 is db2}")

db1.connect()
db2.disconnect()






















































