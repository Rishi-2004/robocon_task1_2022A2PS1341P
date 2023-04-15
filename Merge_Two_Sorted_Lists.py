class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        merged_list = ListNode()
        current_node = merged_list
        
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        
        current_node.next = l1 or l2
        
        return merged_list.next

