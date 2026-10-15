class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Count frequencies using a dictionary
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Iterate backwards from highest frequency bucket down to 0
        result = []
        for freq in range(len(buckets) - 1, -1, -1):
            result.extend(buckets[freq])
            if len(result) >= k:
                return result[:k]
                
        return result
