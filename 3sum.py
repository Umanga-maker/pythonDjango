def three_sum(nums):
    nums.sort() #step 1 : Sort the list to make it easier to avoid duplicates and use two - pointers
    result = []

    for i in range(len(nums)):
        #step 2 : loop through each number as the fixed number
        if i > 0 and nums[i] == nums[i-1]:
            continue # Skip duplicate elements for the fixed number
            
            #step3 : Initialize two pointers starting after 'i' and at the end
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right] # Calculate the sum of triplet

            if total == 0:
                #step 4 : Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates on the left side
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates on the right side
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers after storing the valid triplet
                left += 1
                right -= 1

            elif total < 0: # If the total is less than 0, move left pointer to get a bigger sum
                left += 1
            else: # If the total is more than 0, move right pointer to get a smaller sum
                right -= 1
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))                    