class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right



'''
    A
   / \
  B   D
 /   / \
C   E   F
'''

example_tree = TreeNode(
    'A', 
    TreeNode(
        'B',
        TreeNode(
            'C', None, None
        ),
        None
    ),
    TreeNode(
        'D',
        TreeNode('E', None, None),
        TreeNode('F', None, None)
    )
)

def preOrder(root):
    res = []
    stack = [None]
    curNode = root
    while curNode:
        res.append(curNode.val) # Print
        if curNode.right:
            stack.append(curNode.right)
        if curNode.left:
            curNode = curNode.left
        else:
            curNode = stack.pop()
    return res

def inOrder(root):
    res = []
    stack = []
    curNode = root
    while curNode or len(stack) > 0:
        if curNode:
            stack.append(curNode)
            curNode = curNode.left
        else:
            curNode = stack.pop()
            res.append(curNode.val) # Print
            curNode = curNode.right
    return res

def postOrder(root):
    res = []
    stack = []
    curNode = root
    while curNode or len(stack) > 0:
        while curNode:
            stack.append((curNode, 'L'))
            curNode = curNode.left
        curNode, mode = stack.pop()
        if mode == 'L':
            stack.append((curNode, 'R'))
            curNode = curNode.right
        else:
            res.append(curNode.val) # Print
            curNode = None
    return res

if __name__ == '__main__':
    preOrderOutput = ['A', 'B', 'C', 'D', 'E', 'F']
    inOrderOutput = ['C', 'B', 'A', 'E', 'D', 'F']
    postOrderOutput = ['C', 'B', 'E', 'F', 'D', 'A']

    preOrderResult = preOrder(example_tree)
    inOrderResult = inOrder(example_tree)
    postOrderResult = postOrder(example_tree)

    if preOrderOutput == preOrderResult:
        print('PASSED PreOrder')
    else:
        print(f'FAILED PreOrder: expected {preOrderOutput}, got {preOrderResult}')

    if inOrderOutput == inOrderResult:
        print('PASSED InOrder')
    else:
        print(f'FAILED InOrder: expected {inOrderOutput}, got {inOrderResult}')

    if postOrderOutput == postOrderResult:
        print('PASSED PostOrder')
    else:
        print(f'FAILED PostOrder: expected {postOrderOutput}, got {postOrderResult}')
