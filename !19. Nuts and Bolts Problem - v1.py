#User function Template for python3

class Solution:
    def matchPairs(self, nuts, bolts, n):
        # Code here
        # Utiliser un tri personnalisé pour chaque ensemble
        self.quickSort(nuts, bolts, 0, n-1)
    
    def quickSort(self, nuts, bolts, low, high):
        if low < high:
            # Utiliser le dernier élément des nuts comme pivot pour partitionner bolts
            pivot_index = self.partition(bolts, low, high, nuts[high])
            # Ensuite, utiliser le pivot correspondant dans bolts pour partitionner nuts
            self.partition(nuts, low, high, bolts[pivot_index])
            
            # Trier récursivement les sous-tableaux de gauche et de droite
            self.quickSort(nuts, bolts, low, pivot_index-1)
            self.quickSort(nuts, bolts, pivot_index+1, high)
    
    def partition(self, array, low, high, pivot):
        i = low
        for j in range(low, high):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
            elif array[j] == pivot:
                array[j], array[high] = array[high], array[j]
                j -= 1
        array[i], array[high] = array[high], array[i]
        return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends



# Tested inputs :
'''
1
5
@ % $ # ^
% @ # $ ^
'''

