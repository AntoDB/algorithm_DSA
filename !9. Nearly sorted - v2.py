#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        # code here
        sorted_list = []
        for elm in a:
            if len(sorted_list) == 0:
                sorted_list.append(elm)
            else:
                print(f'sorted list : {sorted_list}')
                index = 0
                for idx, sorted_elm in enumerate(sorted_list):
                    index = idx
                    if sorted_elm > elm:
                        #sorted_list[:] = list(elm)
                        #sorted_list.insert(index, elm)
                        sorted_list = [elm] + sorted_list
                        break
                    elif len(sorted_list) == index + 1:
                        #sorted_list.insert(index + 1, elm)
                        sorted_list += [elm]
                        break
                #sorted_list[index:index] = list(elm)
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
