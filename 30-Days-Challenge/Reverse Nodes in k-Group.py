# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n=0
        temp=head
        while(temp is not None):
            n+=1
            temp=temp.next
        print(n)
        prevset=None
        temp=head
        for i in range(n//k):
            prev=None
            curr=temp
            start=curr
            for j in range(k):
                temp=temp.next
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
            if(prevset is None):
                head= prev
            else:
                prevset.next=prev
            prevset=start
        prevset.next=temp
        return(head)
        
