# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()   # Dummy head to simplify result construction
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


# -------------------------
# Helper functions for testing
# -------------------------

def list_to_linked(lst):
    """Convert a Python list to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    sol = Solution()

    l1 = list_to_linked([2,4,3])
    l2 = list_to_linked([5,6,4])
    result = sol.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [7, 0, 8]

    l1 = list_to_linked([0])
    l2 = list_to_linked([0])
    result = sol.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [0]

    l1 = list_to_linked([9,9,9,9,9,9,9])
    l2 = list_to_linked([9,9,9,9])
    result = sol.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [8,9,9,9,0,0,0,1]
