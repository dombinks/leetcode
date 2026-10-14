class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        out = "9" * (sum // 9)
        left = sum % 9
        if left != 0:
            out += str(left)

        if len(out) > num:
            return ""

        else:
            return out + ("0" * (num - len(out)))
