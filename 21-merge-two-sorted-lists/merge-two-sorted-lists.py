# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node (edge case)
        dummy = ListNode()
        tail = dummy

        # Go through each list
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                # update our 1st pointer
                l1 = l1.next
            else:
                tail.next = l2
                # update our 2nd pointer
                l2 = l2.next
            # update our tail pointer
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

# Time Complexity: O(n + m) because the while loop gets one node from either l1 or l2; no node is revisted
# Space Complexity: O(1) because no new nodes are created, only constant memory is used