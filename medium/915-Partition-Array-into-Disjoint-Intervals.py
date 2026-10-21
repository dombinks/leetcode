class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        biggests = [0] * len(nums)
        biggest = 0

        for i in range(len(nums)):
            biggest = max(biggest, nums[i])
            biggests[i] = biggest

        smallest = 1000001
        index = 100000
        for i in range(len(nums)-1, -1, -1):
            smallest = min(smallest, nums[i])
            if smallest >= biggests[i-1]:
                index = i
                
        return max(index, 1)
