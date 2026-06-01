# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNum = ""
        secondNum = ""

        curr = l1
        while curr:
            firstNum = str(curr.val) + firstNum
            curr = curr.next
        
        curr = l2
        while curr:
            secondNum = str(curr.val) + secondNum
            curr = curr.next
        
        result = int(firstNum) + int(secondNum)
        nodes = []
        if result == 0:
            nodes.append(ListNode(0))
        while result > 0:
            nodes.append(ListNode(result % 10))
            result //= 10
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        return nodes[0]