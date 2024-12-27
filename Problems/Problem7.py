# Product of array except self

# Example: nums = [1,2,3,4]
# result = [24,12,8,6]

# Approach 1: 
# 1. store product from left 
# 2. store product from right
# 3. value at index is left[index-1] * right[index+1]

def productExceptSelf(self, nums):
    leftArr, rightArr, res = [], [], []
    n = len(nums)
    val = nums[0]
    leftArr.append(val)
    for i in range(1, n):
        val *= nums[i]
        leftArr.append(val)
    val = nums[-1]
    rightArr.append(val)
    for i in range(n-2,-1,-1):
        val *= nums[i]
        rightArr.append(val)
    rightArr = rightArr[::-1]
    for i in range(n):
        val = 1
        if i-1>=0:
            val *= leftArr[i-1]
        if i+1<n:
            val *= rightArr[i+1]
        res.append(val)
    return res

# Approach 2:
# with no extra space
# 1. store product from left in result arr
# 2. have suffix with 1 and update the result arr from right with multiplying suffix
# 3. now update product value for suffix

def productExceptSelf(self, nums):
    res = []
    n = len(nums)
    val = 1
    res.append(val)
    for i in range(0, n-1):
        val *= nums[i]
        res.append(val)
    val = 1
    for i in range(n-1,-1,-1):
        res[i] = res[i] * val
        val *= nums[i]
    return res