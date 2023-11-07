"""
Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
"""

#Steps to solve this problem:
#1 Initialize two pointers 'i' and 'k', represents the current position 
#in the array 'nums' and 'k' represents the numer of elements after 
#removing duplicates initially set to 0
#2 Iterate through the array 'nums' using the pointer 'i', starting from 
#the second element (index 1). For each element 'nums[i], do the following
#- compare 'nums[i] with the element at index 'k-2' if 'nums[i]' is greater
#than the element at 'k-2'. It is a new unique element. So we can keep it in the array,
#Update 'nums[k]' with the value of 'nums[i]' and increment both 'i' and 'k' 
#3 Continue this process until you reach the end of the array
#4 The value of 'k' will be the number of elements after removing duplicates. 
#5 Return 'k' 

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 0  # Initialize k to 0

        for i in range(len(nums)):
            if k < 2 or nums[i] > nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k  # Move the return statement here, outside of the for loop
