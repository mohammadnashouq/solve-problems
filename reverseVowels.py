class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        new_res = ''
        saved_voles = []
        voels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        for i in range(len(s)):
            if s[i] in voels:
                saved_voles.append(s[i])
        
        for i in range(len(s)):
            if s[i] in voels:
                new_res += saved_voles[-1]
                del saved_voles[-1]
                
            else:
                new_res += s[i]
        return new_res
