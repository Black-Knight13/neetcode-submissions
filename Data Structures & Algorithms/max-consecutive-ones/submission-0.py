class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        global_sum = 0
        local_sum = 0
        for i in nums:
            if i == 1:
                local_sum += 1 
            else:
                local_sum = 0
            global_sum = max(global_sum, local_sum)
        return global_sum
        