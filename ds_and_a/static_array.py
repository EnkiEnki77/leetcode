class StaticArray:
    """A type of array which has an immutable size determined at it's initialization.
        All of it's allocated spaces in memory are contiguous."""

    def __init__(self, arr):
        # Our initialized array
        self.array = arr
        # The size of our array
        self.size = len(arr)
        # The pointer that tells us where the last element of our array is.
        self.pointer = self.size - 1


    def read_index(self, index):
        """Read from the array at the given index assuming it exists"""

        try:
            print(f"Reading index {index} from array")
            print("""This is an O(1) time complexity operation, because an index is always 
            tied directly to an elements address in memory. Making it instantly accessible, no 
            matter the size of the data structure.""")
            return self.array[index]
        except IndexError:
            print("This index does not exist.")


    def print_size(self):
        """Print the size of the array"""

        print(f"The size of this static array is: {self.size}")


    def print_all_elements(self):
        """Print all elements of the array"""

        if self.array:
            print(f"Reading all elements from array")
            print("This is an O(n) time complexity operation, because the number of operations grows linearly with the size of the array.")
            for i in range(self.size):
                print(f"Element #{i+1} in the array: {self.array[i]}")
            print(f"There are {self.size} elements in the array. So {self.size} operations were made")
        else:
            print("No elements in the array.")


    # Defaulting the index param to None, indicating it's empty if no argument is given for it.
    def pop(self, index = None):
        """Delete the element at given index. Return the deleted element. If no index is given, delete the last element"""

        # If valid index given or no index given run try block, else catch IndexError exception
        try:
            # If no index is given or the index given is the last index pop the last element
            if self.array and not index or self.array and index == self.pointer:
                print(f"Popping from end of array")
                print("""This is a O(1) time complexity operation, because the end of the array 
                is always instantly accessible through the pointer, and no elements must be 
                shifted when popping.""")
                popped_element = self.array[self.pointer]
                # In static arrays indexes are never deleted, just filled with a value indicating
                # they are empty
                self.array[self.pointer] = -1
                # We need to decrement the size since an element has been removed. This will in
                # turn move the pointer to the new last element
                self.size -= 1
                # Returning the popped element in case we'd like to utilize it for something one
                # last time
                return popped_element
            # If an index is given that isnt the last one, pop given index, and shift elements after index over 1
            # so they remain contiguous with the elements before index.
            elif self.array:
                print(f"Popping from {index} index of array")
                print("""This is an O(n) time complexity operation, because in the worst case 
                (the 0 index is popped), we then have to shift over every element.""")
                popped_element = self.array[index]

                # Shift all elements after popped element over to ensure they remain contiguous
                # But only if there is more than one element in the array.
                if self.size > 1:
                    for i in range(index + 1, self.size):
                        self.array[i - 1] = self.array[i]

                # Setting the element at the pointer to empty
                self.array[self.pointer] = -1
                # Reducing size, to indicate an element was removed. In turn, moving the pointer
                # to the new last element.
                self.size -= 1

                return popped_element
            else:
                print("No elements in the array to pop.")
        except IndexError:
            print("This index does not exist.")


    def append(self, element):
        """append an element to the end of an array, given there is an empty space."""

        # Check if there is a space in the array after the pointer, we can assume it's empty.
        if len(self.array) > self.pointer + 1:
            # Add element to empty space
            self.array[self.pointer + 1] = element
            # Increment size, in turn setting pointer to the new element.
            self.size += 1
        # If array is full
        else:
            print("Array is at maximum capacity.")






