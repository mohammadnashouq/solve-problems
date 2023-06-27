class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = ''
        for i,let in enumerate(s):
            if i < len(s) -1:
                if let ==" " and s[i+1] ==' ':
                    continue 
                else:
                   new_s += let
            else:
                new_s += let
        splited_string = new_s.strip().split(' ')
        res = ''
        if len(splited_string) == 1:
            return res+splited_string[0]
        if len(splited_string) == 0:
            return ''
        
        for i in range(len(splited_string)):
           
            res += splited_string[len(splited_string) - 1 - i].strip() + ' '
        res = res[:-1]
        return res
