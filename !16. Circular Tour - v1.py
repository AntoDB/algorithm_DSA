'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        total_petrol = 0  # Total petrol available
        total_distance = 0  # Total distance to cover
        start_index = 0  # Starting index
        current_petrol = 0  # Petrol at current pump

        # Traverse all petrol pumps
        for i in range(n):
            total_petrol += lis[i][0]
            total_distance += lis[i][1]
            current_petrol += lis[i][0] - lis[i][1]

            # If at any point, petrol at current pump is negative,
            # reset starting index to next index and reset current petrol
            if current_petrol < 0:
                start_index = i + 1
                current_petrol = 0

        # If total petrol is less than total distance, no solution exists
        if total_petrol < total_distance:
            return -1
        else:
            return start_index

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends

