class Solution(object):
    def trap(self, height):
        start = 0
        end = len(height) - 1
        leftmax = 0
        rightmax = 0
        totalwater = 0

        while start < end:
            leftmax = max(leftmax, height[start])
            rightmax = max(rightmax, height[end])

            if leftmax < rightmax:
                totalwater += leftmax - height[start]
                start += 1
            else:
                totalwater += rightmax - height[end]
                end -= 1

        return totalwater            
        