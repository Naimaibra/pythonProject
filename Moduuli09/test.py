import colorama
from colorama import Fore, Style
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.current_speed = 0
        self.travelled_distance = 0
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        if speed_change > 0:
            self.current_speed += speed_change
        else:
            self.current_speed = max(0, self.current_speed + speed_change)
        self.current_speed = min(self.current_speed, self.max_speed)

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

def main():
    colorama.init()  # Initialize Colorama for colored output

    cars = []
    for i in range(10):
        car = Car("ABC-" + str(i + 1), random.randint(100, 200))
        cars.append(car)

    race_over = False
    while not race_over:
        for car in cars:
            car.drive(1)
            car.accelerate(random.randint(-10, 15))

        for car in cars:
            if car.travelled_distance >= 10000:
                race_over = True

    print("Race Results:")
    for car in cars:
        print(f"Car: {Fore.GREEN}{car.registration_number}{Style.RESET_ALL}, Distance: {car.travelled_distance} km")

    for car in cars:
        if car.travelled_distance >= 10000:
            print(f"Winner: {Fore.RED}{car.registration_number}{Style.RESET_ALL}")

