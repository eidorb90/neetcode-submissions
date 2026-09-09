class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        for i in range(len(binary)):
            if binary[i] == "1":
                count += 1
        return count
        
