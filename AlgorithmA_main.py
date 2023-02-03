import string
from decimal import *
import math

import mpmath


class GetPrime:

    def __init__(self):
        eulers_number = self.generate_euler_number()
        digit_string = self.process_to_string(eulers_number)
        first_prime = self.find_prime(digit_string)
        print("First Prime is: ", first_prime)

    def generate_euler_number(self):
        e = Decimal("1.0")
        for i in range(1, 1000):
            numerator = Decimal("1.0")
            denominator = Decimal(math.factorial(i))
            getcontext().prec = 1000
            iteration = numerator.__truediv__(denominator)
            e = e.__add__(iteration)
        e = e.__mul__(Decimal(".1"))
        return e

    def process_to_string(self, number):
        digits = str(number)
        digits = digits[2:len(digits)]
        return digits

    def find_prime(self, digits):
        for i in range(0, len(digits)-10):
            number_to_check = digits[i:i+10]
            number = int(number_to_check)
            if self.check_prime(number):
                return number

    def check_prime(self, number_to_chk):
        is_prime = True
        if number_to_chk % 2 == 0 or number_to_chk % 3 == 0 or number_to_chk % 5 == 0:
            is_prime = False
        else:
            limit = math.ceil(math.sqrt(number_to_chk))
            i = 7
            while i <= limit:
                if number_to_chk % i == 0:
                    is_prime = False
                    break
                else:
                    i = i + 2
        return is_prime


def main():
    trial = GetPrime()


main()


