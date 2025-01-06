# Move Zeros

# Example: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Approach
# we need to move all zeroes to right
# 1. keep two pointers initially and keep on moving one to right
# 2. if we find a non zero value then swap and increase the left pointer to next value

def moveZeroes(self, nums: List[int]) -> None:
    i,r = 0,0
    while(i<len(nums)):
        if nums[i]:
            # swap
            nums[i], nums[r] = nums[r], nums[i]
            r += 1
        i += 1