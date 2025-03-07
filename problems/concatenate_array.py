def concatenate_array(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Takes an array of integers and returns a new array of two copies of the input array.
    """

    # Copies input array
    ans = nums[:]
    # Concatenates ans with another copy
    ans += nums[:]

    return ans

def concatenate_array_2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Takes an array of integers and returns a new array of two copies of the input array.
    """

    ans = nums * 2

    return ans

def concatenate_array_3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Takes an array of integers and returns a new array of two copies of the input array.
    """

    # Copies input arra
    nums.extend(nums)
    return nums


print(concatenate_array_3([1,2,1]))