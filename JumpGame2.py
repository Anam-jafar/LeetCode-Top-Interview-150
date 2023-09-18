class Solution(object):
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1]
