class Solution(object):
    def twoSum(self, numbers, target):
        x = 0
        y = len(numbers) - 1
        for i in range(len(numbers)):
            if numbers[x] + numbers[y] == target:
                return [x + 1, y + 1]
            elif numbers[x] + numbers[y] < target:
                x += 1
            else:
                y -= 1