class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nums):
    """
    使用列表构建二叉树 (LeetCode 层序格式)
    例如: [1, 2, 3, None, None, 4, 5]
    """
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nums):
        node = queue.popleft()

        # 处理左子节点
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1

        # 处理右子节点
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root


def print_tree(root):
    """
    直观打印树结构（竖向展开）
    """

    def get_height(node):
        return 1 + max(get_height(node.left), get_height(node.right)) if node else 0

    def display(node):
        if not node:
            return [], 0, 0, 0

        line1, left_pos, left_width, _ = display(node.left)
        line2, right_pos, right_width, _ = display(node.right)

        val_str = str(node.val)
        val_width = len(val_str)

        # 拼接当前层的字符串
        gap = " " * val_width
        new_line = (
            (" " * (left_pos + 1))
            + ("_" * (left_width - left_pos - 1))
            + val_str
            + ("_" * right_pos)
            + (" " * (right_width - right_pos))
        )

        # 处理连接线
        pos = left_width + (val_width // 2)

        # 合并子树的行
        combined = [new_line]
        max_len = max(len(line1), len(line2))
        for i in range(max_len):
            l = line1[i] if i < len(line1) else " " * left_width
            r = line2[i] if i < len(line2) else " " * right_width
            combined.append(l + gap + r)

        return combined, pos, left_width + val_width + right_width, max_len + 1

    lines, _, _, _ = display(root)
    for line in lines:
        print(line)
