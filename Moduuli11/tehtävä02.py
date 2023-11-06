class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)


electric_car.current_speed = 60
gasoline_car.current_speed = 55

electric_car.travelled_distance = electric_car.current_speed * 3
gasoline_car.travelled_distance = gasoline_car.current_speed * 3


print(f'Electric Car (Registration Number: {electric_car.registration_number})\n'
      f'Travelled Distance: {electric_car.travelled_distance} km')
print(f'Gasoline Car (Registration Number: {gasoline_car.registration_number})\n'
      f'Travelled Distance: {gasoline_car.travelled_distance} km')

