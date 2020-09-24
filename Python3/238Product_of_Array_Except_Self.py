#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        #L + R
        if not nums:
            return 0
        n = len(nums)
        L = [1]*n
        R = [1]*n
        ans = [0]*n
        for i in range(1, n):
            L[i]=L[i-1]*nums[i-1]
        for j in range(n-2, -1, -1):
            R[j]=R[j+1]*nums[j+1]
        
        for k in range(n):
            ans[k]=L[k]*R[k]
        
        return ans
        '''
        # O(1) space
        if not nums:
            return 0
        n = len(nums)
        ans = [1]*n
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        R = 1
        for j in range(n-1, -1, -1):
            ans[j] *= R
            R = R*nums[j]
            
        return ans
