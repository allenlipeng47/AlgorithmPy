class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# This is a good one. The point is to let a and b goes same length of 2 list.
# After same distance of travel, they will meet at the same Node.
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a != None else headB
            b = b.next if b != None else headA
        return a

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l6
l5.next = l6
l6.next = l7
l7.next = l8
s = Solution()
print (s.getIntersectionNode(l1, l5).val)