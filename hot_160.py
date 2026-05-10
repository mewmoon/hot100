# 160 相交链表

#O(m+n) O(m)
class Solution1(object):
    def getIntersectionNode(self, headA, headB):

        visit = set()
        while headA:
            visit.add(headA)
            headA = headA.next
        while headB:
            if headB in visit:
                return headB
            headB = headB.next
        return None

# O(m+n) O(1)
class Solution2(object):
    def getIntersectionNode(self, headA, headB):

        if not headA or not headB:
            return None
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
    