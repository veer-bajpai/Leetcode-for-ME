class Solution(object):
    def checkInclusion(self, s1, s2):
        low = 0
        high = len(s1)
        s1_count = Counter(s1)

        while high <= len(s2):
            window_count = Counter(s2[low:high])
            if window_count == s1_count:
                return True
            else:
                low += 1
                high += 1
        return False            