# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        temp = head
        pre = head

        while temp and temp.next:
            pre = pre.next
            temp = temp.next.next

            if temp == pre:
                return True
        return False

        