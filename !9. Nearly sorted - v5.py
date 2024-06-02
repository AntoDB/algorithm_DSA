#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        # code here
        sorted_list = [a.pop()]
        for i in range(len(a)):
            elm = a.pop(0)
            #print(elm)
            for index, sorted_elm in enumerate(sorted_list):
                #print(f'{index} : {sorted_elm}')
                if elm < sorted_elm:
                    sorted_list[index:index] = [elm]
                    #print(f'add : {sorted_list}')
                    break
                elif sorted_list[-1] < elm:
                    sorted_list.append(elm)
                    #print(f'add : {sorted_list}')
                    break
        #print(sorted_list)
        return sorted_list

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
