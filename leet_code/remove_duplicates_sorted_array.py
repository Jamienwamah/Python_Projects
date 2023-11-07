"""
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. 
    Then return the number of unique elements in nums.
    Consider the number of unique elements of nums to be k, 
    to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums 
    contain the unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""

#Steps to solve this are:
#1 Initialize two pointers 'i' and 'k', where 'i' represents the current position in the array 'nums', 
# and 'k' represents the number of unique elements found so far. 
#initially set 'k' to 1 (assuming the first element is always unique)
#2 Iterate through the integer arrays 'nums' starting fromt the second element (index 1) 
# using the pointer 'i' and for each elements 'nums[i], do the following
# - compare 'nums[i]' with the element at index 'i - 1' (the previous element)
# - if 'nums[i] is different from the previoud element, it is a unque element. 
# Update 'nums[k]' with the value of 'nums[i]. Increment both 'i' and 'k'
#3 Continue this process until you reach the end of the array
#4 The value of k will be the number of unique elements in 'nums'
#5 Return k

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:  # Handle the empty array case
            return 0
        
        k = 1  # Initializing k to 1 since the first element is always unique

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Comparing nums[i] with the element at index i - 1
                nums[k] = nums[i]  # Updating nums[k] with the value of nums[i]
                k += 1  # Incrementing k by 1

        return k

        
        