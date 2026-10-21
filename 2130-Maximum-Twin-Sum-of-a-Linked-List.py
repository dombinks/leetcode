# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        values = []
        node = head

        while node:
            values.append(node.val)
            node = node.next

        l = len(values)
        mid = l // 2
        out = 0 

        for i in range(0, mid):
            out = max(out, values[i] + values[l - i - 1])

        return out
