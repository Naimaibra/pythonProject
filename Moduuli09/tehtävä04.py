import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if change > 0:
            self.current_speed += change
        else:
            self.current_speed = max(0, self.current_speed + change)
        self.current_speed = min(self.current_speed, self.max_speed)

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

def main():
    car_list = []

    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        car_list.append(car)

    race_distance = 0

    while race_distance < 10000:
        for car in car_list:
            change_in_speed = random.randint(-10, 15)
            car.accelerate(change_in_speed)
            car.drive(1)
            race_distance = max(race_distance, car.travelled_distance)


    print(f"{'Registration Number':<15}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<25}{'Travelled Distance (km)':<30}")
    for car in car_list:
        print(f"{car.registration_number:<15}{car.max_speed:<20}{car.current_speed:<25}{car.travelled_distance:<30}")



