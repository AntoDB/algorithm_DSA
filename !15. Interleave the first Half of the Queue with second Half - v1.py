
from typing import List


class Solution:
    def rearrangeQueue(self, N : int, q : List[int]) -> List[int]:
        # code here
        middle = N - int(N/2)
        #print(f'middle = {middle}')
        #print(q)
        #print(f'début jusqu au 3 {q[:3]}')
        q1 = q[:middle]
        q2 = q[middle:]
        #print(q1)
        #print(q2)
        #print(q1[:-1])
        q_out = []
        for i in range(middle):
            q_out.append(q1[i])
            q_out.append(q2[i])
        #print(q_out)
        return q_out

#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        q=IntArray().Input(N)
        
        obj = Solution()
        res = obj.rearrangeQueue(N, q)
        
        IntArray().Print(res)
        

# } Driver Code Ends



# Tested inputs :
'''
1
4
2 4 3 1
'''
'''
1
5
2 4 3 1 5
'''

