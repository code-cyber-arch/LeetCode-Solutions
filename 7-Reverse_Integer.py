class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        x = abs(x)
        reversed_int = int(str(x)[::-1])
        if is_negative:
            reversed_int *= -1
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int
