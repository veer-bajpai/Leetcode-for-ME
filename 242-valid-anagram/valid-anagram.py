class Solution(object):
    def isAnagram(self, s, t):
        r_s = set(s)
        d_t = set(t)

        if r_s != d_t or len(s) != len(t):
            return False

        for char in r_s:
            if s.count(char) != t.count(char):
                return False
        return True        