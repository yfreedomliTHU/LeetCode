#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        #1.hashmap
        if not nums:
            return
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1        
        for x in hashmap:
            if hashmap[x] > len(nums) /2:
                return x
        '''
        '''
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        '''
        #2.vote
        count = 0
        candidate = None
        for x in nums:
            if count == 0:
                candidate = x
            count += (1 if x == candidate else -1)
            
        return candidate
