#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        #print(St.pop())
        St_out = []
        while len(St) > 0:
            St_out.append(St.pop())
        #print(St_out)
        while len(St_out) > 0:
            St.append(St_out.pop(0))
        
        return St

#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
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


