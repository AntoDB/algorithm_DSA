class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        #print(s)
        new_list = [s.pop()]
        for i in range(len(s)):
            elm = s.pop(0)
            #print(elm)
            for index, sorted_elm in enumerate(new_list):
                #print(f'{index} : {sorted_elm}')
                if elm > sorted_elm:
                    new_list[index:index] = [elm]
                    #print(f'add : {new_list}')
                    break
                elif new_list[-1] > elm:
                    new_list.append(elm)
                    #print(f'add : {new_list}')
                    break
        #print(new_list)
        while len(new_list) > 0:
            s.append(new_list.pop())
        return s


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


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


