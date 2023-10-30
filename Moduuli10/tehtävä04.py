import random
import time


class Car:
    def __init__(self, name, speed, acceleration):
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.distance = 0

    def drive(self):
        speed_change = random.uniform(-5, 5)
        self.speed += speed_change
        self.distance += self.speed

    def __str__(self):
        return f"{self.name}: {self.distance:.2f} km"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.drive()

    def print_status(self):
        print("Race Status:")
        for car in self.cars:
            print(car)
        print("")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False


def main():
    car_names = ["Car 1", "Car 2", "Car 3", "Car 4", "Car 5", "Car 6", "Car 7", "Car 8", "Car 9", "Car 10"]
    cars = [Car(name, random.uniform(100, 150), random.uniform(5, 15)) for name in car_names]

    race = Race("Grand Demolition Derby", 8000, cars)

    while not race.race_finished():
        race.hour_passes()
        if race.race_finished() or race.distance % 10 == 0:
            race.print_status()
        time.sleep(1)

    print("Race Finished!")


if __name__ == "__main__":
    main()
