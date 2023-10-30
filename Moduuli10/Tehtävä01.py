class Elevator:


    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)

        else:
            print(f"Due to a technical fault, the use of the elevator is prohibited today, stay in {self.current_floor}")


    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.top_floor:

            self.current_floor += 1
            print(f"Elevator is on floor {self.current_floor}")


    def floor_down(self, target_floor):

        while self.current_floor > target_floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is on floor {self.current_floor}")






elevator = Elevator(1,10)
elevator.go_to_floor(7)
elevator.go_to_floor(1)