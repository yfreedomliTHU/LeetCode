#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        # int -> str
        x = str(x)
        return x == x[::-1]
        '''
        # without int -> str
        if x < 0: return False
        tmp_x = x
        x_re = 0
        while tmp_x:
            x_re = x_re *10 + tmp_x % 10
            tmp_x //= 10
        return x == x_re        
