from unittest import TestCase
from expects import expect, equal, be_true, be_false
from prime_generator import PrimeGenerator

class TestPrimeGenerator(TestCase):
    def test_can_check_if_prime(self):
        pgen = PrimeGenerator()
        expect(pgen.check(1)).to(be_false)
        expect(pgen.check(2)).to(be_true)
        expect(pgen.check(5)).to(be_true)
        expect(pgen.check(12)).to(be_false)

    def test_can_make_nth_prime(self):
        pgen = PrimeGenerator()
        expect(pgen.generate(2)).to(equal(3))
        expect(pgen.generate(5)).to(equal(11))

    def test_keeps_memory_of_primes(self):
        pgen = PrimeGenerator()
        expect(pgen.memory).to(equal([]))

        pgen.generate(2)
        expect(pgen.memory).to(equal([2,3]))

        pgen.generate(5)
        expect(pgen.memory).to(equal([2,3,5,7,11]))

        pgen.generate(4)
        expect(pgen.memory).to(equal([2,3,5,7,11]))
