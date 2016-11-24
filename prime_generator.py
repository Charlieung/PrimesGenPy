import math

class PrimeGenerator:
    def __init__(self):
        pass
    
    def check(self, num):
        sqrt_num_rounded_up = int(math.sqrt(num)+1)
        return not any([num % n == 0 for n in range(2,sqrt_num_rounded_up)])
