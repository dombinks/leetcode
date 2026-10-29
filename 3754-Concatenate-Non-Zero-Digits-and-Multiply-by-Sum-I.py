class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''.join([c for c in str(n) if c != '0'])
        x = x if x else "0"
        return int(x) * sum(map(int, x))
