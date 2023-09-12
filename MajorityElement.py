class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        i = 0
        count = 1
        while True:
            if i >= len(nums)-1:
                break
            if nums[i] == nums[i+1]:
                count += 1
                if (count > len(nums)//2):
                    return nums[i]
            else:
                count = 1
            i += 1
        return nums[0]
