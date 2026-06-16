class Book:
    def __init__(self, title: str, page_count: int):
        # Initializing instance attributes
        self.title = title
        self.page_count = page_count  # Uses the setter below for validation

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Validation: Ensure it is an integer
        if not isinstance(value, int):
            print("If not print 'page_count must be an integer'")
            # Depending on your precise test file requirements, you might need to raise an error:
            # raise TypeError("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        # Method to simulate turning a page
        print("Will print 'Flipping the page...wow, you read fast!'")
    
        