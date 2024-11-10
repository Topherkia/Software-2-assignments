from car import Car
import random
race_list=[]
for i in range (10):
    max_speed=random.randint(100,200)
    race_car=Car(f"ABC-{i+1}",max_speed)
    race_list.append(race_car)
for i in range(10):
    print(f"car{i+1} reg num={race_list[i].registration_number}")
for i in range(10):
    print(f"car{i + 1} max speed={race_list[i].maximum_speed}")

while_breaker=0
winner=""
while while_breaker==0:
    for i in range(10):
        if race_list[i].travelled_distance>=10000:
            winner=race_list[i]
            while_breaker=while_breaker+1
    for i in range(10):
        speed_change=random.randint(0,25)
        speed_change=speed_change-10
        race_list[i].accelerate(speed_change)
        race_list[i].drive(1)

for i in range(10):
    print(f"car{i+1} traveled distance={race_list[i].travelled_distance}")
print(f"winner={winner.registration_number}")
