from car import Car
car1=Car("ABC-123",142)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"current speed is: {car1.current_speed}")
car1.accelerate(-200)
print(f"current speed is: {car1.current_speed}")
