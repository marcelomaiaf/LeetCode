# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        mapper_a = {}

        cur_a = headA
        cur_b = headB
        mapper_a[cur_a] = cur_a.val
        while cur_a.next:
            cur_a = cur_a.next
            mapper_a[cur_a] = cur_a.val

        while cur_b:
            if cur_b in mapper_a:
                return cur_b
            cur_b = cur_b.next

        # O(n+m) time
