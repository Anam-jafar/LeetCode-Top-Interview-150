from functools import reduce
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        ans = [0] * n

        left_product = right_product = 1

        # Compute left products
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]

        # Compute right products
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]

        # Calculate the product except self
        for i in range(n):
            ans[i] = left_products[i] * right_products[i]

        return ans
