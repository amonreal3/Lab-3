#lab 3
#Adrian Monreal
#805870881


import numpy as np
import matplotlib.pyplot as plt

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def Insert(T, newItem):
    if T == None:
        T = BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T


def Delete(T, del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left, del_item)
        elif del_item > T.item:
            T.right = Delete(T.right, del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None:  # T is a leaf, just remove it
                T = None
            elif T.left is None:  # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left
            else:  # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right, m.item)
    return T


def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item, end = ' ')
        InOrder(T.right)


def InOrderD(T, space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right, space + '   ')
        print(space, T.item)
        InOrderD(T.left, space + '   ')


def Smallest(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T


def SmallestRec(T): #recursive
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)


def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)


def Find(T, k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item < k:
        return Find(T.right, k)
    return Find(T.left, k)


def FindAndPrint(T, k):
    f = Find(T, k)
    if f is not None:
        print(f.item, 'found')
    else:
        print(k, 'not found')

#1
def drawNode(center, rad, numberInside):
    n = int(4 * rad * math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    ax.plot(x, y, color='k')

def drawTree()

#2
def iterative_search(T, key):
    t = T
    while t != None:
        if t.item == key:
            return t
        elif t.item < key:
            t = t.right
        else:
            t = t.left

#3

def BSTFromList(SortedList):
    mid = SortedList[len(SortedList)/2]
    newRoot= BST(mid)
    midIndex = len(SortedList) / 2
    newRoot.left = BSTFromList(SortedList[0:midIndex-1])
    newRoot.right = BSTFromList(SortedList[midIndex+1:-1])

#4
def ListFromBST(T):
    if T is None:
        return None
    t=T
    sortedList = []
    sortedList.append(ListFromBST(T.left))
    sortedList.append(t)
    sortedList.append(ListFromBST(T.right))
    return sortedList

#5
















T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)