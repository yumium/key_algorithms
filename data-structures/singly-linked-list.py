class Node:
    def __init__(self, datum, next):
        self.datum = datum
        self.next = next

class Singly:
    '''
    Abstration function:
        Let's define function L first, which will help us define the abs function
            L(None) = []
            L(a) = a.datum:L(a.next)
        Then abs(self) = L(self.head.next)

    Concrete DTI:
    - self.head.datum holds the size of the linked list, which is maintained
    - the linked list is finite (acyclic)
    '''

    def __init__(self):
        self.head = Node(0, None)

    def __str__(self):
        out = ""
        separator = " -> "

        first = True
        node = self.head.next
        while (node != None):
            if not first:
                out += separator
            out += str(node.datum)
            node = node.next
            first = False

        return out

    # --- Haskell style operations --- #

    def cons(self, val):
        self.insert(0, val)

    def getHead(self):
        if self.length() != 0:
            out = self.popVal(0)
            return out

    # --- Mutable operations --- #

    def insert(self, pos, val):
        '''
        Pre: 0 <= pos <= length
        Post: Insert node of datum val at position pos. Returns True if successful, False if not
        '''
        if not (0 <= pos <= self.length()):
            return False
        
        curPos = 0
        node = self.head
        # Invariant: node points to the node previous to the node at position curPos
        while (curPos < pos):
            node = node.next
            curPos += 1

        node.next = Node(val, node.next)
        self._setLength(self.length()+1)

        return True

    def delete(self, pos):
        '''
        Pre: 0 <= pos < length
        Post: Deletes node at position pos. Returns True if successful, False if not
        '''
        if not (0 <= pos <= self.length()):
            return False
        
        curPos = 0
        node = self.head
        # Invariant: node points to the node previous to the node at position curPos
        while (curPos < pos):
            node = node.next
            curPos += 1

        node.next = node.next.next
        self._setLength(self.length()-1)

        return True

    def popVal(self, pos):
        '''
        Pre: 0 <= pos < length
        Post: Returns value of node at position *pos* and deletes the node. Returns False if unsuccessful
        '''
        if not (0 <= pos < self.length()):
            return False

        out = self.getVal(pos)
        self.delete(pos)

        return out

    # --- Immutable operations --- #

    def length(self):
        '''
        Returns length of the linked list
        '''
        return self.head.datum

    def setVal(self, pos, val):
        '''
        Pre: 0 <= pos < length
        Post: Sets node value at position *pos* to be *val*. Returns True if successful, False if not
        '''
        if not (0 <= pos < self.length()):
            return False

        node = self._getNodeAtPos(pos)
        node.datum = val

        return True


    def getVal(self, pos):
        '''
        Pre: 0 <= pos < length
        Post: Returns value of node at position *pos*. Returns False if unsuccessful
        '''
        if not (0 <= pos < self.length()):
            return False

        node = self._getNodeAtPos(pos)

        return node.datum

    def _getNodeAtPos(self, pos):
        curPos = 0
        node = self.head.next
        # *node* points to node at position *curPos*
        while (curPos < pos):
            node = node.next
            curPos += 1
        
        return node

    def _setLength(self, length):
        self.head.datum = length