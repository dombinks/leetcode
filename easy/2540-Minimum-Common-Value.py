class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        a = 0
        b = 0

        while a < len(nums1) and b < len(nums2):
            while a < len(nums1) and nums1[a] < nums2[b]:
                a += 1
            if a == len(nums1):
                return -1

            while b < len(nums2) and nums2[b] < nums1[a]:
                b += 1
            if b == len(nums2):
                return -1

            if nums1[a] == nums2[b]:
                return nums1[a]
