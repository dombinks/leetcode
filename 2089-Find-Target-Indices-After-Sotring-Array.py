class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        below = 0
        targets = 0 
        for n in nums:
            if n < target:
                below += 1
            if n == target:
                targets += 1

        return [i for i in range(below, below + targets)]
