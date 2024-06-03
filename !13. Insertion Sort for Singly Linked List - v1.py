#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        # code here
        # Créer une liste triée vide
        sorted_head = None
        
        # Parcourir chaque nœud de la liste d'entrée
        current = head
        while current:
            # Enregistrer le suivant pour la prochaine itération
            next_node = current.next
            # Insérer le nœud actuel dans la liste triée
            sorted_head = self.sortedInsert(sorted_head, current)
            # Passer au nœud suivant de la liste d'entrée
            current = next_node
        
        return sorted_head

    def sortedInsert(self, head, node):
        # Si la liste triée est vide ou si le nœud doit être inséré au début
        if head is None or node.data < head.data:
            node.next = head
            return node
        
        # Rechercher la position correcte pour insérer le nœud
        current = head
        while current.next and current.next.data < node.data:
            current = current.next
        
        # Insérer le nœud
        node.next = current.next
        current.next = node
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
INF = float("inf")
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = Node(INF)
        nodes = list(map(int, input().strip().split()))
        ptr = a
        for x in nodes:
            ptr.next = Node(INF)
            ptr = ptr.next
            ptr.data = x
        a = a.next
        ob=Solution()
        head = ob.insertionSort(a)
        printList(head)
# } Driver Code Ends