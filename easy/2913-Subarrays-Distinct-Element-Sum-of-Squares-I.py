class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        out = 0

        for i in range(0, len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                seen.add(nums[j])
                l = len(seen)
                out += (l * l)

        return out
