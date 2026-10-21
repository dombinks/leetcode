class Solution:
    def rob(self, nums: list[int]) -> int:
        amount = [0] * (len(nums)+1)
        amount[1] = nums[0]

        for i in range(1, len(nums)):
            amount[i+1] = max(amount[i], amount[i-1] + nums[i])

        print(amount)
        return amount[len(nums)]
