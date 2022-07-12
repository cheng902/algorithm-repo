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

#iterative
def preorder_iterative(root):

    s=[root]

    while s:
        cur = s.pop()
        print(cur.val)
        if cur.right:
            s.append(cur.right)
        if cur.left:
            s.append(cur.left)

#preorder_iterative(root)

#recursive
def preorder_recursive(root):

    if root==None:
        return []

    
    l=preorder_recursive(root.left)
    
    r=preorder_recursive(root.right)
    return [l,root.val,r]

#print(preorder_recursive(root))



def tree_includes(root,target):

    if root is None:
        return False
    if root.val == target:
        return True
    
    l = tree_includes(root.left,target)
    r = tree_includes(root.right,target)
    print(l)
    return l or r

   
print(tree_includes(root,4))

