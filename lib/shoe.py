#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        # tests expect __init__ signature to be (brand, size)
        self.brand = brand
        # initialize the internal storage, then delegate to setter for validation/assignment
        self._size = None
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            # test expects this exact message on stdout when given non-int :contentReference[oaicite:2]{index=2}
            print("size must be an integer")

    def cobble(self):
        # test captures this exact output and then checks condition attr :contentReference[oaicite:3]{index=3}
        print("Your shoe is as good as new!")
        self.condition = "New"
