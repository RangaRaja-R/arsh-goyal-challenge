class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0
        while i<len(nums):
            if nums[i]!=0:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
            i+=1
