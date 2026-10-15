class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for i in range(1, n):
            current = res[0]
            count = 1
            newData = ""
            for c in res[1:]:
                if c == current:
                    count += 1
                else:
                    newData = newData + str(count) + current
                    current = c
                    count = 1
            res = newData + str(count) + current
        return res                