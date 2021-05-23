# Calling methods
class my_class:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

my_class_0 = my_class()
my_class_0.method() # method
                    # other