from timeit import timeit
from time import time
from abc import ABC, abstractmethod
from typing import Any
from typing import Self
from functools import wraps


class OldSystem:
    def print_old(self):
        print("Drukowanie w starym systemie")

class Adapter:
    def __init__(self, old_system: OldSystem):
        self.old_system = old_system

    def print_new(self):
        self.old_system.print_old()

old_system = OldSystem()

adapter = Adapter(old_system)

adapter.print_new()

#b)
class FahrenheitSensor:
    def get_temperature_fahrenheit(self) -> float:
        return 98.6

class FahrenheitAdapter:
    def __init__(self, fahrenheit_sensor: FahrenheitSensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature_float(self) -> float:
        fahrenheit = self.fahrenheit_sensor.get_temperature_fahrenheit()
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        return celsius

fahrenheit_sensor = FahrenheitSensor()

adapter = FahrenheitAdapter(fahrenheit_sensor)

temperature_celsius = adapter.get_temperature_float()

print(f"Temperatura w stopniach Celsjusza: {temperature_celsius:.2f}°C")

#c)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class PayPal:
    def make_payment(self, amount: float) -> str:
        return f"Płatność {amount} PLN została przetworzona przez PayPal"

class Stripe:
    def charge_payment(self, amount: float) -> str:
        return f"Płatność {amount} PLN została przetworzona przez Stripe"

class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal: PayPal):
        self.paypal = paypal

    def process_payment(self, amount: float) -> str:
        return self.paypal.make_payment(amount)

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe: Stripe):
        self.stripe = stripe

    def process_payment(self, amount: float) -> str:
        return self.stripe.charge_payment(amount)

paypal = PayPal()
stripe = Stripe()

paypal_adapter = PayPalAdapter(paypal)
stripe_adapter = StripeAdapter(stripe)

print(paypal_adapter.process_payment(100.0))
print(stripe_adapter.process_payment(200.0))


#Zad2
#a

class User(ABC):
    @abstractmethod
    def get_permissions(self):
        pass

class BasicUser(User):
    def get_permissions(self):
        return "Podstawowe uprawnienia"

class UserDecorator(User):
    def __init__(self, user: User):
        self._user = user

    @abstractmethod
    def get_permissions(self):
        return self._user.get_permissions()

class AdminDecorator(UserDecorator):
    def get_permissions(self):
        return f"{self._user.get_permissions()}, Uprawnienia Admina"

class ModeratorDecorator(UserDecorator):
    def get_permissions(self):
        return f"{self._user.get_permissions()}, Uprawnienia Moderatora"

class GuestDecorator(UserDecorator):
    def get_permissions(self):
        return f"{self._user.get_permissions()}, Uprawnienia Gościa"

user = BasicUser()
print(user.get_permissions())

admin_user = AdminDecorator(user)
print(admin_user.get_permissions())

moderator_user = ModeratorDecorator(admin_user)
print(moderator_user.get_permissions())

#b



def validate_form(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        form_data = kwargs

        password = form_data.get('password', '')
        if len(password) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków")

        age = form_data.get('age', 0)
        if age < 18:
            raise ValueError("Użytkownik musi mieć co najmniej 18 lat")

        return func(*args, **kwargs)

    return wrapper

@validate_form
def submit_form(password, age):
    return "Formularz został wysłany pomyślnie!"

try:
    print(submit_form(password="password123", age=2))
except ValueError as e:
    print(e)

try:
    print(submit_form(password="123", age=17))
except ValueError as e:
    print(e)

#c
print("PRÓBUJEMY TO---------------------------------------------------")
def timeit(fn: callable) -> callable:
    def wrapper(*args: list, **kwargs: dict) -> str:
        start = time()
        result = fn(*args, **kwargs)
        stop = time()

        print(f"Czas logowania wynosi: {stop - start:.4f}")


        return result

    return wrapper


class B:
    @timeit
    def a(self) -> str:
        return "greetings from a"

    @timeit
    def b(self) -> str:
        return "greetings from b"

b = B()

print(b.a())

#Zad3
#a

class File:
    def write(self) -> Any:
        print(f"Zapis pliku")

    def read(self) -> Any:
        print(f"Odczytujemy plik")

    def delete(self) -> Any:
        print(f"Usuwamy plik")

#b
class graphics_library:
    def __init__(self, scale: int, compressing_images: int, colors: str) -> None:
        this.scale = scale
        this.compressing_images = compressing_images
        this.colors = colors

    def scales(self) -> None:
        print("skalowanie grafiki")

    def colors(self) -> None:
        print("zmiana koloru")

    def compress(self) -> None:
        print("Kompresja obrazu")


#c

class Queues:
    def __init__(self, time: int, size: tuple, usbs: int, joints: int) -> None:
        this.time = time
        this.size = size
        this.joints = joints
        this.usbs = usbs

class Kafka:
    queues: Queues
    def __init__(self) -> None:
        self.queues = Queues(20, (10,20), 4, 4)

#Zad4

class File(ABC):
    _file: Self

    def __init__(self) -> None:
        self.file = None

    @property
    def file(self) -> Self:
        return self._file

    @file.setter
    def file(self, file: Self) -> None:
        self._file = file

    def get_file(self) -> Self:
        return self._file

    def add(self, component: Self) -> None:
        pass

    def remove(self, component: Self) -> None:
        pass


class Directory(ABC):
    _directory: Self

    def __init__(self) -> None:
        self.directory = None

    @property
    def directory(self) -> Self:
        return self._file

    @directory.setter
    def directory(self, directory: Self) -> None:
        self._directory = directory

    def get_file(self) -> Self:
        return self._directory

    def add(self, component: Self) -> None:
        pass

    def remove(self, component: Self) -> None:
        pass









