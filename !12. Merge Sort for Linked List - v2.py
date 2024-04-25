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
    # Function to merge two sorted linked lists.
    def merge(self, left, right):
        # If one of the lists is empty, return the other list
        if not left:
            return right
        if not right:
            return left

        # Compare the values of the head nodes of both lists
        if left.data < right.data:
            # If the value in the left list is smaller,
            # set the result to the current node from the left list
            # and recursively merge the remaining lists
            result = left
            result.next = self.merge(left.next, right)
        else:
            # If the value in the right list is smaller or equal,
            # set the result to the current node from the right list
            # and recursively merge the remaining lists
            result = right
            result.next = self.merge(left, right.next)

        return result

    # Function to perform merge sort on linked list.
    def mergeSort(self, head):
        # Base case: If the list is empty or has only one node, return the list
        if not head or not head.next:
            return head

        # Split the list into two halves
        prev = None  # Pointer to the previous node
        slow = head  # Pointer to the middle node (or the start of the second half)
        fast = head  # Pointer to move twice as fast as 'slow' to find the middle

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # Break the list into two halves

        # Recursively sort the two halves
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(slow)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

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
