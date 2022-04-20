from Card import Card
from PlayerHand import PlayerHand

def test_Card():
    card = Card('D', '2')
    assert str(card) == "D 2 | 1"
    card1 = Card('D', '5')
    card2 = Card('D', 'A')
    card3 = Card('H', 'Q')
    card4 = Card('C', 'Q')
    assert card1 > card2 == True
    assert card2 < card3 == True
    assert card3 < card4 == True

    

def test_PlayerHand():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    #print(hand.size)
    #print(hand.root)
    print(hand.inOrder())
    print(hand.preOrder())
    print(hand.getTotalCards())
        
    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"

    assert hand.preOrder() == \
    "D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"


def test_deleteRoot():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
    hand.delete('C', 'Q')
    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C K | 1\n\
S K | 2\n"

def test_deleteLeaf():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
    hand.delete('D', 'A')
    assert hand.inOrder() == \
    "S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"

def test_deleteNodeWith2Children():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
    hand.delete('H', '7')
    assert hand.inOrder() == \
    "D A | 1\n\
S 2 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
     
    
    
    
