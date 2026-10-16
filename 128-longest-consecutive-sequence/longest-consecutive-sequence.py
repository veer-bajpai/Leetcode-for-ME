class Solution(object):
    def longestConsecutive(self, nums):
        long = 0
        s = set(nums)

        for x in s:
            i = 1
            if x-1 not in s:
                while x+i in s:
                    i += 1

                long = max(i, long)
        return long            