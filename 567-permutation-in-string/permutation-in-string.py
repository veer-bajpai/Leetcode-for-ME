from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counts_1 = Counter(s1)
        i = 0
        j = len(s1)
        while j <= len(s2):
            window_counter = Counter(s2[i:j])
            if counts_1 == window_counter:
                return True
            i += 1
            j += 1
        return False