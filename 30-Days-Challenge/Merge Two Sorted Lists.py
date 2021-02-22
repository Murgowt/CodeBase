# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=None
        curr=head
        while(l1!=None and l2!=None):
            if(l1.val<l2.val):
                v=l1.val
                l1=l1.next
            else:
                v=l2.val
                l2=l2.next
            if(head==None):
                head=ListNode(v)
                curr=head
            else:
                curr.next=ListNode(v)
                curr=curr.next
        while(l1!=None):
            if(head==None):
                head=ListNode(l1.val)
                curr=head
                l1=l1.next
            else:
                curr.next=ListNode(l1.val)
                curr=curr.next
                l1=l1.next
        while(l2!=None):
            if(head==None):
                head=ListNode(l2.val)
                curr=head
                l2=l2.next
            else:
                curr.next=ListNode(l2.val)
                curr=curr.next
                l2=l2.next
        return(head)
