from car_second_copy import Car
from car_second_copy import ElectricCar
from car_second_copy import GasolineCar
car1=ElectricCar("ABC-15",180,52.5)
car2=GasolineCar("ACD-123",165,32.3)
car1.accelerate(60)
car2.accelerate(75)
car1.drive(3)
car2.drive(3)
car1.print_information()
car2.print_information()