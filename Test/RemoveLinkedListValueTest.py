import unittest
from lc.RemoveLinkedListValue import Solution, ListNode

class RemoveLinkedListValueTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test1(self):
        l1, l2, l3, l4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
        l1.next = l2
        l2.next = l3
        l3.next = l4
        l1 = self.s.removeElements(l1, 3)
        assert str(l1) == '1->2->4'

    def test2(self):
        l1, l2, l3, l4 = ListNode(1), ListNode(1), ListNode(1), ListNode(1)
        l1.next = l2
        l2.next = l3
        l3.next = l4
        l1 = self.s.removeElements(l1, 1)
        assert l1 == None


    def tearDown(self):
        pass

