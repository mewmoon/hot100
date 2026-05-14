# 21 合并两个有序链表
from tools import *
from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_root = ListNode(None)
        node = dummy_root
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 if list1 else list2
        return dummy_root.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
l1 = list_to_link(l1)
l2 = list_to_link(l2)
print(Solution().mergeTwoLists(l1, l2))
