# Reverse words in a string

# example: s = "the sky is blue"
# result: "blue is sky the"

# Approach 1
# psuedo:
# 1.split the string 
# 2.reverse the list
# 3.join the list 

def reverseWords(self, s):
    listOfValues = s.split()
    return " ".join(listOfValues[::-1])

# Approach 2
# psuedo:
# two pointer method
# 1. reverse the string
# 2. make string as list
# 3. start pointers left and right from 0
# 4. keep on increasing until u get empty
# 5. now reverse from left to right and add space
# 6. assign left as right
# 7. repeat the process until it reaches the end
# 8. join the list and remove extra chars and remove extra spaces

def reverseWords(self, s):
    # remove trailing and leading spaces
    s = s.strip()[::-1]
    n = len(s)
    finalLen = 0
    s = list(s)
    i,l,r = 0,0,0
    while i<n:
        if i==n: break
        while i<n and s[i] != " ":
            s[r] = s[i]
            r +=1
            i +=1
        if l<r:
            s[l:r] = s[l:r][::-1]
            print(len(s[l:r]))
            finalLen += len(s[l:r]) + 1
            if r == n: break
            s[r] = " "
            r += 1
            l = r
        i += 1
    # join, remove trailing and leading spaces
    return "".join(s)[0:finalLen].strip()
