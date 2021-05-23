# Stack implementation (procedural way)
print("Stack definition, procedural way")
stack = []
def push(val):
    stack.append(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(3)
push(2)
push(1)
print(pop())    # 1
print(pop())    # 2
print(pop())    # 3

# Stack implementation (object way)
# Stack object definition
class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# Creating objects
print("\nStack definition, POO way")
stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())