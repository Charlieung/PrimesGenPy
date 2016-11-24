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