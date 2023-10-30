class Elevator:
    def __init__(self):
        self.current_floor = 1
    def go_to_floor(self, target_floor):
        if self.current_floor > target_floor:
            print(f"Elevator is moving up from floor{self.current_floor} to the{target_floor} ")
            self.current_floor = target_floor
        elif self.current_floor > target_floor:
            print(f"Elevator is moving down from floor{self.current_floor} to the{target_floor} ")
            self.current_floor = target_floor

        else:
            print(f"Elevator is already on floor{target_floor},")


class Building:
    def __init_(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator() for _ in range(num_elevators)]


    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            if self.bottom_floor <= destination_floor <= self.top_floor:
                elevator.go_to_floor(destination_floor)
            else:
                print(f"Invalis destination floor{destination_floor} the building has floors from{self.bottom_floor} to {self.top_floor}")

        else:
            print(f"invalid elevator number{elevator_number}. choose an available elevator.")

building = Building()

bottom_floor = 1
top_floor = 10
num_elevators = 3

building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)











