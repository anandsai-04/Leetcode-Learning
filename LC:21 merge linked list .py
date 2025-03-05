class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy node to start the merged list
        tail = dummy  # Tail pointer to keep track of the last node

        while list1 and list2:  # Iterate as long as both lists are not empty
            if list1.val < list2.val:  # If list1 has a smaller value
                tail.next = list1  # Attach list1's node to merged list
                list1 = list1.next  # Move list1 pointer forward
            else:  # If list2 has a smaller or equal value
                tail.next = list2  # Attach list2's node to merged list
                list2 = list2.next  # Move list2 pointer forward
            tail = tail.next  # Move tail forward

        # Attach remaining nodes if any list is not fully traversed
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next  # Return merged list, skipping dummy node
