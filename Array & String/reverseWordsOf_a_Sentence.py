class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = []
        for i in range(len(words)-1,-1,-1):
            result.append(words[i])
            
            if i!=0:
                result.append (" ")
        return "".join(result)
        
        
#test case 
solution = Solution()
s= "I love Bangladesh"
print(solution.reverseWords(s))

#expected Output: Bangladesh love I