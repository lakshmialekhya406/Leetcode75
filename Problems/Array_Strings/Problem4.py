# Can place flowers

# example: flowerbed = [1,0,0,0,1], n = 1
# result = true

# psuedo:
# 1. if n == 0 return True as no need to plant
# 2. if length of flower bed is 1 and is empty return True
# 3. iterate whole flowerbed, check adjacent if we are able to place plant update value to 1 and decremnt n
# 4. return True if n<=0, that means we planted our plants

def canPlaceFlowers(self, flowerbed, n):
    if n == 0:
        return True
    len_flowerbed = len(flowerbed)
    if len_flowerbed == 1:
        return flowerbed[0] == 0
    for i in range(len_flowerbed):
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i == len_flowerbed-1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            n -= 1
            flowerbed[i] = 1
    return n<=0
