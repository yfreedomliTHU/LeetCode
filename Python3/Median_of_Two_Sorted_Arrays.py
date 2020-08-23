#https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lens = len(nums1) + len(nums2)
        if lens % 2 == 1:
            return self.findknum(nums1, nums2, lens//2)
        else:
            return (self.findknum(nums1, nums2, lens//2-1) + self.findknum(nums1, nums2, lens//2)) / 2.0
        
    def findknum(self, nums1, nums2, k):
        if not nums1: return nums2[k]
        if not nums2: return nums1[k]
        
        idx1, idx2 = len(nums1) //2, len(nums2) // 2
        mid1, mid2 = nums1[idx1], nums2[idx2]
        
        if idx1+idx2 <k:
            if mid1 > mid2:
                return self.findknum(nums1, nums2[idx2+1:], k-idx2-1)
            else:
                return self.findknum(nums1[idx1+1:], nums2, k-idx1-1)
        else:
            if mid1 > mid2:
                return self.findknum(nums1[:idx1], nums2, k)
            else:
                return self.findknum(nums1, nums2[:idx2], k)
