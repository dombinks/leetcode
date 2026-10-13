class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        if x > 0:
            rev = int(str(x)[::-1])
        elif x < 0:
            rev = -int(str(x)[-1:0:-1])

        return rev if rev <= (2**31 - 1) and rev >= -(2**31) else 0
