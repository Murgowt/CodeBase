# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        k=head
        while(head is not None):
            temp=head
            while( temp.val==head.val ):
                temp=temp.next
                
                if(temp is None):
                    head.next=None
                    break
            head.next=temp
            head=head.next
            
        return(k)
