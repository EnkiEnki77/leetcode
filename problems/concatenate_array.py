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