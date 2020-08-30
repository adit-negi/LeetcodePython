# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = ListNode()

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is not None:
            node.val, node.next = node.next.val, node.next.next
