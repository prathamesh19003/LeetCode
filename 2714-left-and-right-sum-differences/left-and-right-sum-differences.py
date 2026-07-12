class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result=[]
        rightSum=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            rightSum-=nums[i]
            result.append(abs(leftSum-rightSum))
            leftSum+=nums[i]
        return result