class Metrics: 

    def __init__(self, start_list=None) -> None:
        if start_list: 
            self.numbers_list = start_list 
        else: 
            self.numbers_list = [] 
    

    def average(self): 
        return sum(self.numbers_list) / len(self.numbers_list) 

    def sum(self): 
        return sum(self.numbers_list) 

    def add(self, integer): 
        self.numbers_list.append(integer) 
    def reset(self): 
        self.numbers_list = []