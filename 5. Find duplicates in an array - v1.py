class Solution:
    def duplicates(self, arr, n): 
        # code here
        dupp = []
        checked_list = []
        for i in range(0, n):
            if arr[i] in checked_list and not(arr[i] in dupp):
                dupp.append(arr[i])
            else:
                checked_list.append(arr[i])
   
        if len(dupp) > 0:
            dupp.sort()
            return dupp
        else:
            return [-1]

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends



# Tested inputs :
'''
1
3
5 2 5 3
'''