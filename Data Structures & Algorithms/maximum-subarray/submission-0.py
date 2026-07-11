class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] # init array
        currSum = 0 #init sum
        for i in nums:
            if currSum < 0: # if curr sum less than 0 reset to 0
                currSum = 0
            currSum += i
            maxSub = max(maxSub, currSum)
        return maxSub
