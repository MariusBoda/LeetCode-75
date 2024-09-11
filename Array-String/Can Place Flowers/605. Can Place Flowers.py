class Solution:
        def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:          
            for i in range(len(flowerbed)):
                 if i == 0 or flowerbed[i-1] == 0:
                     left = True
                 else: 
                     left = False
                 if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                    right = True
                 else:
                    right = False
                                                                                                                                                           if left and right and flowerbed[i] == 0                                                                                                       flowerbed[i] = 1
                                                                                                                                                               n -= 1
                                                                                                                                                                                                                    
                                                                                                                                                       return n <= 0


