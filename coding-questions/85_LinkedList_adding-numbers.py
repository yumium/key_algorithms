# Source: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = node = ListNode((l1.val+l2.val)%10, None) # DTI: head points to head of result list, node points to last element of result list
        carry = (l1.val+l2.val) // 10 # DTI: Carry of the last added digit to the result list

        # Invariant: l1 and l2 the last nodes summed respectively
        while l1.next != None and l2.next != None:
            l1 = l1.next; l2 = l2.next
            node.next = ListNode((l1.val+l2.val+carry)%10, None)
            node = node.next
            carry = (l1.val+l2.val+carry) // 10

        while l1.next != None:
            l1 = l1.next
            node.next = ListNode((l1.val+carry)%10, None)
            node = node.next
            carry = (l1.val+carry) // 10

        while l2.next != None:
            l2 = l2.next
            node.next = ListNode((l2.val+carry)%10, None)
            node = node.next
            carry = (l2.val+carry) // 10

        if carry == 1:
            node.next = ListNode(1, None)

        return head
