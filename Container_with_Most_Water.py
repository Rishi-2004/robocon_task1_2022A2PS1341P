class MaxAreaFinder:
    def find_max_area(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left_idx = 0
        right_idx = len(heights) - 1
        max_area = 0
        while left_idx < right_idx:
            area = (right_idx - left_idx) * min(heights[left_idx], heights[right_idx])
            max_area = max(max_area, area)
            if heights[left_idx] < heights[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return max_area
