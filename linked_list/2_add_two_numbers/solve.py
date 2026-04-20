# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0
        
        def rec(l1,l2, carry, res):
            if not l1 and not l2:
                if carry:
                    res.val = carry
                    res.next = None
                    return res
                else:
                    return

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            _sum = v1 + v2 + carry
            carry, val = _sum // 10 , _sum % 10

            res.val = val
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res.next = rec(l1, l2, carry, ListNode())
            
            return res

        rec(l1,l2,carry, res)
        return res