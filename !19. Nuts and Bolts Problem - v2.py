#User function Template for python3

class Solution:
    def matchPairs(self, nuts, bolts, n):
        #code here
        order = ['!', '#', '$', '%', '&', '*', '@', '^', '?']
        
        # Créer des dictionnaires pour enregistrer les positions des écrous et des boulons
        nuts_dict = {nut: nut for nut in nuts}
        bolts_dict = {bolt: bolt for bolt in bolts}
        
        # Trier les écrous et les boulons selon l'ordre spécifié
        sorted_nuts = []
        sorted_bolts = []
        
        for char in order:
            if char in nuts_dict:
                sorted_nuts.append(nuts_dict[char])
            if char in bolts_dict:
                sorted_bolts.append(bolts_dict[char])
        
        # Remplacer les éléments dans les listes d'origine
        for i in range(n):
            nuts[i] = sorted_nuts[i]
            bolts[i] = sorted_bolts[i]


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

