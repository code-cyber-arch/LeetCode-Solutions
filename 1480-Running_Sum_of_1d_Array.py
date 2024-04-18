class Solution(object):
    def runningSum(self, nums):
        sum1 = [] * len(nums)
        sum1.append(nums[0])
        for i in range(1, len(nums)):
            sum1.append(sum1[i-1] + nums[i])
        
        return sum1
