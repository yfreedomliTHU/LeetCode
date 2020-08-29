#https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        # Violent solution
        if not lists: return None
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        ans = ListNode(0)
        tmp = ans
        for x in vals:
            tmp.next = ListNode(x)
            tmp = tmp.next
        return ans.next
        '''
        if not lists: return None
        import heapq as hq
        queue = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for l in lists:
            while l:
                hq.heappush(queue, l.val)
                l = l.next
        ans = ListNode(0)
        tmp = ans
        while queue:
            tmp.next = ListNode(hq.heappop(queue))
            tmp = tmp.next
        return ans.next
        
