class Solution(object):
    def mergeAlternately(self, word1, word2):
    
        result = []
        for i in range(len(word1)):
            result.append(word1[i])
            try:
                result.append(word2[i])
            except:
                continue
        if len(word2) > len(word1):
            result.append(word2[len(word1):])
        return "".join(result)

# Example usage
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))    # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))    # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))     # Output: "apbqcd"

