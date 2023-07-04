class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        current_char = chars[0]
        counts = 0
        length_chars = 0
        for i, char in enumerate(chars):
            print("----- char", char)
            if current_char == char:
                counts +=1 
            else:
                chars[length_chars] = current_char
                length_chars += 1
                    
                if counts > 1 and counts< 10:
                    print("chars: ",chars)
                    print("counts: ",counts)
                    print("length_chars: ",length_chars)
                    
                    chars[length_chars] = str(counts)
                    length_chars += 1
                elif counts >= 10:
                    for char_c in str(counts):
                        chars[length_chars] = str(char_c)
                        length_chars += 1
                counts = 1
                current_char = char
            if i == len(chars) - 1 :
                    chars[length_chars] = current_char
                    length_chars += 1
                    
                    if counts > 1 and counts< 10:
                        print("chars: ",chars)
                        print("counts: ",counts)
                        print("length_chars: ",length_chars)
                        
                        chars[length_chars] = str(counts)
                        length_chars += 1
                    elif counts >= 10:
                        for char_c in str(counts):
                            chars[length_chars] = str(char_c)
                            length_chars += 1
        return length_chars

                    
