# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if not head: return head
            lastElement = head
            lengthList= 1
            while lastElement.next:
                lastElement = lastElement.next
                lengthList += 1
            k = k%lengthList
            if k==0:
                return head
            else:
                lastElement.next = head
                tempNode = head
                for _ in range(lengthList-k-1):
                      tempNode = tempNode.next
                answer = tempNode.next
                tempNode.next = None
                return answer

""" class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        temp = head
        lengthList = 1
        while temp.next:
            lengthList += 1
            temp = temp.next
        k = k%lengthList
        if k==0: 
            return head
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = head
            temp = head
            counter = 0
            while counter < k:
                temp = temp.next
                counter += 1
            res = temp.next
            temp.next = None
            return res"""