class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ''
        for i in range(min(len(word1), len(word2))):
            res = res + word1[i] + word2[i]
        if len(word1) > len(word2):
            for i in range(len(word2),len(word1)):
                res = res + word1[i]
        else:
            for i in range( len(word1),len(word2)):
                res = res + word2[i]

        return res
            
