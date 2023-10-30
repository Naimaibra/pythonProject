class Elevator:
    def __init__(self, id, all_floors):
        self.id = id
        self.current_floor = 0
        self.all_floors = all_floors

    def move_to_floor(self, target_floor):
        self.current_floor = target_floor

    def __str__(self):
        return f'Elevator {self.id} is on floor {self.current_floor}'

class ElevatorSystem:
    def __init__(self, num_elevators, all_floors):
        self.elevators = [Elevator(i, all_floors) for i in range(num_elevators)]
        self.all_floors = all_floors

    def request_elevator(self, target_floor):
        pass

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.move_to_floor(0)

    if __name__ == "__main__":
    num_elevators = 3
    all_floors = 10

    elevator_system = elevator_system(num_elevators, all_floors)

    for elevator in elevator_system.elevators:
        print(elevator)


    elevator_system.fire_alarm()

    for elevator in elevator_system.elevators:
        print(elevator)
