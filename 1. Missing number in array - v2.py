#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        array.sort()
        print(array)
#        for i in range(1, n+1) :
#            print(i)
#            if i != array[i-1]:
#                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    print(a)
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends2
