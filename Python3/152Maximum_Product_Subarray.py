#https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #1.dp[i] = max(num[i]*pre_max, nums[i]*pre_min, num[i])
        if not nums:
            return
        ans = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for x in nums[1:]:
            tmp_max = max(x*pre_max, x*pre_min,x)
            tmp_min = min(x*pre_max, x*pre_min,x)
            pre_max = tmp_max
            pre_min = tmp_min
            ans = max(ans, tmp_max)
        return ans
        '''
        #2.count sign numbers
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        print(nums)
        print(reverse_nums)
        return max(nums + reverse_nums)
        ''' 
