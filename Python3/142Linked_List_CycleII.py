#https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getMeet(self, head):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        return None
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        #1.hash
        if head == None:
            return None
        visited = {}
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited[node] = node
                node = node.next
        '''
        #2.Floyd
        meet = self.getMeet(head)
        if meet == None:
            return None
        p1 = head
        p2 = meet
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
