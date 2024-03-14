#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        #print(head)
        #print(head.data)
        #print(head.next)
        #print(head.next.data)
        node_list = []
        try:
            while 1:
                node_list.append(f'{head.data}')
                head = head.next
        except:
            pass
        node_list.sort()
        #print(node_list)
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, node_list))
        for x in nodes_p:
            p.append(x)  # add to the end of the list
        # Verification
        '''
        print(p)
        print(p.head)
        head=p.head
        node_list = []
        try:
            while 1:
                node_list.append(f'{head.data}')
                head = head.next
        except:
            pass
        #print(node_list)
        '''

        return p.head

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
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
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        #print(input().strip().split())
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends


# Tested inputs :
'''
1
6
1 2 6 4 5 3
'''
