class StaticArray:
    """A type of array which has an immutable size determined at it's initialization.
        All of it's allocated spaces in memory are contiguous."""

    def __init__(self, arr):
        # Our initialized array
        self.array = arr
        # The amount of elements in our array at any given moment
        self.length = 0
        # Sets length property, accounting for indexes array has indicated are empty with a -1.
        for i in range(len(arr)):
            if arr[i] > -1:
                self.length += 1
        # The pointer that tells us where the last element of our array is.
        self.pointer = self.length - 1
        # The max_capacity of the array, determined at initialization. This is immutable
        self.max_capacity = len(arr)


    def at_max_capacity(self):
        """Checks if the array is at max capacity."""

        # print(f"Length: {self.length}", f"max capacity: {self.max_capacity}")
        if self.length > 0 and self.length == self.max_capacity:
            print("Array is at max capacity")
            return True
        else:
            return False


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

        print(f"The size of this static array is: {self.length}")


    def print_all_elements(self):
        """Print all elements of the array"""

        if self.array:
            print(f"Reading all elements from array")
            print("This is an O(n) time complexity operation, because the number of operations grows linearly with the size of the array.")
            for i in range(self.length):
                print(f"Element #{i+1} in the array: {self.array[i]}")
            print(f"There are {self.length} elements in the array. So {self.length} operations were made")
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
                self.length -= 1
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
                if self.length > 1:
                    for i in range(index + 1, self.length):
                        self.array[i - 1] = self.array[i]

                # Setting the element at the pointer to empty
                self.array[self.pointer] = -1
                # Reducing size, to indicate an element was removed. In turn, moving the pointer
                # to the new last element.
                self.length -= 1

                return popped_element
            else:
                print("No elements in the array to pop.")
        except IndexError:
            print("This index does not exist.")


    def append(self, element):
        """append an element to the end of an array, given there is an empty space."""

        # Check if there is a space in the array after the pointer, we can assume it's empty.
        if  not self.at_max_capacity() or self.length == 0:
            print(f"Appending {element} to the end of the array")
            print("""This is an O(1) time complexity operation, because the end of the array is always accessible 
            through the pointer, no matter the size of the array""")
            # Add element to empty space
            self.array[self.pointer + 1] = element
            # Increment size, in turn setting pointer to the new element.
            self.length += 1
        # If array is full
        # else:
        #     print("Array is at maximum capacity.")


    def insert(self, index, element):
        """Insert element at given index, given there is empty space."""

        try:
            # Check if array empty or index the same as pointer
            if  self.length == 0 or index == self.pointer:
                # Check if array is at max_capacity, if so, replace element at pointer
                if self.at_max_capacity():
                    self.array[self.pointer] = element
                # If index is the last index and array not at max_capacity append element
                else:
                    self.append(element)
                print(f"Inserting {element} to the end of the array")
                print("""This is an O(1) time complexity operation, because the end of the array is always accessible 
                            through the pointer, no matter the size of the array""")
                self.length += 1
            else:
                # Check if array is at max_capacity, if so, remove element at end of array to make room for new
                # one
                if self.at_max_capacity():
                    self.array[self.pointer] = -1
                    self.length -= 1
                # Shift all elements starting at given index to the right, to make space for new element.
                for i in range(self.pointer, index, -1):
                    self.array[i] = self.array[i - 1]
                # Assign element to given index
                print(f"Inserting {element} at index {index} of the array")
                print("""This is an O(n) time complexity operation, because at worst case we have to shift all 
                other elements, the amount of operations grows linearly with the array""")
                self.array[index] = element
                self.length += 1
        except IndexError:
            print("This index does not exist.")





