# Is Subsequence

# Example: s = "abc", t = "ahbgdc"
# result = true

# Approach:
# we need to find whether s is subsequence of t
# 1. have two iterators starting initially indicating the strings
# 2. move iterator of s if the value is present in t
# 3. if value of iterator comes to end this shows it is subsequence


def isSubsequence(self, s: str, t: str) -> bool:
    i,j = 0,0
    n,m = len(t), len(s)
    if m>n:
        return False
    while j<m and i<n:
        if t[i] == s[j]:
            j += 1
        i += 1
    return j == m