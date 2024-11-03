class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = float('inf')
        min2 = float('inf')
        
        for n in nums:
            if n <= min1:
                min1 = n 
            elif n<= min2:
                min2 = n
            else:
                return True
        return False
        
#test case 
solution = Solution()
nums =[3,4,1,5,6]
print(solution.increasingTriplet(nums))
         
        