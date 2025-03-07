# Stacks typically support three operations:
# Push to the end/top of the stack
# Pop from the end/top of the stack
# Look at the end/top of the stack


# All of the above operations are O(1) constant time

# All of the above operations are supported by a dynamic array, so we can implement a stack
# using one. A stack is essentially a subset of a dynamic array.

# We would have some sort of pointer that helps us determine where the top of the stack is.

# Stacks are considered a LIFO data structure. Last In First Out.
from ds_and_a.dynamic_array import DynamicArray

class Stack(DynamicArray):
    def __init__(self):
        pass