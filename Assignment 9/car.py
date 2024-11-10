class Car:
    def __init__(self, reg_num, max_speed, current=0, distance=0):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = current
        self.travelled_distance = distance

    def accelerate(self,change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,number_of_hours):
        self.travelled_distance += number_of_hours * self.current_speed
