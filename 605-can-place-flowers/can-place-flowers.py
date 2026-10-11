class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # Return immediately because placing zero flowers is always possible.
        if n == 0:
            return True

        # Scan every plot in the flowerbed.
        for i in range(len(flowerbed)):
            # A flower can only be planted in an empty plot.
            if flowerbed[i] == 0:
                # The left side is valid if this is the first plot or its left neighbor is empty.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                # The right side is valid if this is the last plot or its right neighbor is empty.
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # Plant only when both adjacent positions are empty or out of bounds.
                if left_empty and right_empty:
                    # Mark this plot as occupied so future checks respect adjacency.
                    flowerbed[i] = 1

                    # One required flower has now been planted.
                    n -= 1

                    # Return early once all required flowers are placed.
                    if n == 0:
                        return True

        # Not enough valid positions were available.
        return False