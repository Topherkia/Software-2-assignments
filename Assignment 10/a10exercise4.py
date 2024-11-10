from race import Race
players=[]
for i in range (10):
    players.append(f"ABC-{i}")
race1=Race("Grand Demolition Derby",8000,players)
while_counter=0
while True:
    if race1.race_finished():
        race1.print_status()
        break
    race1.hour_passes()
    while_counter+=1
    if while_counter==10:
        race1.print_status()
        while_counter=0
