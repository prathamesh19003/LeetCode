class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum=sum(nums)
        leftSum=0

        for i in range(len(nums)):
            rightSum-=nums[i]
            if rightSum==leftSum:
                return i
            leftSum+=nums[i]
        return -1