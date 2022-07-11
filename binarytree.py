class Node():
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)


def preorder_iterative(root):

    s=[root]

    while s:
        cur = s.pop()
        print(cur.val)
        if cur.right:
            s.append(cur.right)
        if cur.left:
            s.append(cur.left)
            
preorder_iterative(root)

