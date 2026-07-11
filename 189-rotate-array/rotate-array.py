class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        rotated=[0]*n
        for i in range(len(nums)):
            rotated[(i+k)%n]=nums[i]
        
        for j in range(len(nums)):
            nums[j]=rotated[j]

        