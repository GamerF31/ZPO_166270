from abc import ABC, abstractmethod
'''
class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, price: float) -> float:
        pass

class PolandTax(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.23

class GermanyTax(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.19

class USA_Tax(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.07

class TaxCalculator:
    def __init__(self, strategy: TaxStrategy):
        self.strategy = strategy

    def calculate(self, price: float) -> float:
        return self.strategy.calculate_tax(price)

product_price = 100
for strategy in [PolandTax(), GermanyTax(), USA_Tax()]:
    calculator = TaxCalculator(strategy)
    print(f"Podatek: {calculator.calculate(product_price):.2f}")

#b
class AttackGame(ABC):
    def attack(self) -> str:
        pass

class AgressiveAttack(AttackGame):
    def attack(self) -> str:
        return "Ten kutas zaatakował mnie agresywnie"

class DeffensiveAttack(AttackGame):
    def attack(self) -> str:
        return "Ten kutas atakuje jak jakaś ciota"

class GoodOrBadAttack(AttackGame):
    def attack(self) -> str:
        return "Chuj wie co on odpierdala"

class Character:
    def __init__(self, power: float, height, strategy: AttackGame):
        self.power = power
        self.height = height
        self.strategy = strategy

    def StrategyAttack(self):
        print(f"My strategy is {self.strategy.attack()}")

heros = Character(10, 200, DeffensiveAttack())
print(heros.StrategyAttack())


#c
class SortStrategy(ABC):
    def sort(self, data: list[int]) -> list[int]:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Używam bubble sorta")
        arr = data.copy()
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class MergeSort(SortStrategy):
    def sort(self, data) -> list[int]:
        print("Używam merge sorta")
        return sorted(data)


class QuickSort(SortStrategy):
    def sort(self, data):
        print("Używam quick sorta")
        return sorted(data)

numbers = [1, 6, 3, 4, 5, 2, 7, 8, 9, 10]
bubble = MergeSort()
sorted_numbers = bubble.sort(numbers)
print(sorted_numbers)
'''
from typing import Self
#Zad2
#a
'''
class Iterator:
    n: int
    add: int
    limit: int
    k: int

    def __init__(self, limit: int) -> None:
        self.n = 0
        self.limit = limit
        self.add = 1

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.n < self.limit:
            self.n += self.add
            self.add += 2
            return self.n

        raise StopIteration
iterator = Iterator(20)
while 1:
    print(next(iterator))

#b

from typing import List, Iterator

class Order:
    def __init__(self, id: int, status: str):
        self.id = id
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, status={self.status})"

class OrderIterator(Iterator):
    def __init__(self, orders: List[Order], status: str):
        self.orders = orders
        self.status = status
        self.index = 0
        self.filtered_orders = [order for order in self.orders if order.status == self.status]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.filtered_orders):
            order = self.filtered_orders[self.index]
            self.index += 1
            return order
        else:
            raise StopIteration

orders = [
    Order(1, "nowe"),
    Order(2, "w realizacji"),
    Order(3, "zrealizowane"),
    Order(4, "nowe"),
    Order(5, "w realizacji"),
]

iterator = OrderIterator(orders, "nowe")

for order in iterator:
    print(order)

print("Sena magłiszana i jesty bambo bambo")
#c
from typing import Generator


def prime_generator(limit: float) -> Generator:
    n = 1
    gen_sum = 0.0
    while gen_sum <= limit:
        gen_sum += 1/n
        yield gen_sum
        n += 1

gen = prime_generator(5.0)
for i in gen:
    print(i)


#Zad3
#a
class Document(ABC):
    name: str
    content: str

    def __init__(self, name: str, content: str) -> None:
        self.name = name
        self.content = content

    @abstractmethod
    def save(self) -> str:
        pass

    @abstractmethod
    def show_content(self) -> str:
        pass

    def show_extension(self) -> str:
        pass

    def show_file(self) -> None:
        self.save()
        self.show_content()
        self.show_extension()


class PDF(Document):
    def save(self) -> str:
        print("PDF file saved.")

    def show_content(self) -> str:
        print(self.content)

    def show_extension(self) -> str:
        print("PDF File")


class DOCX(Document):
    def save(self) -> str:
        print("DOCX file saved.")

    def show_content(self) -> str:
        print(self.content)

    def show_extension(self) -> str:
        print("DOCX File")


class TXT(Document):
    def save(self) -> str:
        print("TXT file saved.")

    def show_content(self) -> str:
        print(self.content)

    def show_extension(self) -> str:
        print("TXT File")


pdf_file = PDF("PlikPDF", "To jest zawartosc pliku PDF")
docx_file = DOCX("PlikDOCX", "To jest zawartosc pliku DOCX")
txt_file = TXT("PlikTXT", "To jest zawartosc pliku TXT")

print("")
pdf_file.show_file()
print("")
docx_file.show_file()
print("")
txt_file.show_file()
print("")
'''
#b
from abc import ABC, abstractmethod


class OrderProcessor(ABC):

    def process_order(self):
        self.receive_order()
        self.prepare_order()
        self.ship_order()
        self.send_confirmation()

    @abstractmethod
    def receive_order(self):
        pass

    @abstractmethod
    def prepare_order(self):
        pass

    @abstractmethod
    def ship_order(self):
        pass

    def send_confirmation(self):
        print("Order has been processed and confirmation sent.")


class StandardDeliveryOrder(OrderProcessor):
    """
    Realizacja zamówienia z dostawą standardową.
    """

    def receive_order(self):
        print("Receiving the order through standard process.")

    def prepare_order(self):
        print("Preparing the order for standard delivery.")

    def ship_order(self):
        print("Shipping the order via standard delivery method.")


class ExpressDeliveryOrder(OrderProcessor):
    """
    Realizacja zamówienia z dostawą ekspresową.
    """

    def receive_order(self):
        print("Receiving the order through expedited process.")

    def prepare_order(self):
        print("Preparing the order for express delivery.")

    def ship_order(self):
        print("Shipping the order via express delivery method.")


class InPersonPickupOrder(OrderProcessor):
    """
    Realizacja zamówienia z odbiorem osobistym.
    """

    def receive_order(self):
        print("Receiving the order for in-person pickup.")

    def prepare_order(self):
        print("Preparing the order for in-person pickup.")

    def ship_order(self):
        print("Order is ready for pickup at the designated location.")

'''
order_standard = StandardDeliveryOrder()
order_standard.process_order()

order_express = ExpressDeliveryOrder()
order_express.process_order()

order_pickup = InPersonPickupOrder()
order_pickup.process_order()
'''
#c


class FileExporter(ABC):
    def export(self, data):
        self.open_file()
        self.write_data(data)
        self.close_file()

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def close_file(self):
        pass


class CSVExporter(FileExporter):
    def open_file(self):
        print("Opening CSV file for writing.")

    def write_data(self, data):
        print(f"Writing data to CSV: {data}")

    def close_file(self):
        print("Closing CSV file.")


class JSONExporter(FileExporter):
    def open_file(self):
        print("Opening JSON file for writing.")

    def write_data(self, data):
        print(f"Writing data to JSON: {data}")

    def close_file(self):
        print("Closing JSON file.")


class XMLExporter(FileExporter):
    def open_file(self):
        print("Opening XML file for writing.")

    def write_data(self, data):
        print(f"Writing data to XML: {data}")

    def close_file(self):
        print("Closing XML file.")


data = "Sample data"

csv_exporter = CSVExporter()
csv_exporter.export(data)

json_exporter = JSONExporter()
json_exporter.export(data)

xml_exporter = XMLExporter()
xml_exporter.export(data)

