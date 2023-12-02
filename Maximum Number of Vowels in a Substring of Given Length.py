class Solution(object):
    def number_of_vowles(self,s):
        #print("number_of_vowles",s)
        vouels = ['a', 'e', 'i', 'o', 'u']
        res = 0
        for i in range(len(s)):
            
            if s[i] in  vouels:
                #print("s[i]",s[i])
                res += 1
        return res
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vouels = ['a', 'e', 'i', 'o', 'u']
        if k > len(s):
            return 0
        
        res =self.number_of_vowles(s[0:k])
        max_res = res
        i = k -1
        j = 0
        while i< len(s):
            #print("res",res)
            #print("array",s[j:i+1])
            if s[j] not in vouels:
                if i < len(s) - 1:
                    if s[i+1]  in  vouels:
                        res +=1
                        if res> max_res:
                            max_res = res
                    else:
                        pass
            else:
                if i < len(s) - 1:
                    if s[i+1] not in vouels:
                        res -= 1
            
            j += 1
            i += 1
           

        return max_res
