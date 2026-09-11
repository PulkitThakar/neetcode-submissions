class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.append(1)
        count = 0

        l = -2
        for r in range(len(flowerbed)):
            if flowerbed[r] == 1:
                print(f"{l}  {r}")
                temp = max(0, r - l - 3)
                count += temp//2
                if temp % 2 == 1:
                    count += 1
                l = r
        print(count)
        return count >= n