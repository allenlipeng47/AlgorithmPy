class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if (self.next == None):
            return str(self.val)
        else:
            return str(self.val) + '->' + str(self.next)

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = dummyHead = ListNode(0)
        dummyHead.next = head
        while head != None:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return dummyHead.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
s = Solution()
s.removeElements(l1, 3)
print (l1)

