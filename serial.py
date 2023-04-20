"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initializing generator starting at start (0 is default value)"""
        self.start = start
        self.next_serial = start

    def __repr__(self):
        """Shows better representation in terminal"""
        return f'SerialGenerator start = {self.start} next = {self.next_serial}'

    def generate(self):
        """Returning next consecutive number"""
        self.next_serial += 1
        return self.next_serial - 1

    def reset(self):
        """Reset number back to start"""
        self.next_serial = self.start
