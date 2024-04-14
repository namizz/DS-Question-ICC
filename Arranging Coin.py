from typing import List
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            check = (mid * (mid + 1)) // 2
            if n == check:
                return mid
            elif n < check:
                right = mid - 1
            else:
                left = mid + 1

        return right
p = Solution()
print(p.arrangeCoins(9))