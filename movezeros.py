from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
        print(nums)

p = Solution()
p.moveZeroes([2,3,4,0,2,0,1])

                