class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found = 0
        if s == "":
            return True

        for i in range(len(t)):
            if s[found] == t[i]:
                found += 1

            if found == len(s):
                return True
        return False
        