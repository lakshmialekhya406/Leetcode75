# Max number of k-sum pairs

# Example: nums = [1,2,3,4], k = 5
# result= 2

# Approach 
# we need to know the number of pairs which sum to k
# 1. sort the array
# 2. have 2 pointer two extream ends
# 3. update count if the two pointer value sum to k
# 4. if sum is less than k then update left pointer
# 5. else update right pointer perform this until the pointers cross them

def maxOperations(self, nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)
    l,r = 0,n-1
    nums.sort()
    while l<r:
        val = nums[l]+nums[r]
        if val == k:
            l += 1
            r -= 1
            count += 1
        elif val<k:
            l += 1
        else:
            r -= 1
    return count