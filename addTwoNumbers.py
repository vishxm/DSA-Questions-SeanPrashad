class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = ListNode(0)
        nHead = ptr
        carry = 0
        while l1 and l2:
            temp = ListNode(l1.val + l2.val + carry)
            carry = temp//10
            temp.val = temp.val%10
            l1, l2 = l1.next, l2.next
            ptr.next = temp
            ptr = temp
        
        while l1:
            temp = ListNode(l1.val + carry)
            carry = temp//10
            temp.val = temp.val%10
            l1 = l1.next
            ptr.next = temp
            ptr = temp
        
        while l2:
            temp = ListNode(l2.val + carry)
            carry = temp//10
            temp.val = temp.val%10
            l2 = l2.next
            ptr.next = temp
            ptr = temp

        if carry > 0:
            temp = ListNode(carry)
            ptr.next = temp

        return nHead.next