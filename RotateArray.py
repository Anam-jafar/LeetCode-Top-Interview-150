class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotate_point = (len(nums)-k) % len(nums)
        nums[:] = nums[rotate_point:] + nums[:rotate_point]
