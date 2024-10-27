class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0  # Initialize indices
        
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1  # Increment i
            
            if j < len(word2):
                result.append(word2[j])
                j += 1  # Increment j
        
        return ''.join(result)  # Join the list into a string

# Example usage
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))    # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))    # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))     # Output: "apbqcd"

''' Time Complexity : O(n+m);
    Space Complexity: O(n+m);'''