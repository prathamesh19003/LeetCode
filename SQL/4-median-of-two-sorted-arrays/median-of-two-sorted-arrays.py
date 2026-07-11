class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        i = j = 0
        res = []

        while i < n and j < m:
            if nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                i += 1

        while i < n:
            res.append(nums1[i])
            i += 1

        while j < m:
            res.append(nums2[j])
            j += 1

        k = len(res)

        if k % 2 == 1:
            return res[k // 2]

        return (res[k // 2 - 1] + res[k // 2]) / 2