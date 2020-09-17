#https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #归并算法
        h, length, intv = head, 0, 1
        while h:
            h = h.next
            length += 1
        ans = ListNode(0)
        ans.next = head
        while intv < length:
            pre, h = ans, ans.next
            while h:
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i-1
                if i: break #h2 is None
                h2, i = h, intv
                while i and h: h, i = h.next, i-1
                len1, len2 = intv, intv-i
                #merge
                while len1 and len2:
                    if h1.val < h2.val:
                        pre.next , h1, len1 = h1, h1.next, len1-1
                    else:
                        pre.next , h2, len2 = h2, h2.next, len2-1
                    pre = pre.next
                pre.next = h1 if len1 else h2
                while len1>0 or len2>0:
                    pre , len1, len2= pre.next, len1-1, len2-1
                pre.next = h
            intv *= 2
        return ans.next
