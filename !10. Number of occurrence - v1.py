#User function Template for python3
class Solution:

    def count(self,arr, n, x):
        # code here
        nbr_occ = 0
        for elm in arr:
            if elm == x:
                nbr_occ += 1
        return nbr_occ

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
        
# Tested inputs :
'''
1
6 4
1 2 4 4 5 4
'''
