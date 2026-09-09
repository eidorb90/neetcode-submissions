class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}
        t_char = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            if sc not in s_char:
                s_char[sc] = 0
            else:
                s_char[sc] += 1
            
            if tc not in t_char:
                t_char[tc] = 0
            else:
                t_char[tc] += 1


        for sc in s_char:
            sc_num = s_char[sc]

            if t_char.get(sc) != sc_num:

                    return False    

        return True


            
