class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        mins = sorted([int(t[0]) * 60 + int(t[1]) for t in [t.split(':') for t in timePoints]])
        m = 1440

        for i in range(len(mins) - 1):
            m = min(m, mins[i+1] - mins[i])

        m = min(m, (1440 - mins[len(mins)-1]) + mins[0])

        return m
