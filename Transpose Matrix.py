from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = []
        row = len(matrix)
        column = len(matrix[0])
        for i in range(column):
            arr = []
            for j in range(row):
                arr.append(matrix[j][i])
            trans.append(arr)
        return trans
p = Solution()
print(p.transpose([[1, 2, 3,4]]))