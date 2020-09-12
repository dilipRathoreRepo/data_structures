from binary_tree import BinaryTree

"""
A binary search tree relies on the property that the keys less than parent are found in the left subtree and keys
greater than parent are found in the right subtree. This property holds true for each parent and a child. All keys
in the left of the root are less than the root. While all keys on the right of the root are larger than the root.
"""


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        if self.parent and self.parent.hasLeftChild() == self:
            return True
        else:
            return False

    def isRightChild(self):
        if self.parent and self.parent.hasRightChild() == self:
            return True
        else:
            return False

    def isRoot(self):
        if self.parent is None:
            return True
        else:
            return False

    def isLeaf(self):
        if self.leftChild is None and self.rightChild is None:
            return True
        else:
            return False

    def hasAnyChildren(self):
        if self.leftChild or self.rightChild:
            return True
        else:
            return False

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.length()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key=key, val=val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.left)
            else:
                currentNode.left = TreeNode(key=key, val=val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.right)
            else:
                currentNode.right = TreeNode(key=key, val=val, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key=key, val=value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if currentNode is None:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return self.get(key=item) is not None


# OPTION 1
def compare_key_left_child(currentNode):
    if currentNode.hasLeftChild():
        if currentNode.left.key < currentNode.key:
            return compare_key_left_child(currentNode.left)
        else:
            return False
    return True


def compare_key_right_child(currentNode):
    if currentNode.hasRightChild():
        if currentNode.right.key > currentNode.key:
            return compare_key_right_child(currentNode.right)
        else:
            return False
    return True


def bst_or_not(t):
    if not t.root:
        return False
    return compare_key_left_child(t.root) and compare_key_right_child(t.root)

# OPTION 2
# tree_vals = []
# def inorder(tree):
#     if tree is not None:
#         inorder(tree.getLeftChild())
#         tree_vals.append(tree.getRootVal())
#         inorder(tree.getRightChild())
#
#
# def sort_check(tree_vals):
#     if tree_vals == sorted(tree_vals):
#         return True

# inorder(tree)
# sort_check(tree_vals)


bst = BinarySearchTree()
bst.put(1, 'one')
bst.put(2, 'two')
bst.put(9, 'nine')
bst.put(6, 'six')
bst.put(100, 'hundred')
bst.put(5, 'five')

print(f'length of bst is {len(bst)}')
print(f'val of 9 is {bst.get(9)}')
print(f'tree is bst or not : {bst_or_not(bst)}')


bt = BinaryTree(5)
bt.insertLeft(3)
bt.insertRight(6)
print(f'bt root is {bt.key}, bt left child is {bt.left.key} and bt right child is {bt.right.key}')
