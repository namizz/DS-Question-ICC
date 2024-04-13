class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        store = [0]
        left = 0
        right = 0
        for num in nums:
            if num == 1:
                right += 1
        max = right
        size = len(nums)
        for i in range(size):
            if nums[i] == 0:
                left+=1
            else:
                right-=1
            current_Answer = left + right
            if current_Answer == max:
                store.append(i+1)
            elif current_Answer > max:
                max = current_Answer
                store = [i+1]
        return store
p =Solution()
print(p.maxScoreIndices([0,0,1,0]))

