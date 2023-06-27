class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = 0
        j =0 
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
        for i in range(len(flowerbed)):
            if i+j+1 < len(flowerbed):
                if flowerbed[i+j] == 0:
                    if i ==0 and flowerbed[i+j + 1] ==0 and flowerbed[i+j] ==0:
                        res += 1
                        j += 1
                    
                    elif (flowerbed[i+j- 1] ==0 and flowerbed[i+j + 1] ==0):
                        res += 1
                        j += 1
            elif (i+j ==len(flowerbed) -1 and  flowerbed[i+j] ==0 and flowerbed[i+j -1] ==0):
                        res += 1
                        j += 1
        if res >= n:
            return True
        return False
