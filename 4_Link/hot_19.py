# 19 删除链表的倒数第n个结点

from tools import *
from typing import Optional


# O(L) O(L)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        def dfs(node, parent):
            if not node:
                return 0
            idx = dfs(node.next, node) + 1
            if idx == n:
                parent.next = node.next
            return idx

        dummy = ListNode(None)
        dummy.next = head
        dfs(head, dummy)
        return dummy.next


# O(L) O(1) 快慢指针
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


head = [1, 2, 3, 4, 5]
root = list_to_link(head)
print_link(Solution().removeNthFromEnd(root, 2))
