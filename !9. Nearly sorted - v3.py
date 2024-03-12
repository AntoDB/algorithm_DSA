#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        # code here
        for idx1, elm in enumerate(a):
            #print(idx1)
            curent_nbr = 0
            try:
                if elm > a[idx1+1]:
                    curent_nbr = a[idx1+1]
                    del a[idx1+1]
                    print(f'curent_nbr: {curent_nbr}')
                    
                    for idx2, sorted_elm in enumerate(a[:idx1]):
                        if sorted_elm > curent_nbr:
                            a[idx2:idx2] = [curent_nbr]
                            break
                print(f'step: {a}')
            except:
                break
        print(a)
        for index in range(len(a)):
            try:
                if a[index] > a[index+1]:
                    self.nearlySorted(a,n,k)
            except:
                break
        return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends



# Tested inputs :
'''
1
6 4
1 3 5 6 4 2
'''
