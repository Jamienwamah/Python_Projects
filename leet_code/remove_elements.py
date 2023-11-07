""""
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place.
    The order of the elements may be changed.
    Then return the number of elements in nums which are not equal to val.
    Consider the number of elements in nums which are not equal to val be k, 
    to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the elements 
    which are not equal to val. The remaining elements of nums are not important as well as 
    the size of nums.
    Return k.
"""

#The steps to solve it are:
#1 Initialize two pointers 'i' and 'k',
#where 'i' represents the current position in the array 'nums'
#and 'k' represents the number of elements not equal to 'val' found so far
#initially setting 'k' to 0
#2 iterate through the array 'nums' with the pointer 'i'
# and for each element 'nums[i]', do the following
#-if'nums[i]' is equal to 'val', continue to the next element (skip it)
#- if 'num[i]' is not equal to 'val', update 'nums[k]' 
#increment both i and k
#3 Continue the process until you reach the end of the array
#4 The value of k will be the number of elements in 'nums' 
#that are not equal to 'val' 
#return k

class solution(object):
    def removeElement(self, nums, val):
        #initializing i and k
        i = 0
        k = 0
        #iterating through the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] #this updates the nums[k]
                k += 1
                
            return k
                