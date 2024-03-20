import random


class Random:
    def __init__(self) -> None:
        self.hex = "0123456789abcdef"

    def generate(self, n):
        if n < 6:
            n = 6
        if n > 16:
            n = 16
        random_value = ""
        for i in range(n):
            random_value += random.choice(self.hex)
        return random_value
