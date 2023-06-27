class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        res = ''
        len_str1 = len(str1)
        len_str2 = len(str2)
        
        if str1 == str2:
            return str1
        
        elif len_str1 < len_str2:
            if str1 not in str2:
                return ""
            
            else:
                temp = int(len_str1 * 2/2) + 1
                for i in range(temp):
                    match_str= ''                
                    if len_str2 % int(temp - i) == 0:
                        if len_str1 % int(temp - i) == 0:
                            div_num = len_str2 /  int(temp - i)
                            for j in range(div_num):
                                match_str += str1[:temp-i]
                            
                            if match_str == str2:
                                return str1[:temp-i]
                            else:
                                return ''
        elif str2 not in str1:
                return ""
        
        else:
            temp = int(len_str2 * 2 /2) + 1
            for i in range(temp):
                if len_str1 % int(temp - i) == 0:
                    if len_str2 % int(temp - i) == 0:
                        match_str= ''
                        div_num = len_str1 /  int(temp - i)
                        for j in range(div_num):
                            match_str += str2[:temp-i]
                        
                        if match_str == str1:
                            return str1[:temp-i]
            return ''
                    

    
