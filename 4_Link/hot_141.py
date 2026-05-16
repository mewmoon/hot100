# 141 环形链表
from tools import *
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vocab = set()
        while head:
            if head in vocab:
                return True
            vocab.add(head)
            head = head.next
        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
