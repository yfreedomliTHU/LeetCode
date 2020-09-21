#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        #link-list ->array O(N) space complexity
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
        '''
        # O(1)
        if not head or not head.next:
            return True
        # find the first half
        first_end = self.getFirstEnd(head)
        second_start = self.reverse(first_end.next)
        
        ans = True
        p1 = head
        p2 = second_start
        while ans and p2:
            if p1.val != p2.val:
                ans = False
            p1 = p1.next
            p2 = p2.next
        
        #reverse second half
        first_end.next = self.reverse(second_start)
        
        return ans
          
        
    def getFirstEnd(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        
        return pre
