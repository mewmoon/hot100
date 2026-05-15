# 2 两数相加
from tools import *
from typing import Optional, List


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = dummy
        carry = 0

        while l1 or l2 or carry:
            if not l1 and not carry:
                node.next = l2
            if not l2 and not carry:
                node.next = l1

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            num = val1 + val2 + carry
            carry = num // 10
            node.next = ListNode(num % 10)

            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


l1 = [2, 4, 3]
l2 = [5, 6, 9]
result = Solution().addTwoNumbers(list_to_link(l1), list_to_link(l2))
print_link(result)
