# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        temp1=headA
        temp2=headB

        count1=0
        count2=0

        while temp1:
            count1+=1
            temp1=temp1.next
        while temp2:
            count2+=1
            temp2=temp2.next
        temp1=headA
        temp2=headB
        if count1>count2:
            diff=count1-count2
            while diff:
                temp1=temp1.next
                diff-=1
        else:
            diff=count2-count1
            while diff:
                temp2=temp2.next
                diff-=1
        while temp1 and temp2:
            if temp1==temp2:
                return temp1
            temp1=temp1.next
            temp2=temp2.next
        return None