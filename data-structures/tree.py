class Node:
    def __init__(self, name="root", child=None):
        self.name = name
        self.child = child if child is not None else []

    def addChild(self, c):
        self.child.append(c)

#    *
#   /|\
#  1 2 +
# /|  / \
#3 4 5   6

myTree = Node("*",[
    Node("1",[
        Node("3"),
        Node("4")
    ]),
    Node("2"),
    Node("+",[
        Node("5"),
        Node("6")
    ])
])


class NAryTree:
    def __init__(self):
        pass

    @classmethod
    def preOrder(cls, tree):
        print(tree.name)
        for child in tree.child:
            cls.preOrder(child)

    @classmethod
    def preOrder2(cls, tree):
        res = []
        stack = [tree]
        while len(stack) > 0:
            v = stack.pop()
            res.append(v.name)
            stack.extend(v.child[::-1])
        
        return res

    @classmethod
    def postOrder(cls, tree):
        res = []
        stack = [tree]
        while len(stack) > 0:
            v = stack.pop()
            res.append(v.name)
            stack.extend(v.child)

        return res[::-1]

    @classmethod
    def levelOrder(cls, tree):
        res = []
        q = [tree]
        while len(q) > 0:
            node = q.pop(0)        
            res.append(node.name)
            q.extend(node.child)

        return res

if __name__ == '__main__':
    print(f'Preorder: {NAryTree.preOrder2(myTree)}')
    print(f'Postorder: {NAryTree.postOrder(myTree)}')
    print(f'Levelorder: {NAryTree.levelOrder(myTree)}')
