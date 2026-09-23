class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
       zeroes = 0
       for i in [0] + flowerbed + [0]:
           if i == 0:
               zeroes += 1
           else:
               zeroes = 0

           if zeroes == 3:
                zeroes = 1
                n -= 1

           if n == 0:
             break

       return n == 0                    
