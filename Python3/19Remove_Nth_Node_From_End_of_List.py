#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        # count head
        lenth = 0
        tmp = head
        while tmp:
            lenth += 1
            tmp = tmp.next
        
        lenth = lenth-n+1
        # re_search the delete node
        tmp = head
        pos = 1
        if pos == lenth:
            return head.next
        while pos < lenth-1:
            tmp = tmp.next
            pos += 1
        
        tmp.next = tmp.next.next # delete node
        return head
        '''
        # double pointer
        tmp = ListNode(0)
        tmp.next = head
        p1, p2 = tmp, head
        for i in range(n):
            p2 = p2.next
        while p2:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next # remove 操作 
        return tmp.next
