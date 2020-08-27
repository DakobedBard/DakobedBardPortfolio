# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if(current.val == current.next.val):
                current.next = current.next.next
            else:
                current = current.next




head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

solution = Solution()
newHead = solution.deleteDuplicates(head)
