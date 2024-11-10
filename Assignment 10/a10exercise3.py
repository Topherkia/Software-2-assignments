from building import Building
building2=Building(10,0,3)
building2.run_elevator(0,7)
building2.run_elevator(1,2)
building2.run_elevator(2,4)
for i in range(3):
    print((building2.ele_list[i]).current_floor)
building2.fire_alarm()
for i in range(3):
    print((building2.ele_list[i]).current_floor)
    