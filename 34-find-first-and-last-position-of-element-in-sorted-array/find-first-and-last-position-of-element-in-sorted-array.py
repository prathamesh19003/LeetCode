class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstpos=-1
        lastpos=-1
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                if firstpos==-1:
                    firstpos=i
                    lastpos=i
                elif i>lastpos:
                    lastpos=i
        res.append(firstpos)
        res.append(lastpos)
        return res