class Accumulator:
    def __init__(self):
        self._total = 0

    @property
    def count(self):
        return self._total

    def add(self, value: int = 1):
        self._total += value
