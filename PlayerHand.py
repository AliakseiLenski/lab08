from Card import Card 

class PlayerHand:
    
    def __init__(self):
        self.root = None # BST needs reference  to the root
        self.size = 0
        
    def getTotalCards(self):
        return self.size

    #Find minimum value in a subtree by walking down
    #the left children
    def getMin(self):
        if self.root == None:
            return None
        else:        
            minCard = self.root
            while minCard.left != None:
                minCard = minCard.left
            return minCard
        
        
    #key - suit, rank   
    def put(self, suit, rank):
        if self.root:
            self._put(suit.upper(), str(rank).upper(), self.root)
        else:
            self.root = Card(suit.upper(), str(rank).upper())
        self.size += 1

    def _put(self,suit, rank,currentNode):
        temp = Card(suit, rank)

        if temp < currentNode:
            if currentNode.left != None:
                self._put(suit, rank, currentNode.left)
            else:
                temp.setParent(currentNode)
                currentNode.left = temp
        elif temp > currentNode:
            if currentNode.right != None:
                self._put(suit, rank, currentNode.right)
            else:
                temp.setParent(currentNode)
                currentNode.right = temp
        elif temp == currentNode:
            currentNode.count += 1


    def getSuccessor(self, suit, rank):
        successor = None

        if self.size == 0 or self._get(suit, rank, self.root) == None:
            return successor
        else:
            found = self._get(suit, rank, self.root)
            if found.right != None:
                successor = found.right
                while successor.left != None:
                    successor = successor.left
            else:
                if found.parent:
                    if found == found.parent.left:
                        successor = found.parent
                    else:
                        found.parent.right = None
                        successor = self.getSuccessor(found.parent.suit, found.parent.rank)
                        found.parent.right = found
        return successor

    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def get(self,suit, rank):
        if self.root:
            res = self._get(suit, rank, self.root)
            if res:
                return res
        return None
    '''        
    def _get(self,suit, rank, currentNode):
       if not currentNode:
           return None
       elif currentNode.suit == suit and currentNode.rank == rank:
           return currentNode
       elif suit < currentNode.suit and rank < currentNode.rank:
           return self._get(suit, rank, currentNode.left)
       else:
           return self._get(suit, rank, currentNode.right)
    '''
    def _get(self, suit, rank, currentNode):
        temp = Card(suit, rank)
        if currentNode != None:
            if not currentNode:
                return None
            elif currentNode.suit.upper() == suit.upper() and str(currentNode.rank).upper() == str(rank).upper():
                return currentNode
            elif temp < currentNode:
                return self._get(suit, rank, currentNode.left)
            else:
                return self._get(suit, rank, currentNode.right)
   
    def delete(self, suit, rank):
        suit = suit.upper()
        rank = str(rank).upper()
        
        if self.size == 0:
            return False
        elif self.root.suit.upper() == suit.upper() and str(self.root.rank).upper() == str(rank).upper() and self.root.left == None and self.root.right == None:
            if self.size == 1:
                self.root = None
                self.size = self.size - 1
                return True
            else:
                self.root.count = self.root.count - 1
                self.size = self.size - 1
                return True            
        else:
            nodeToRemove = self._get(suit, rank, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
                return True 
        return False

    def remove(self, currentNode):
        if currentNode.count > 1:
            currentNode.count = currentNode.count - 1
        else:        
            # leaf
            if currentNode.left == None and currentNode.right == None:
                if currentNode == currentNode.parent.left:
                    currentNode.parent.left = None
                else:
                    currentNode.parent.right = None
                    
            # two children
            elif currentNode.left != None and currentNode.right != None:
                successor = self.getSuccessor(currentNode.suit, currentNode.rank)
                successor.spliceOut()
                currentNode.suit = successor.suit
                currentNode.rank = successor.rank
                currentNode.count = successor.count

            # one child
            else:
                # left child
                if currentNode.left != None:
                    if currentNode.parent != None:
                        if currentNode == currentNode.parent.left:
                            currentNode.left.setParent(currentNode.parent)
                            currentNode.parent.setLeft(currentNode.left)
                        elif currentNode == currentNode.parent.right:
                            currentNode.left.setParent(currentNode.parent)
                            currentNode.parent.setRight(currentNode.left)
                    else:
                        currentNode.replaceNodeData(currentNode.left.suit, currentNode.left.rank, currentNode.left.count, currentNode.left.left, currentNode.left.right)

                # right child
                else:
                    if currentNode.parent != None:
                        if currentNode == currentNode.parent.left:
                            currentNode.right.setParent(currentNode.parent)
                            currentNode.parent.setLeft(currentNode.right)
                        elif currentNode == currentNode.parent.right:
                            currentNode.right.setParent(currentNode.parent)
                            currentNode.parent.setRight(currentNode.right)
                    else:
                        currentNode.replaceNodeData(currentNode.right.suit, currentNode.right.rank, currentNode.right.count, currentNode.right.left, currentNode.right.right)     
 
    def _preOrder(self, current):
        ret = ""
        if current is not None:
            ret += str(current)
            if current.getLeft() is not None:
                ret+= self._preOrder(current.getLeft())
            if current.getRight() is not None:
                ret+= self._preOrder(current.getRight())
        return ret
        
    '''    
    def preOrder(self):
        ret = ""
        if self is not None:
            ret+= self._preOrder(self.root)
        return ret
    '''
    def preOrder(self):
        return self._preOrder(self.root)

    def _inOrder(self, current):
        ret = ""
        if current is not None:
            if current.getLeft() is not None:
                ret+= self._inOrder(current.getLeft())
            ret += str(current)
            if current.getRight() is not None:
                ret+= self._inOrder(current.getRight())
        return ret
    '''
    def inOrder(self):
        ret = ""
        if self !=None:
            ret += self._inOrder(self.root)
        return ret
    '''
    def inOrder(self):
        return self._inOrder(self.root)


