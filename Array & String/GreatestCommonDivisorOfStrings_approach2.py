from math import gcd
class Solution:
    def gcdOfStrings(self, str1, str2) :
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        return str1[:gcd(len(str1), len(str2))]
        return ""
        
# Test case 1
solution = Solution()
str1 = "ABCABCABC"
str2 = "ABCABC"

print(f"Input: str1 = '{str1}', str2 = '{str2}'")
print(f"Output: '{solution.gcdOfStrings(str1, str2)}'")