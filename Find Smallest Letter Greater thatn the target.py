from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        if letters[len(letters)-1] <= target:
            return letters[left]
        while left < right:
            mid = (left + right)//2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[right]

p = Solution()
print(p.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"e"))