import math

class PrimeGenerator:
    def __init__(self):
        pass
    
    def check(self, num):
        if num == 1:
            return False

        sqrt_num_rounded_up = int(math.sqrt(num)+1)
        return not any([num % n == 0 for n in range(2,sqrt_num_rounded_up)])

    def generate(self, num):
        primes = 0
        start = 1
        while primes != num:
            start += 1
            if self.check(start):
                primes += 1
        return start