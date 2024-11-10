from car_copy import Car
import random
class Race:
    def __init__(self, name,kilometers,car_list):
        self.name = name
        self.distance_in_kilometers = kilometers
        self.car_list = car_list
        for i in range(len(self.car_list)):
            self.car_list[i]=Car(str(car_list[i]),random.randint(200,300))

    def hour_passes(self):
        for i in range(len(self.car_list)):
            speed_change=random.randint(0,25)
            speed_change=speed_change-10
            self.car_list[i].accelerate(speed_change)
            self.car_list[i].drive(1)

    def print_status(self):
        for i in range(len(self.car_list)):
            print(f"{self.car_list[i].registration_number} = {self.car_list[i].travelled_distance}")

    def race_finished(self):
        for i in range(len(self.car_list)):
            if self.car_list[i].travelled_distance > self.distance_in_kilometers:
                return True
        return False