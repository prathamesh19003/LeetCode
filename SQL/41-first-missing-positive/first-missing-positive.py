class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        for i in range(len(nums)):
            if nums[i]==count:
                count+=1
        return count