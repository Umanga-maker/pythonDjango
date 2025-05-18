from typing import List

def twoSumRecursive(nums: List[int], target:int,start:int=0) -> List[int]:
    if start >= len(nums):
        return[]# Base case: if start index goes out of bounds, no pair found
    for i in range(start + 1,len(nums)):# Loop through all elements after 'start'
        if nums[start] + nums[i] == target:
            return [start, i]# Found the pair
        return twoSumRecursive(nums, target, start + 1)#recur for the next element
    
nums = [3,2,4]
target = 6

print(twoSumRecursive(nums, target))