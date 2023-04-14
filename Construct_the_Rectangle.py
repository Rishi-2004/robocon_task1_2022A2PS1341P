class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt_area = int(math.sqrt(area))
        for width in range(sqrt_area, 0, -1):
            if area % width == 0:
                length = area // width
                return [length, width]