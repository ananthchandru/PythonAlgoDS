class CanPlaceFlowers:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        #O(N) space complexity solution
        f = [0] + flowerbed + [0]
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i]=1
                n-=1
        return n<=0

    def canPlaceFlowers1(self, flowerbed: [int], n: int) -> bool:
        #O(1) space complexity solution

        for i in range(len(flowerbed)):
            if n==0:
                return True
            if (i==0 or flowerbed[i-1]==0) and flowerbed[i]==0 and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return n==0

obj = CanPlaceFlowers()
print(obj.canPlaceFlowers([1,0,0,0,1], 1))
print(obj.canPlaceFlowers([1,0,0,0,1], 2))
print(obj.canPlaceFlowers([0,0,1,0,0], 1))
print(obj.canPlaceFlowers([1,1,0,0,0], 1))
print("\n")
print(obj.canPlaceFlowers1([1,0,0,0,1], 1))
print(obj.canPlaceFlowers1([1,0,0,0,1], 2))
print(obj.canPlaceFlowers1([0,0,1,0,0], 1))
print(obj.canPlaceFlowers1([1,1,0,0,0], 1))