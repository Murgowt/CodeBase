# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        head=None
        curr=head
        while(l1!=None and l2!=None):
            ans=l1.val+l2.val+carry
            carry=ans//10
            if(head==None):
                head=ListNode(ans%10)
                curr=head
            else:
                newnode=ListNode(ans%10)
                curr.next=newnode
                curr=newnode
            l1=l1.next
            l2=l2.next
        while(l1!=None):
            ans=l1.val+carry
            carry=ans//10
            newnode=ListNode(ans%10)
            curr.next=newnode
            curr=newnode
            l1=l1.next
        while(l2!=None):
            ans=l2.val+carry
            carry=ans//10
            newnode=ListNode(ans%10)
            curr.next=newnode
            curr=newnode
            l2=l2.next
        if(carry!=0):
            newnode=ListNode(carry)
            curr.next=newnode
            curr=newnode
        return(head)
