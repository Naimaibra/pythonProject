class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def intro(self):
        print(f"Registration Number: {my_car.registration_number}\n"
              f"Maximum Speed: {my_car.max_speed} km/h\n"
              f"Current Speed: {my_car.current_speed} km/h\n"
              f"Travelled Distance: {my_car.travelled_distance} km\n")

my_car = Car("ABC-123", 142)
my_car.intro()
