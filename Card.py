class Card:
  
    
    suits = ['C', 'D', 'H', 'S']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        '''
        Constructor to initialize the suit and rank to specified values
        and parent, left, right to default value of None and count to 1
        '''
        # validate input suit is valid
        if suit.upper() in self.suits:
            self.suit = suit.upper()
        else:
            self.suit = 'C' # if not set it to default value of "C"
          
        # validate input rank is valid  
        if rank.upper() in self.ranks:
            self.rank = rank.upper()
        else:
            self.rank = "A" # if not set it to default value of "A"
          
        #initialize parent, left and right to None  
        self.parent = None  
        self.left = None
        self.right = None
        self.count = 1 # initialize count to 1

    def getSuit(self):
        # method to return the suit
        return self.suit
      
    def setSuit(self, suit):
        # method to set the suit
        # validate input suit is valid, if invalid no change
        if suit.upper() in self.suits:
            self.suit = suit.upper()
          
    def getRank(self):
        # method to return the rank
        return self.rank
      
    def setRank(self, rank):
        # method to set the rank
        # validate input rank is valid, if invalid no change
        if rank.upper()   in self.ranks:
            self.rank = rank.upper()

    def getCount(self):
        # method to return the count
        return self.count
      
    def setCount(self, count):
        # method to set the count
        self.count = count
      
    def getParent(self):
        # method to return the parent node
        return self.parent
      
    def setParent(self, parent):
        # method to set the parent node
        self.parent = parent
      
    def getLeft(self):
        # method to return the left node
        return self.left
      
    def setLeft(self, left):
        # method to set the left node
        self.left = left
      
    def getRight(self):
        #method to return the right node
        return self.right
  
    def setRight(self, right):
        # method to set the right node
        self.right = right

    def isLeaf(self):
        return not (self.right or self.left)

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def hasAnyChildren(self):
        return self.right or self.left

    def replaceNodeData(self, suit, rank, count, lc, rc):
        self.suit = suit
        self.rank = rank
        self.count = count
        self.left = lc
        self.right = rc

        if self.left != None:
            self.left.parent = self
        if self.right != None:
            self.right.parent = self

    #Used to delete the successor
    def spliceOut(self):
        #Case 1
        #If node to be removed is a leaf, set parent's
        #left or right child references to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None

        #Case 2
        #Not a leaf Node. Should only have a right child for BST removal
        elif self.hasAnyChildren():
            if self.getRight():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

        
    def __str__(self):
       # method to return string representation of the Card
       return "%s %s | %d"%(self.suit, self.rank, self.count)+ "\n"
      
    def __gt__(self, other):
        if self == None or other == None:
            return False
        
        rank = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
        suit = {"C":1, "D":2, "H":3, "S":4}

        self.rank = str(self.rank).upper()
        other.rank = str(other.rank).upper()

        if rank.get(self.rank) > rank.get(other.rank):
            return True
        elif self.rank == other.rank:
            if suit.get(self.suit.upper()) > suit.get(other.suit.upper()):
                return True
        return False

    def __lt__(self, other):
        if self == None or other == None:
            return False
        
        rank = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
        suit = {"C":1, "D":2, "H":3, "S":4}

        self.rank = str(self.rank).upper()
        other.rank = str(other.rank).upper()
  
        if rank.get(self.rank) < rank.get(other.rank):
            return True
        elif self.rank == other.rank:
            if suit.get(self.suit.upper()) < suit.get(other.suit.upper()):
                return True
        return False

    def __eq__(self, other):
        if self and other:
            return str(self.rank).upper() == str(other.rank).upper() and self.suit.upper() == other.suit.upper()
        return False
