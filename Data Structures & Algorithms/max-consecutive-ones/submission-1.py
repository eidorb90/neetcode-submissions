class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > max_c:
                    max_c = count
            else:
                if count > max_c:
                    max_c = count
                count = 0
            
        return max_c