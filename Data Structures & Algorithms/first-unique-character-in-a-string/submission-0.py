class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_chars = {}
        for char in s:
            if char not in seen_chars:
                seen_chars[char] = 0
            else:
                seen_chars[char] += 1
        for index, char in enumerate(s):
            if seen_chars[char] == 0:
                return index
        return -1
        
