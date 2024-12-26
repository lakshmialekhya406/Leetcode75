 # Merge Strings Alternately

 # example: s1 = abcd, s2 = pqr
 # result = apbqcrd

 # psuedo:
 # 1. add alternatively both strings upto same length
 # 2. append the extra length of string to result 

 def mergeAlternately(self, word1: str, word2: str) -> str:
 	numberOfCommonCharsLength = len(word1) if len(word1) < len(word2) else len(word2)
    result = ""
    for i in range(numberOfCommonCharsLength):
        result += word1[i]
        result += word2[i]
    if len(word1) > len(word2):
        result += word1[numberOfCommonCharsLength: len(word1)]
    elif len(word2) > len(word1):
        result += word2[numberOfCommonCharsLength: len(word2)]
    return result