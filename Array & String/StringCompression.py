class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        result = 0  # Pointer for where to write the compressed string
        
        while i < len(chars):
            letter = chars[i]
            count = 0
            
            # Count consecutive occurrences of the same character
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            
            # Write the character
            chars[result] = letter
            result += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[result] = digit
                    result += 1
        
        return result

#test case

chars = ["a", "a", "b", "b", "c", "c", "c"]
solution = Solution()
c_length = solution.compress(chars)
print(chars[:c_length])
