"""
    inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
    composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.
"""
# Composition
import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller
    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

