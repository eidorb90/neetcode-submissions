class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            try:
                score += abs(ord(s[i+1]) - ord(s[i]))
                i += 1
            except:
                pass
        return score
