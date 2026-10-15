class Solution(object):
    def diagonalSum(self, mat):
        first = 0
        last = len(mat) - 1
        total = 0

        for i in mat:
            if first == last:
                total += i[first]
            else:
                total += i[first] + i[last]
            first += 1
            last -= 1
        return total            