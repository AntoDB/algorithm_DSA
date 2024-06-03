#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self,head):
        #Your code here
        # Si la liste est vide ou contient un seul élément, elle est déjà triée
        if not head or not head.next:
            return head

        # Diviser la liste en deux moitiés
        second = self.split(head)

        # Trier récursivement les deux moitiés
        head = self.sortDoubly(head)
        second = self.sortDoubly(second)

        # Fusionner les deux moitiés triées
        return self.merge(head, second)

    def split(self, head):
        slow = head
        fast = head

        # Utiliser deux pointeurs pour trouver le milieu de la liste
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Diviser la liste en deux moitiés
        second = slow.next
        slow.next = None
        if second:
            second.prev = None

        return second

    def merge(self, first, second):
        # Si une des listes est vide, retourner l'autre liste
        if not first:
            return second
        if not second:
            return first

        # Fusionner les deux listes triées
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends