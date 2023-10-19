# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 , temp2 , temp3 = head , head , head
        while temp1: 
            while temp3:
                if temp2.val > temp3.val:
                    temp2 = temp3
                temp3 = temp3.next
            temp1.val , temp2.val = temp2.val , temp1.val   
            temp1 = temp1.next
            temp2 , temp3 = temp1 , temp1
        return head    