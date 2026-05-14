# 23 合并K个升序链表

from tools import *
from typing import Optional, List
import heapq


# O(nlogk) O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        dummy_root = ListNode(None)
        node = dummy_root

        for k, l in enumerate(lists):
            if l:
                vals.append((l.val, k))
        heapq.heapify(vals)

        while vals:
            l, k = heapq.heappop(vals)
            curr_node_k = lists[k]
            node.next = curr_node_k
            lists[k] = curr_node_k.next
            node = node.next
            if lists[k]:
                heapq.heappush(vals, (lists[k].val, k))
        return dummy_root.next


# O(nlogk) O(logk)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        # 分：递归处理左右两半
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # 治：合并两个有序链表
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


# lists = [
#     [1, 3, 4, 6, 8, 9, 12],
#     [1, 2, 5, 7, 11, 21, 24],
#     [-4, 0, 4, 7, 10, 14, 22, 29],
# ]
lists = [[1], [0]]
lists = [list_to_link(l) for l in lists]

print(print_link(Solution().mergeKLists(lists)))
