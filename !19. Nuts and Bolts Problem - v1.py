#User function Template for python3

class Solution:
    def matchPairs(self, nuts, bolts, n):
        # On appelle la fonction de tri QuickSort pour trier les écrous et les boulons
        self.quickSort(nuts, bolts, 0, n - 1)

    def quickSort(self, nuts, bolts, low, high):
        if low < high:
            # Choisir le pivot
            pivot_index = self.partition(nuts, low, high, bolts[high])
            # Partitionner bolts autour du pivot
            self.partition(bolts, low, high, nuts[pivot_index])
            # Trier les sous-listes avant et après le pivot récursivement
            self.quickSort(nuts, bolts, low, pivot_index - 1)
            self.quickSort(nuts, bolts, pivot_index + 1, high)

    def partition(self, arr, low, high, pivot):
        # Trouver l'index où le pivot est dans arr
        pivot_index = arr.index(pivot)
        # Placer le pivot à la fin
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        left = low
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[high] = arr[high], arr[left]
        return left


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

