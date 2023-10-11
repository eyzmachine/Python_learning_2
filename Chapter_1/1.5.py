class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        
    def can_add(self, v): return(v + self.current) <= self.capacity
    
    def add(self, v):
        if self.can_add(v):
            self.current += v

class Buffer:
    def __init__(self):
       self.enum = list()
    
    def add(self, *a):
        for item in a:
            self.enum.append(item)
            if (self.enum.__len__() == 5):
                print(sum(self.enum))
                self.enum.clear()
    
    def get_current_part(self):
        return self.enum


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]