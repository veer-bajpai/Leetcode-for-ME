class Solution(object):
    def sortSentence(self, s):
        splited_string = s[::-1].split()
        splited_string.sort()
        res = []
        for word in splited_string:
            res.append(word[1:][::-1])
        return " ".join(res) 