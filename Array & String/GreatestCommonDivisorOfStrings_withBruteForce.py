class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)

        def is_valid_divisor (k):
            if len1 % k !=0 or len2 % k !=0:
                return False
            repeat_count1 = len1//k 
            repeat_count2 = len2//k
            base = str1[:k]
            return str1 == repeat_count1*base and str2 == repeat_count2*base
            
        # Iterate from the largest possible divisor down to 1
        for i in range (min(len1,len2),0,-1):
            if is_valid_divisor(i):
                return str1[:i]
        
        return ""
        
# Test case 1
solution = Solution()
str1 = "ABABAB"
str2 = "ABAB"

print(f"Input: str1 = '{str1}', str2 = '{str2}'")
print(f"Output: '{solution.gcdOfStrings(str1, str2)}'")