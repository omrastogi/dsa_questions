# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Recursive_Solution: # Less optimized
    def reverseList(self , head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head  
        
class Solution:
    def reverseList(self , head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next, curr = None, None, head
        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr
            curr = next
        return prev

def create_linked_list(nums):
    head = None
    for num in nums[::-1]:
        head = ListNode(val=num, next=head)
    return head

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3]
    nums = create_linked_list(nums)
    head = obj.reverseList(nums)
    while head:
        print(head.val, end=' ')
        head = head.next