class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)
        bool_res = []
        number_of_kids = len(candies)
        for i in range(number_of_kids):
            if extraCandies + candies[i] >= max_num:
                bool_res.append(True)
            else:
                bool_res.append(False)

        return bool_res
