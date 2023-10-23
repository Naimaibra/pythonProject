class Car:
    def __init__(self, name, registration_number, max_speed, cur_speed, travelled_distant):
        self.name = name
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.travelled_distance = travelled_distant

    def accelerate(self, change):
        if change > 0:
            self.cur_speed += change
        else:
            self.cur_speed = max(0, self.cur_speed + change)
        self.cur_speed = min(self.cur_speed, self.max_speed)

    def new_speed(self):
        print(f"{self.name}'s current speed is {self.cur_speed} km/h")


car = Car("Bugatti", "ABC-123", 142, 0, 0)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.new_speed()
car.accelerate(-200)
car.new_speed()
