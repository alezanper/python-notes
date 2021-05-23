# Inheritance Order example

class One:
    def do_it(self):
        print("do_it from One")
    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it from Two")

one = One()
two = Two()

one.doanything()    # do_it from One
two.doanything()    # do_it from Two