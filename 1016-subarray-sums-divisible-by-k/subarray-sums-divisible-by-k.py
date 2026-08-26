class Solution(object):
    def subarraysDivByK(self, nums, k):
        rem_counts = {0:1}
        curr_sum = 0
        counts = 0

        for num in nums:
            curr_sum += num
            rem = curr_sum % k
            if rem < 0:
                rem += k

            if rem in rem_counts:
                counts += rem_counts[rem]
                rem_counts[rem] += 1
            else:
                rem_counts[rem] = 1

        return counts                 