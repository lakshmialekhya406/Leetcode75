# Reverse vowels of a string

# example: s = "IceCreAm"
# result: "AceCreIm"

# Approach 1
# psuedo:
# 1. store all vowels in array
# 2. iterate string if vowel found assign value from vowels in reverse manner

def reverseVowels(self, s):
    def isVowel(a):
        vowels = ['a','e','i','o','u']
        return a.lower() in vowels
    vowels = []
    for i in s:
        if isVowel(i):
            vowels.append(i)
    result = ""
    ind = len(vowels) - 1
    for i in s:
        if isVowel(i):
            result += vowels[ind]
            ind -= 1
        else: 
            result += i
    return result

# Approach 2
# psuedo:
# 1. iterate with 2 pointers one from left and other from right
# 2. if both left and right find vowels swap them
# 3. always check left<right

def reverseVowels(self, s):
    def isVowel(a):
        vowels = ['a','e','i','o','u']
        return a.lower() in vowels
    s = list(s)
    l = 0
    r = len(s)-1 
    while l<r:
        if isVowel(s[l]) == False:
            l+=1
        if isVowel(s[r]) == False:
            r-=1
        if isVowel(s[l]) and isVowel(s[r]):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
    return "".join(s)