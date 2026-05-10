# 234 回文链表


# O(n) O(n)
class Solution1(object):
    def isPalindrome(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


# O(n) O(n) Bad!
class Solution2(object):
    def isPalindrome(self, head):
        self.p = head

        def check(q):
            if q:
                if not check(q.next):
                    return False
                if self.p.val != q.val:
                    return False
                self.p = self.p.next
            return True

        return check(head)


# O(n) O(1) 快慢指针，链表逆转
class Solution3(object):
    def isPalindrome(self, head):
        if not head:
            return True
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse(first_half_end.next)

        result = True
        first_pos = head
        second_pos = second_half_start
        while result and second_pos is not None:
            if first_pos.val != second_pos.val:
                result = False
            first_pos = first_pos.next
            second_pos = second_pos.next
        first_half_end.next = self.reverse(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
