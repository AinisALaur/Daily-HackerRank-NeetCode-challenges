class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        curr = dummy 

        for _ in range(left - 1):
            curr = curr.next
        
        nodeBeforeList = curr
        firstNodeInList = curr.next
        
        prev = None
        curr = curr.next
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        lastNodeInList = prev

        nodeBeforeList.next = lastNodeInList
        firstNodeInList.next = temp

        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
curr = sol.reverseBetween(node1, 1, 3)

while curr:
    print(curr.val)
    curr = curr.next