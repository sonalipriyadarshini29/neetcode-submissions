# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find mid of linked list. fast will be at the end 
        while fast and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of linked list from mid to fast 
        curr = slow.next
        slow.next = None
        prev = None # will become the head of reversed linked list
        while curr:
            nextVal = curr.next
            curr.next = prev 
            prev = curr 
            curr = nextVal
        # interleave two halves from each side + fast is at end, slow at 0
        first = head
        second = prev
        while first and second:
            nextFirst = first.next
            nextSecond = second.next
            first.next = second
            second.next = nextFirst
            first = nextFirst
            second = nextSecond

