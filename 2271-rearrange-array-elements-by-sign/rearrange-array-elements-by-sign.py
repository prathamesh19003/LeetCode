class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        res=[0]*n
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(n//2):
            res[i*2]=pos[i]
            res[i*2+1]=neg[i]
        return res