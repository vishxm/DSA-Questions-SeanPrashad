"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev = tail = None
        node = root
        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                prev = node.left
                if not tail:
                    tail = prev
            if node.right:
                if prev:
                    prev.next = node.right
                prev = node.right
                if not tail:
                    tail = prev
            node = node.next
            if not node:
                node = tail
                prev = tail = None
        return root