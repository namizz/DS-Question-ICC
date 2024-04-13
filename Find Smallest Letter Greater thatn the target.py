from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        if letters[len(letters)-1] <= target:
            return letters[left]
        while left <= right:
            mid = (left + right)//2
            print(mid)
            if letters[mid] > target:
                right = mid - 1
            elif letters[mid] < target:
                left = mid + 1
            elif letters[mid] == target:
                if letters[mid +1]== target:
                    left += 1
                else:
                    return letters[mid+1]
        if letters[mid] < target:
            return letters[mid+1]
        else:
            return letters[mid]

p = Solution()
print(p.nextGreatestLetter(["e","e","e","e","e","e"],"e"))