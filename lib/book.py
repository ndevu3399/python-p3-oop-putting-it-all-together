#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # tests expect __init__ signature to be (title, page_count)
        self.title = title
        # initialize the internal storage, then delegate to setter for validation/assignment
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            # test expects this exact message on stdout when given non-int :contentReference[oaicite:0]{index=0}
            print("page_count must be an integer")

    def turn_page(self):
        # test captures this exact output :contentReference[oaicite:1]{index=1}
        print("Flipping the page...wow, you read fast!")
