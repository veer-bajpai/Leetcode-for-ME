class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        def freq_count(a):
            freq = {}
            for ch in a:
                freq[ch] = freq.get(ch, 0) + 1
            return freq

        freq_s = freq_count(s)
        freq_t = freq_count(t)

        return freq_s == freq_t
