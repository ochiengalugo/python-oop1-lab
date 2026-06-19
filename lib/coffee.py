class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            raise ValueError("size must be Small, Medium, or Large")
        self._size = value

    def tip(self):
        self.price += 1