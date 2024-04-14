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
        upward = True

        while i <= sum:
            print(i)
            print(index1,index2)
            if (index1+index2) == i:
                diagonalOrder.append(mat[index1][index2])
                print(index1,index2, upward)
                if i%2 == 1:#diagonally down ward
                    while upward:
                        if index1 < row and index2 > 0:#index2>=0
                            index1 += 1
                            index2 -= 1
                            diagonalOrder.append(mat[index1][index2])
                        else:
                            upward = False
                            print("turn off")
                elif i%2 == 0 and i!= 0:
                    while not upward:
                        if index2 < column and index1 > 0:
                            index2 += 1
                            index1 -= 1
                            diagonalOrder.append(mat[index1][index2])
                        else:
                            upward = True
                            print("turn on")
            else:
                if not upward:
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
print(p.findDiagonalOrder([[1,2,3,4,5,6,7,8,9,10]]))



