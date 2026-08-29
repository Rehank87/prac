# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            newnode = ListNode(sum % 10)
            current.next = newnode
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
# Output: [7,0,8]

solver = Solution()
result = solver.addTwoNumbers(l1=l1, l2=l2)
answer = []
while result:
    answer.append(result.val)
    result = result.next
print(answer)
