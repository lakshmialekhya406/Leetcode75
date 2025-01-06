# Kids with greatest number of candies

# example: candies = [2,3,5,1,3], extraCandies = 3
# result = [true,true,true,false,true] 

# psuedo:
# 1.find the max element
# 2. add extraCandies for each element 
# 3. append the result of checking the max element found from step 1

def kidsWithCandies(self, candies, extraCandies):
    result = []
    maxElement = max(candies)
    for i in candies:
        result.append(i+extraCandies >= maxElement)
    return result