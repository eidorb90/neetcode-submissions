class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        score = 0
        for char in s:
            if i + 1 < len(s):
                score += abs(ord(s[i+1]) - ord(char))
                i += 1
        return score
