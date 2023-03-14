class TreeNode:
    def __init__(self, datum, left, right):
        self.datum = datum
        self.left = left
        self.right = right

    @classmethod
    def preOrder(node):
        print(node.datum, end=" ")
        if node.left:
            preOrder(node.left)
        #print(node.datum, end=" ")
        if node.right:
            preOrder(node.right)
        #print(node.datum, end=" ")

    @classmethod
    def levelOrder(root):
        q = [root]
        while len(q) > 0:
            n = q.pop()
            print(n.val)
            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)