class Solution(object):
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)

        for s in strs:
            count = [0]*26

            for letter in s:
                count[ord(letter) - ord('a')] += 1
            d[tuple(count)].append(s)

        return d.values()    