class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while True:
            if i >= len(nums)-1:
                break
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
