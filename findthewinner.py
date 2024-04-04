from typing import List
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friend = [i for i in range(1,n+1)]
       
        start = 0
        while(len(friend)>1):
             to_be_removed = (start + k - 1)% len(friend)
             friend.pop(to_be_removed)
             start = to_be_removed
        return friend[0]
p = Solution()
print(p.findTheWinner(5,3))
