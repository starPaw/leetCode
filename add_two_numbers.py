# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))


class Solution:
    def read_list_node(self, node):
        if node.next:
            return str(node.val) + self.read_list_node(node.next)
        else:
            return str(node.val)

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> list:
        val = int(self.read_list_node(l1)[::-1]) + int(self.read_list_node(l2)[::-1])

        node = None
        for a in str(val):
            if node:
                node = ListNode(int(a), node)
            else:
                node = ListNode(int(a))
        return node


print(Solution().addTwoNumbers(l1=l1, l2=l2))
