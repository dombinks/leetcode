class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def place(node: Node, val: int, closest: int) -> int:
        if val < node.val:
            if node.left:
                return Node.place(node.left, val, closest if abs(val - node.val) > abs(val - closest) else node.val)
            else:
                node.left = Node(val)
                return min(abs(val - node.val), abs(val - closest))
        elif val > node.val:
            if node.right:
                return Node.place(node.right, val, closest if abs(val - node.val) > abs(val - closest) else node.val)
            else:
                node.right = Node(val)
                return min(abs(val - node.val), abs(val - closest))
            
class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        def toMins(val: str) -> int:
            hm = val.split(':')
            return int(hm[0]) * 60 + int(hm[1])

        s = toMins(timePoints[0])
        seen = set()
        seen.add(s)
        t = Node(s)
        m = 1440
        mn = s
        mx = s

        for i in range(1, len(timePoints)):
            p = toMins(timePoints[i])

            if p in seen:
                return 0
            else:
                seen.add(p)

            mn = min(mn, p)
            mx = max(mx, p)

            m = min(m, Node.place(t, p, s))
            m = min(m, mn + (1440 - mx))

        return m
