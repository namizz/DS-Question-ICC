from typing import List
#time exceeds

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        store = []
        num_left = []
        num_right = nums
        y = len(nums)
        max = 0
        print ("lenth of y",y)
        for k in range(len(nums)+1):
            i = 0
            j = 0
            left = 0
            right = 0

            while i < len(num_right):#check if there is 1 in the num_right and store its count in variable right
                if num_right[i] == 1:
                    right += 1
                i += 1
            print("right",right)
            if len(num_right) >= y:
                max = right
            print(max)
            while j < len(num_left):#checks if there is 0 in the nums_left and store its count in variable left
                if num_left[j]==0:
                    left+=1
                j+=1
            print("left",left)
            if max < (left+right):
                max = left + right
                store.clear()
                store.append(k)
            elif max == left+right:
                store.append(k)
            print("max", max)
            print("store",store)
            if k < y:
                num_left.append(num_right[0])
                num_right.pop(0)
            print("numleft", num_left)
            print("numright",num_right)



        return store
p =Solution()
print(p.maxScoreIndices([0,0,1,0]))

