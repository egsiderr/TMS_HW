class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.surname_list = []
        self.free_seats = True
        self.dict_seats = {}

    def board_unboard(self, state, *surname_list):
        if state == "board":
            for name in surname_list:
                if len(self.surname_list) < self.max_seats:
                    self.surname_list.append(name)
                    self.dict_seats[name] = len(self.surname_list)
                    self.free_seats = len(self.surname_list) < self.max_seats
                else:
                    print(f"No free seats for {name}")
        elif state == "unboard":
            for name in surname_list:
                if name in surname_list:
                    self.surname_list.remove(name)
                    del self.dict_seats[name]
                    self.free_seats = len(self.surname_list) < self.max_seats
                else:
                    print(f"{name} not in bus")
                
    def change_speed(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0
            
    def __contains__(self, name):
        return name in self.surname_list
    
    def __add__(self, name):
        self.board_unboard("board", name)
        return self
    def __rmv__(self, name):
        self.board_unboard("unboard", name)

bus = Bus(7, 60)
bus.board_unboard("board", "Popkin", "Pipkin")
print(bus.surname_list)
bus.board_unboard("unboard", "Popkin")
print(bus.surname_list)
bus.change_speed(30)
print(bus.speed)
bus.change_speed(10)
print(bus.speed)