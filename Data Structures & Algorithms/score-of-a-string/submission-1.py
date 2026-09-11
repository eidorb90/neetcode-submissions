class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            if i + 1 < len(s):
                score += abs(ord(s[i+1]) - ord(s[i]))
                i += 1
        return score
