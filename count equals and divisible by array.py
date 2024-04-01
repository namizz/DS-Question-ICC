from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter=0
        for i in range(len(nums)-1):
            for  j in range(len(nums)-1, i , -1):
                if nums [i]== nums[j]:
                    if (i*j)%k==0:
                        counter+=1
        return counter
p = Solution()
print(p.countPairs([3,1,2,2,2,1,3], 3))
