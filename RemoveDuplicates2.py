class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        count = 1
        while True:
            if i >= len(nums)-1:
                break
            if nums[i] == nums[i+1]:
                count += 1
                if (count > 2):
                    nums.pop(i)
                    continue
            else:
                count = 1
            i += 1

        return len(nums)
