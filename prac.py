from copy import deepcopy
from typing import Any

class Car:
    def __init__(
            self,
            brand: str,
            model: str,
            engine: str,
            gearbox: str,
            body_type: str,
            licence_plate: str,
            owner: str,
            **kwargs: dict,
    ) -> None:
        self.brand = brand
        self.model = model
        self.engine = engine
        self.gearbox = gearbox
        self.body_type = body_type
        self.licence_plate = licence_plate
        self.owner = owner

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = []

        for key, val in vars(self).items():
            summary.append(f"{key}: {val}\n")

        return "".join(summary)

ford_focus = Car("Ford", "Focus mk2", "1.6D", "manual", "hatchback", "XX YYYYY", "Wujek Janusz", color="silver", doors=5)

print(ford_focus)

print()
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
prototypes.add_prototype("1", ford_focus)
another_car = prototypes.clone("1", license_plate="AA BBBBB", owner="other")

print(another_car)