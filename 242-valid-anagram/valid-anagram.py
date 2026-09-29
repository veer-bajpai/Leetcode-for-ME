class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        singular_s = set(s)
        singular_t = set(t)
        if singular_s != singular_t or len(s) != len(t):
            return False
        for char in singular_s:
            if s.count(char) == t.count(char):
                return True
            else:
                return False
        