class Solution(object):
    def mergeAlternately(self, str1, str2):
        merged_result = []
        max_length = max(len(str1), len(str2))
        
        for index in range(max_length):
            if index < len(str1):
                merged_result += str1[index]
            if index < len(str2):
                merged_result += str2[index]

        return "".join(merged_result)
        
# Example usage
solution = Solution()
print(solution.mergeAlternately("john", "snow"))    # Output: "jsonhonw"
print(solution.mergeAlternately("ab", "pqrs"))    # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))     # Output: "apbqcd"

