# Increasing Triplet Subsequence

# Example: nums = [2,1,5,0,4,6]
# output = True

# Approach:
# 1. as per question we need a subsequence of i<j<k
# 2. so this mean we need a value with 2 min values 
# 3. find the min1 until we get the first min, if it fails assign it to next min if this also fails then we got the solution
# 4. if we did not get min2 that mean it is not possible

def increasingTriplet(self, nums: List[int]) -> bool:
    min1, min2 = float('inf'), float('inf')
    for i in nums:
        if i <= min1:
            min1 = i
        elif i<= min2:
            min2 = i
        else: 
            # if there are min1 and min2 the next value coming will be min3 which satisfies our condition so we return true
            return True
    return False