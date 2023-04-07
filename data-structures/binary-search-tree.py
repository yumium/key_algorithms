class BinaryTree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        pass

    @classmethod
    def search(cls, val, root):
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right

        return root

    @classmethod
    def minimum(cls, root):
        if root is None:
            return None
        
        while root.left:
            root = root.left
        
        return root.val
    
    @classmethod
    def maximum(cls, root):
        if root is None:
            return None
        
        while root.right:
            root = root.right

        return root.val
    
    @classmethod
    def successor(cls, root):
        if root.right is not None:
            return cls.minimum(root.right)

        while root.p and root.p.right == root:
            root = root.p
        
        return root.p.val if root.p is not None else None
        
    @classmethod
    def predecessor(cls, root):
        if root.left is not None:
            return cls.maximum(root.left)
        
        while root.p and root.p.left == root:
            root = root.p

        return root.p.val if root.p is not None else None

    @classmethod
    def insert(cls, val, root):
        # Pre: val is not in tree
        root0 = root

        if root is None:
            return BinaryTree(val, None, None)
        
        parent = None
        while root is not None:
            parent = root
            if val < root.val:
                root = root.left
            else:
                root = root.right
            
        if val < parent.val:
            parent.left = BinaryTree(val, None, None)
        else:
            parent.right = BinaryTree(val, None, None)
        
        return root0


