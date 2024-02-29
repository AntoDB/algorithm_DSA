#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
        print(self.arr)
        
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        data = self.arr[1::]
        self.arr = self.arr[1::]
        print(self.arr)
        print(data[0])
        if not self.arr:
            return -1
        else:
            return data[0]
        
"""

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends
"""

if __name__=='__main__':
    s=MyStack()
    s.push(2)
    s.push(3)
    s.pop()
    s.push(4)
    s.pop()
