# String Compression

# Example: chars = ["a","a","b","b","c","c","c"]
# result = ["a","2","b","2","c","3"]

# Approach 
# 1. have 2 pointers at start store the character and count set 0 on each iteration
# 2. iterate the second pointer untill we find a different from present character
# 3. once this is done update chars array with first pointer

def compress(self, chars: List[str]) -> int:
    i,k = 0,0
    n = len(chars)
    while(i<len(chars)):
        present = chars[i]
        count = 0
        while((i < len(chars)) and (chars[i] == present)):
            count += 1
            i += 1
        chars[k] = present 
        k += 1
        if count > 1:
        	# this is to handle more than 2 digits
            for j in str(count):
                chars[k] = j
                k += 1
    return k