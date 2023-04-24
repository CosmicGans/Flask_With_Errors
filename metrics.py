class Metrics: 

    def __init__(self, start_list=None) -> None:
        if start_list: 
            self.numbers_list = start_list 
        else: 
            self.numbers_list = [] 
    

    def get_current_average(self): 
        return sum(self.numbers_list) / len(self.numbers_list) 

    def get_current_sum(self): 
        return sum(self.numbers_list) 

    def append(self, integer): 
        self.numbers_list.append(integer) 
    def reset(self): 
        self.numbers_list = []