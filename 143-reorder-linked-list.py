from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# How to:
# - Find the middle using fast and slow pointer technique 
# - Reverse the second half in-place 
# - Merge both linked list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return  # Edge case: empty list or single node

        first_half, second_half = self.split_list(head)
        rev_second_half = self.reverse_list(second_half)
        self.merge_list(first_half, rev_second_half)  # Modify in-place

    def merge_list(self, list1, list2):
        while list1 and list2:
            list1_next, list2_next = list1.next, list2.next

            list1.next = list2  # Link first node to second list node
            if not list1_next:  # If list1 ends first, stop
                break
            
            list2.next = list1_next  # Link second list node back to list1
            list1, list2 = list1_next, list2_next  # Move forward

    def reverse_list(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next  # Use a clearer variable name
            curr.next = prev  # Reverse link
            prev = curr
            curr = next_node
        return prev  # Return new head of reversed list

    def split_list(self, head):
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # Disconnect first half
        return head, slow  # Return two separate lists
        
class Optimized_Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return  # Edge case: empty list, 1 node, or 2 nodes
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Split the list
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Merge the two halves in-place
        first, second = head, prev  # Second is now the reversed half
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next  # Move forward
        


def create_linked_list(nums):
    head = None
    for num in nums[::-1]:
        head = ListNode(val=num, next=head)
    return head

def print_ll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,4,5]
    nums = create_linked_list(nums)
    obj.reorderList(nums)
    print_ll(nums)
