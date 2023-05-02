class TreeNode:
    def __init__(self, datum, left, right):
        self.datum = datum
        self.left = left
        self.right = right

    @classmethod
    def preOrder(cls, node):
        print(node.datum, end='')
        if node.left:
            cls.preOrder(node.left)
        #print(node.datum, end=" ")
        if node.right:
            cls.preOrder(node.right)
        #print(node.datum, end=" ")

    @classmethod
    def levelOrder(cls, root):
        q = [root]
        while len(q) > 0:
            n = q.pop()
            print(n.datum, end='')
            if n.left:
                q.insert(0, n.left)
            if n.right:
                q.insert(0, n.right)

'''
    stack curNode             loop
0  [None]    root          curNode
1      []    root  curNode + stack
2      []    root  curNode + stack
'''

    @classmethod
    def preOrderIter(cls, root):
        stack = [None]  #
        curNode = root  #

        while curNode:  #
            print(curNode.datum, end='')

            if curNode.right:
                stack.append(curNode.right)
            
            if curNode.left:
                curNode = curNode.left
            else:
                curNode = stack.pop()

    @classmethod
    def inOrderIter(cls, root):
        stack = []                          #
        curNode = root                      #
        while curNode or len(stack) > 0:    #
            if curNode:                         #
                stack.append(curNode)
                curNode = curNode.left
            else:                               #
                curNode = stack.pop()
                print(curNode.datum, end='')
                curNode = curNode.right

    @classmethod
    def postOrderIter(cls, root):
        stack = []                          #
        curNode = root                      #
        while curNode or len(stack) > 0:    #
            while curNode:                      #
                stack.append((curNode, 'L'))
                curNode = curNode.left
            curNode, mode = stack.pop()
            if mode == 'L':                     #
                stack.append((curNode, 'R'))
                curNode = curNode.right
            else:                               #
                print(curNode.datum, end='')
                curNode = None

#     A
#    / \
#   B  C
#  /|   \
# D E    F
#  /    / \
# G    H   I

my_tree = TreeNode("A",
    TreeNode("B",
        TreeNode("D", None, None),
        TreeNode("E",
            TreeNode("G", None, None),
            None
        )
    ),
    TreeNode("C", None, 
        TreeNode("F",
            TreeNode("H", None, None),
            TreeNode("I", None, None)
        )
    )
)

if __name__ == '__main__':
    print('PreOrder')
    TreeNode.preOrderIter(my_tree)  # ABDEGCFHI
    print()
    
    print('InOrder')
    TreeNode.inOrderIter(my_tree)   # DBGEACHFI
    print()

    print('PostOrder')
    TreeNode.postOrderIter(my_tree) # DGEBHIFCA
    print()

    print('Level Order')
    TreeNode.levelOrder(my_tree)    # ABCDEFGHI
    print()

    print('PreOrder recursive')     # ABDEGCFHI
    TreeNode.preOrder(my_tree)
    print()
