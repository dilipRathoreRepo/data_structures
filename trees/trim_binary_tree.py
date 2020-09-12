from binary_search_tree import TreeNode, BinarySearchTree

t = BinarySearchTree()
t.put(1, 'a')
t.put(2, 'b')
t.put(9, 'c')
t.put(6, 'd')

print(f'length of t is {len(t)}')
print(f'val of 1 is {t.get(1)}')
print(f'val of 2 is {t.get(2)}')
print(f'val of 9 is {t.get(9)}')
print(f'val of 6 is {t.get(6)}')


def trim_binary_tree(tree, min_val, max_val):
    if not tree:
        return
    tree.left = trim_binary_tree(tree.left, min_val, max_val)
    tree.right = trim_binary_tree(tree.right, min_val, max_val)

    if min_val <= tree.payload <= max_val:
        return tree

    elif tree.payload < min_val:
        return tree.right

    else:
        return tree.left
