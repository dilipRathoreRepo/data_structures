class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        print(tree.getRootVal())
        postorder(tree.getRightChild())


r = BinaryTree('root')
print(r.getRootVal())
r.insertLeft('left')
print(r.getLeftChild().getRootVal())
r.insertRight('right')
print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())
r.insertLeft('left_1')
t0 = r.getLeftChild()
t = t0.getLeftChild()
t.insertLeft('t_left')
t.insertRight('t_right')

r.insertLeft('left_2')
r.insertLeft('left_3')
r.insertRight('right_1')


print("*" * 20)
preorder(r)

print("*" * 20)
postorder(r)

print("*" * 20)
inorder(r)
