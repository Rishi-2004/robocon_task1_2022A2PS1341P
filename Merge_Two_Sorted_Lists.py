class LinkedListMerger:
    def merge_linked_lists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
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
        
        
        if l1:
            current_node.next = l1
        elif l2:
            current_node.next = l2
        
        
        return merged_list.next
