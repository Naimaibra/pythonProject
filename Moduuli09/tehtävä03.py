class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def intro(self):
        print(f"Registration Number: {self.registration_number}\n"
              f"Maximum Speed: {self.max_speed} km/h\n"
              f"Current Speed: {self.current_speed} km/h\n"
              f"Travelled Distance: {self.travelled_distance} km\n")

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


my_car = Car("ABC-123", 142)
my_car.current_speed = 60
my_car.drive(1.5)
my_car.intro()
