# Greatest Common divisor of strings

# example: s1 = abcabcabc s2 = abc
# result = abc

# psuedo:
# 1. check whether adding both strings viceversa are same
# 2. if yes find the gcd between length of both strings
# 3. if no return empty string

def gcdOfStrings(self, str1, str2):
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b) 
    if str1+str2 == str2+str1:
        a = len(str1)
        b = len(str2)
        val = gcd(a,b)
        return str2[:val]
    else: 
        return ""