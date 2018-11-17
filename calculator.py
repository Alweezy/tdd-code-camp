"""Create a calculator that accepts 2 integers and returns their sum
"""


class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_numbers(self):
        if isinstance(self.a, str) or isinstance(self.b, str):
            return 'Inputs should be integers only!'
        else:
            return self.a + self.b

    def multiply_numnbers(self):