# Container with most water

# Example: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Approach 
# we need to calculate the area which is maximum
# 1. have 2 pointers left and right to extream ends
# 2. calculate area as min(heights of left and right) * (right-left)
# 3. store area compare always with the areas 
# 4. move the pointer on min height until they both cross them

def maxArea(self, height: List[int]) -> int:
    n = len(height)
    l = 0
    r = n-1
    result = -1
    while(l<r):
        w = r-l
        h = min(height[r],height[l])
        result = max(result,w*h)
        if height[r]<height[l]:
            r -= 1
        else:
            l += 1
    return result