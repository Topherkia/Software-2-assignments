from building import Building
building1=Building(7,1,3)
building1.run_elevator(0,5)
building1.run_elevator(1,7)
building1.run_elevator(2,2)
for i in range(3):
    print((building1.ele_list[i]).current_floor)
