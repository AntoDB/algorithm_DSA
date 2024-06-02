#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self, arr, n, k):
        # Initialize a min-heap
        heap = [] # = tas en français
        
        # Add first k+1 elements to the heap
        for i in range(min(k+1, n)):
            print(f'Heap push {arr[i]}')
            heapq.heappush(heap, arr[i])
        print(f'1    heap {heap}, array {arr}\n')
        
        index = 0
        # For the remaining elements in the array
        for i in range(k+1, n):
            # Extract the minimum element from the heap and place it in the array
            print(f'Heap pop {heap} and add into array[{index}]')
            arr[index] = heapq.heappop(heap)
            index += 1
            # Add the current element to the heap
            print(f'Heap push {arr[i]}')
            heapq.heappush(heap, arr[i])
            print(f'2    heap {heap}, array {arr}\n')
        
        # Extract remaining elements from the heap and place them in the array
        while heap:
            print(f'Heap pop {heap} and add into array[{index}]')
            arr[index] = heapq.heappop(heap)
            index += 1
            print(f'3    heap {heap}, array {arr}')
        
        return arr
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
