class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            current = []
            for j in range(len(res[-1]) + 1):
                current.append(temp[j] + temp[j + 1])
            res.append(current)
        return res       