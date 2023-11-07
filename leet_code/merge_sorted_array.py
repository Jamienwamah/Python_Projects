"""
You are given two integer arrays nums1 and nums2, 
sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

#Step by step way of solving the question
#1 Initialize two pointers. 
# P1 to track current position in the original 'nums1'(starting at an indec of 'm-1', 
# which is the last elements in the original nums1)
#p2 to also track the current position in the original 'nums2'(starting at an index of n-1,
# which is the last elements in nums2)
#2 Initialize a third pointer P to track the current position in the merged array, 
#starting with an index of m+n-1
#3 compare the nums1[p1] and nums2[p2] and select the larger of the two elements
#4 copy the selected elements to nums1[p1] and then decrement 'p' and the pointer corresponding to the selected element (either p1 or p2)
#5 Repeat steps 3 &4

#we first define a function and assign the different integer arrays with their various integers

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy any remaining elements from nums2 (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

            
    
