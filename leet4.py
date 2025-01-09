class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i=0
        while (i < len(flowerbed)):
            if(flowerbed[i]==0):
                if(i+1<len(flowerbed) and flowerbed[i+1]==0 and (i==0 or ( i-1>=0 and flowerbed[i-1]==0))):
                    flowerbed[i]=1
                    n-=1
                    i+=1
                elif(len(flowerbed)==1 or (i==len(flowerbed)-1 and flowerbed[i-1]==0)):
                    n-=1
                    break

            i+=1
        if (n==0):
            return True
        else:
            return False    

        


obj = Solution()
print(obj.canPlaceFlowers([1,0,0,0,0,0,1], 2))

## 1,0,0,0,0,0,1