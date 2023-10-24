
from colorama import init, Fore
import random

# Initialize colorama
init(autoreset=True)

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.odometer = 0
        self.speed = 0
        self.max_speed = max_speed


    def print_info(self):
        print(f"Bugatti{Fore.YELLOW}" f"Huippunopeus{self.max_speed}" f"matkamittari{self.odometer}" f"nopeus {self.speed}")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change

    def walk(self, hours):
        if self.odometer > -1:
            self.odometer = self.speed * hours + self.odometer

cars = []
for i in range(10):
    car = Car("ABC-" + str(i + 1), random.randint(100, 200))
    cars.append(car)

race_over = False

while not race_over:
    for car in cars:
        car.walk(1)
        car.accelerate(random.randint(-10, 15))

    for car in cars:
        if car.odometer >= 10000:
            race_over = True

for car in cars:
    car.print_info()


for car in cars:
    if car.odometer >= 10000:
        print(f"{Fore.BLUE}Voittaja on {car.register_number}")
