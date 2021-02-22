# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        op=head
        
        while(not head is None and not head.next is None):
            temp=head.val
            head.val=head.next.val
            head.next.val=temp
            print(head.val,head.next.val)
            head=head.next.next
            
        return(op)
