#https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        # 1递归 Recursive method
        if not head or not head.next:
            return head
        node1 = head
        node2 = head.next
        
        node1.next = self.swapPairs(node2.next)
        node2.next = node1
        return node2
        '''
        # 2Iterative method
        ans = ListNode(0)
        ans.next = head
        tmp = ans
        
        while head and head.next:
            node1 = head
            node2 = head.next
            
            # swaping
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            head = node1.next
            #tmp = tmp.next.next # tmp move 2 pointer
            tmp = node1
        return ans.next
            
