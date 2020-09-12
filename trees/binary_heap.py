
class BinHeap:
    """
    a balanced binary tree has each node with two children. Exception could be the last level where only one child can
    be there. It has methods to insert elements into the tree (which will automatically adjust the elements in correct
    position. Similarly, elements removed will cause the tree to adjust itself. There is an additional method which will
    create a binary tree from a list. for each element in a particular position, its left and right children can be
    found in 'i * 2' and '(i * 2) + 1' position.
    """
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i // 2] > self.heapList[i]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = tmp
            i *= 2

    def minChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            leftChild = self.heapList[(i * 2)]
            rightChild = self.heapList[(i * 2) + 1]
            if leftChild < rightChild:
                return i * 2
            else:
                return (i * 2) + 1

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        while i > 0:
            self.percDown(i)
            i -= 1


a = BinHeap()
a.insert(2)
a.insert(6)
a.insert(3)
a.insert(5)
print(a.currentSize)
print(a.heapList)

print("*" * 15)
lst = [2, 6, 3, 5]
b = BinHeap()
b.buildHeap(lst)
print(b.currentSize)
print(b.heapList)
