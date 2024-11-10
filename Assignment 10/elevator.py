class Elevator :
    def __init__(self, top, bottom):
        self.target_floor= None
        self.top_floor = top
        self.bottom_floor = bottom
        self.current_floor = self.bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor+1
            print(f"Going up: Now at floor {self.current_floor}")
        else:
            print(f"Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor-1
            print(f"Going down: Now at floor {self.current_floor}")
        else:
            print(f"Elevator already at the bottom floor.")

    def go_to_floor(self, target_floor):
        self.target_floor = target_floor
        if self.target_floor == self.current_floor:
            print("Elevator already in the target floor")
            return
        while self.current_floor != target_floor:
            if self.target_floor < self.bottom_floor or self.target_floor > self.top_floor:
                print("Target floor is out of range.")
                break
            if self.target_floor > self.current_floor:
                self.floor_up()
            if self.target_floor < self.current_floor:
                self.floor_down()
