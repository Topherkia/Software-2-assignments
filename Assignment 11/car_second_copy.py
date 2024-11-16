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

    def print_information(self):
        print(f"Registration Number: {self.registration_number}\n"
              f"maximum speed: {self.maximum_speed}\n"
              f"current speed: {self.current_speed}\n"
              f"distance: {self.travelled_distance}")

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed,battery_capacity, current=0, distance=0):
        self.battery_capacity = battery_capacity
        self.current_speed = current
        self.travelled_distance = distance
        super().__init__(reg_num, max_speed)

    def print_information(self):
        super().print_information()
        print(f"battery capacity: {self.battery_capacity}\n")

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, gasoline_tank_volume, current=0, distance=0):
        self.gasoline_tank_volume = gasoline_tank_volume
        self.current_speed = current
        self.travelled_distance = distance
        super().__init__(reg_num, max_speed)

    def print_information(self):
        super().print_information()
        print(f"gasoline_tank_volume: {self.gasoline_tank_volume}\n")