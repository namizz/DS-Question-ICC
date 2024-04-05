#the code fail on case test 23/32
#attempted
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        column = len(mat[0]) - 1
        row = len(mat)- 1
        index1 = 0
        index2 = 0
        diagonalOrder = []
        sum = row + column
        i = 0

        while i <= sum:
            print(i)
            print(index1,index2)
            if (index1+index2) == i:
                diagonalOrder.append(mat[index1][index2])
                if index1 < index2:
                    for j in range(index2):
                        if index1 < row and index2 >= 0:
                            index1 += 1
                            index2 -= 1
                            diagonalOrder.append(mat[index1][index2])
                else:
                    for j in range(index1):
                        if index2 < column and index1 >= 0:
                            print('in')
                            index2 += 1
                            index1 -= 1
                            diagonalOrder.append(mat[index1][index2])
            else:
                if index1 > index2:
                    if index1 < row:
                        index1 += 1
                    elif index2 < column:
                        index2 += 1
                else:
                    if index2 < column:
                        index2 += 1
                    elif index1 < row:
                        index1 += 1
                i -= 1
            print(diagonalOrder)
            i += 1
        return diagonalOrder
p = Solution()
print(p.findDiagonalOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))



