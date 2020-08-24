#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        '''
        # python style:int->str->int
        if x >= 0:
            sign = 1
            str_x = str(x)
        else:
            sign = -1
            str_x = str(x)[1:]
        # reverse str
        x_re = (int(str_x[::-1])) * sign
        if x_re <= 2**31 -1 and x_re >= -2**31:
            return x_re
        else:
            return 0
        '''
        # divide 10 to get number
        x_re = 0
        tmp_x = abs(x)
        while tmp_x:
            x_re = x_re * 10 + tmp_x % 10
            tmp_x //= 10
        result = x_re if x>0 else -1*x_re
        return result if x_re <= 2**31 -1 and x_re >= -2**31 else 0
