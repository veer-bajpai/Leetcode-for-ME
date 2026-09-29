class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]

        return list(anagram_map.values())         