class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp 
        return prev