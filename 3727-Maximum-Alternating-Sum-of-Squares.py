class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [n * n for n in nums]
        squares.sort()
        return sum(squares[(len(squares)//2):]) - sum(squares[0:(len(squares)//2)])
