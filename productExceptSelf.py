class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionart = {}
        right_count = [0 for i in nums]
        left_count = [0 for i in nums]
        #print(right_count)
        right_count[0] = (1)
        left_count[len(nums) - 1] = (1)
        res =[]
        for i in range(len(nums)):
            if i>0:
                right_count[i] =right_count[i -1 ] * nums[i-1]
                left_count[len(nums) - i-1] = nums[len(nums) - i ] * left_count[len(nums) -i]

                
        for i in range(len(nums)):
            if i == 0:
                res.append(left_count[0])
            elif i ==  len(nums) - 1:
                res.append(right_count[len(nums) - 1])

            else:
                res.append(right_count[i] * left_count[i]) 
                
            
        return res
