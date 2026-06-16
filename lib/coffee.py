class Coffee:
    def __init__(self, size: str, price: float):
        self.size = size      # Uses the setter below for validation
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Validation: Ensure size is Small, Medium, or Large
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("If not print 'Size must be Small, Medium, or Large'")
            return
        self._size = value

    def tip(self):
        # Methods specified in the steps
        print("Will print 'This coffee is great, here's a tip!'")
        # Will increase price by 1
        self.price += 1