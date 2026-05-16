# 142 环形链表Ⅱ
# Definition for singly-linked list.
from ctypes import pointer
from curses import noecho
from typing import Optional
from tools import *


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vocab = set()
        while head:
            if head in vocab:
                return head
            vocab.add(head)
            head = head.next
        return None


class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast:
            if fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return slow
        return None


head = [3, 2, 0, -4, 2]
head = list_to_link(head)
print(Solution().detectCycle(head))
