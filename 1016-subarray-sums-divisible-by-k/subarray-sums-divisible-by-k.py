class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = [0] * k
        count[0] = 1
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            rem = prefix % k

            result += count[rem]
            count[rem] += 1

        return result                 