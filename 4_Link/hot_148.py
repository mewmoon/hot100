# 148 排序链表

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortFunc(head, tail):
            if head is None:
                return head
            if head.next == tail:
                head.next = None
                return head
            fast = slow = head
            while fast != tail:
                fast = fast.next
                slow = slow.next
                if fast != tail:
                    fast = fast.next

            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(p, q):
            head = ListNode()
            node = head
            i, j = p, q
            while i and j:
                if i.val < j.val:
                    node.next = i
                    i = i.next
                else:
                    node.next = j
                    j = j.next
                node = node.next
            node.next = i if i else j
            return head.next

        return sortFunc(head, None)


def printHead(head):
    if head is None:
        print("\n=======")
        return
    print(head.val, end=" -> ")
    printHead(head.next)


nums = [-1, 5, 9, -4, 0]
# nums = [4, 2, 1, 3]
head = ListNode()
node = head
for num in nums:
    node.next = ListNode(num)
    node = node.next
head = head.next
# printHead(head)
printHead(Solution().sortList(head))
