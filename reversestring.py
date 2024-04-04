from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) -1
        arr = []
        j=0
        while(left < right):
            s[right],s[left]= s[left],s[right]
            left+=1
            right-=1
        print(s)

p = Solution ()
p.reverseString("Abebe")

