# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # L1 next 하면서 L1를 기준으로 순서대로(값) 연결리스트를 연결하기 위함
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
