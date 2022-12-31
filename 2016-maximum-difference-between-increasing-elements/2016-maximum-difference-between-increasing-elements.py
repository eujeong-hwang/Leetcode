class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_difference = 0
        min_num = float('inf')

        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
            elif nums[i] - min_num > max_difference:
                max_difference = nums[i] - min_num

        if max_difference == 0:
            return -1
        else:
            return max_difference