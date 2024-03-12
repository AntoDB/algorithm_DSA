#User function Template for python3
class Solution:

    def kLargest(self,arr, n, k):
        # code here
        des_list = []
        sorted_list = arr[::]
        sorted_list.sort(reverse=True)
        for i in range(k):
            des_list.append(sorted_list[i])
        return des_list


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends



# Tested inputs :
'''
1
6 4
1 3 5 6 4 2
'''
