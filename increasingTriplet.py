class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = -1
        j = -1
        k = -1
        study_case = []
        length = len(nums) 
        
        if length < 3:
            return False
        
        for l in range(len(nums)):
            if i == -1:
                i = l
                continue 
            elif nums[l] < nums[i]  :
                if j == -1:
                    i = l
                else:
                    study_case.append(l)
            
            elif nums[l] > nums[i] and j==-1:
                j = l

            elif nums[l] < nums[j] and nums[l] > nums[i]  and k==-1:
                j = l
            elif nums[l] > nums[j] :
                k = l
                break
        print("i,j,k",i,j,k)
        print("nums[i], nums[j] ,nums[k]",nums[i],nums[j],nums[k])
        
        if k > j and j > i and nums[k] > nums[j] and nums[j] > nums[i]:
            return True
        else:
           
            for case in study_case:
                i = case
                j = -1
                k = -1
                for l in range(i+1,len(nums)):
                    
                    if nums[l] < nums[i]  :
                        if j == -1:
                            i = l
                        else:
                            study_case.append(l)
                    
                    elif nums[l] > nums[i] and j==-1:
                        j = l

                    elif nums[l] < nums[j] and nums[l] > nums[i]  and k==-1:
                        j = l
                    elif nums[l] > nums[j] :
                        k = l
                        break
                print("i,j,k",i,j,k)
                print("nums[i], nums[j] ,nums[k]",nums[i],nums[j],nums[k])
                
                if k > j and j > i and nums[k] > nums[j] and nums[j] > nums[i]:
                    return True


        return False
