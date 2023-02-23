# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        prepre = dummyNode
        pre = head
        cur = head.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre.next = temp
            prepre.next = cur
            prepre = pre
            pre = temp 
            cur = pre.next
        return dummyNode.next
        