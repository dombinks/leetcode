class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        seen = {}
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        ns = sorted(list(seen.keys()))
        low = 0
        high = len(ns) - 1

        for low in range(0, len(ns)):
            for high in range(len(ns) - 1, low, -1): 
                x = ns[low]
                y = ns[high]
                z = -(x + y)

                validZ = z in seen
                zBetween = (z > ns[low]) and (z < ns[high])
                sameZHasDuplicate = (z == ns[low] or z == ns[high]) and seen[z] >= 2
    
                if validZ and (zBetween or sameZHasDuplicate):
                    out.append([x, y, z])

        if 0 in seen and seen[0] >= 3:
            out.append([0, 0, 0])

        return out
