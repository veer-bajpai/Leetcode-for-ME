class Solution(object):
    def sortSentence(self, s):
        s = s.split()
        b = []

        for i in range(1, len(s) + 1):
            for j in s:
                if j[-1] == str(i):
                    b.append(j[:-1])
        return" ". join(b)            