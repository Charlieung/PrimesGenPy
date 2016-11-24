import math

class PrimeGenerator:
    def __init__(self):
        self.memory = []
    
    def check(self, num):
        if num == 1:
            return False

        sqrt_num_rounded_up = int(math.sqrt(num)+1)
        return not any([num % n == 0 for n in range(2,sqrt_num_rounded_up)])

    def generate(self, num):
        if num <= len(self.memory):
            return self.memory[num]

        primes = len(self.memory)
        nth_prime = self.memory[-1] if len(self.memory) != 0 else 1
        
        while primes != num:
            nth_prime += 1
            if self.check(nth_prime):
                primes += 1
                self.memory.append(nth_prime)
        return nth_prime

    