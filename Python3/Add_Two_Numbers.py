#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        elif l2 == None: return l1

        sum_ = l1.val + l2.val
        res = ListNode(sum_ % 10)
        res.next = self.addTwoNumbers(l1.next, l2.next)
        carry = sum_ // 10
        if carry: 
            res.next = self.addTwoNumbers(res.next, ListNode(carry))
        return res
