# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val#stores the value
        self.next = next#points to next node , default is None
class Solution(object):
    def deleteDuplicates(self, head):#takes head as first node
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head#done to keep track , if not initialized we can confuse head to the first node
        while current and current.next:#iterates over all nodes including the last node
            if current.val == current.next.val:
                current.next=current.next.next#verifies the condition and skips it 
            else:
                current=current.next
        return head
'''
more efficient  code
def deleteDuplicates(self, head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
'''
