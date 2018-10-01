class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    print "Iteration"

    if root.left and root.right:


    if root.left < v1 and root.right < v2:
        return lca(root.right, v1, v2)
    elif root.right > v1 and root.right > v2:
        return lca(root.left, v1, v2)



tree = BinarySearchTree()

arr = [4, 2, 3, 1, 7, 6]
v = [1, 7]

tree.create(arr)

ans = lca(tree.root, v[0], v[1])

print ans

