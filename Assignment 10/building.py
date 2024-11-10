from elevator import Elevator
class Building :
    def __init__(self, num_top, num_bot, num_ele):
        self.top_floor_number = num_top
        self.bottom_floor_number = num_bot
        self.ele_list=[]
        for i in range(num_ele):
            ele=Elevator(num_top, num_bot)
            self.ele_list.append(ele)

    def run_elevator(self,ele_num,des_floor):
        self.ele_list[ele_num].go_to_floor(des_floor)

    def fire_alarm(self):
        for i in range(len(self.ele_list)):
            self.run_elevator(i,self.bottom_floor_number)

