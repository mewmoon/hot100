class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_link(nums):
    """将数组转换为链表，返回头节点"""
    if not nums:
        return None

    dummy = ListNode(0)
    current = dummy
    for val in nums:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_link(head):
    """打印链表结构"""
    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res) if res else "Empty List")
