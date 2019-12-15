import random
import pygame
import os
import time
class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
        if val == 1:
            x = "A"
        elif self.value == 11:
            x = "J"
        elif self.value == 12:
            x = "Q"
        elif self.value == 13:
            x = "K"
        else:
            x = self.value
        path1=os.path.dirname(os.path.abspath(__file__))+"\\Cards\\"+str(x)+str(suit[0])+".png"
        self.path=str(path1)
    
        
    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)


class Deck():
    def __init__(self,num):
        self.cards = []
        self.build(num)

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print (card.show())

    # Generate 52 cards
    def build(self,num):
        self.cards = []
        for i in range(num):
            for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
                for val in range(1,14):
                    self.cards.append(Card(suit, val))
            

    # Shuffle the deck
    def shuffle(self, num=1):
        random.shuffle(self.cards)
    def find(self,suit,val):
        for i in self.cards:
            if i.suit==suit and i.value==val:
                return i
                found=True
        if found==False:
            return 0
    # Return the top card
    def deal(self):
        return self.cards.pop()
    def remove(self,suit,val):
        x=-1
        for i in self.cards:
            if i.suit==suit and i.value==val:
                x=i
                self.cards.remove(i)
                break
        if x==-1:
            return 0#Does Not Exist this card
        else:
            return x
class Player():
  
    def __init__(self, name,hand):
        self.name = name
        self.hand = hand
    def deal(self):
        return self.hand.pop()
    def find(self,suit,val):
        found=False
        for i in self.hand:
            if i.suit==suit and i.value==val:
                return i
                found=True
        if found==False:
            return 0
    def gettopcard(self,taker):
        x=self.hand.pop()
        taker.hand.append(x)
        

    def drawtop(self, deck, num=1):
        i=0
        #print(num)
        while (i<num):
            i+=1   
            card = deck.deal()
            #print(i)
            
            if card:
                self.hand.append(card)
                #card=0
                #print(self.hand)
                #input("wait"+str(i))
            else: 
                return False
        return True
    def drawcardandremove(self,deck,suit,val):
        removal=deck.remove(suit,val)
        if removal!=0:
            self.hand.append(removal)
    

    def discard(self):
        return self.hand.pop()
    def playershuffle(self):
        random.shuffle(self.hand)
    def playerpattaswitch(self,taker,suit1,val1,suit2,val2): #1 in self to 1 in taker
        x=self.find(suit1,val1)
        taker.hand.append(x)
        self.hand.remove(x)
        y=taker.find(suit2,val2)
        taker.hand.remove(y)
        self.hand.append(y)
    def sendpatta(self,taker,suit1,val1): #1 in self to 1 in taker
        x=self.find(suit1,val1)
        taker.hand.append(x)
        self.hand.remove(x)
        



def main():
    one04deck=Deck(1)
    one04deck.shuffle()
    
    print(len(one04deck.cards))
    playerone=Player("PlayerOne",[])
    playertwo=Player("Computer",[])
    playerStock=Player("Stock",[])
    playerdiscard=Player("Discard",[])
    playerdiscard.drawtop(one04deck) 
    playerone.drawtop(one04deck,13)
    playertwo.drawtop(one04deck,13)
    playerStock.drawtop(one04deck,25)
    playeroneturn=True
    playertwoturn=False
    rounds=10
    height=600
    width=800
    first=True
    Computer=True
    count=0
    playerone.hand=sorted(playerone.hand, key=lambda x: x.value)
    pygame.init()
    font = pygame.font.SysFont('Arial', 25)
    gameDisp=pygame.display.set_mode((width,height))

    back=pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'\\800.jpg').convert_alpha()
    g=pygame.image.load(os.path.dirname(os.path.abspath(__file__))+'\\back.png').convert()
    j=70
    selected=100
    #print(playerone.hand)
    playercardviewlist=[]
    for i in playerone.hand:
        playercardviewlist.append(pygame.image.load(i.path).convert())
    playerblitlist=[]
    for i in playercardviewlist:
        playerblitlist.append([j,height-150])
        gameDisp.blit(i,(j,height-150))
        j+=50
    gameExit=False
    selected=100
    selected2=100
    #print(playertwo.hand)
    while not gameExit:
        
        if rounds>0:            
            gameDisp.blit(back,(0,0))
            
            d=70
            
     
            
            discardviewlist=[]
            discardblitlist=[]
            for i in playerdiscard.hand:
                discardviewlist.append(pygame.image.load(i.path).convert())
            
            for i in discardviewlist:
                discardblitlist.append([d,300])
                gameDisp.blit(i,(d,300))
                d+=50
            gameDisp.blit(g,(350,180))
            j=50
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                    x, y = event.pos
                    #print(playerblitlist)
                    
                    for i in range(len(playerblitlist)):
                        
                        if playerblitlist[i][0]<x<playerblitlist[i][0]+50 and playerblitlist[i][1]<y<playerblitlist[i][1]+90:
                            #print("click card"+str(i))
                            
                            if first==True:
                                playerblitlist[i][1]-=30
                                selected=i
                                first=False
                                
                            elif i==selected:
                                
                                playerblitlist[selected][1]+=30
                                selected=100
                                first=True
                            elif i!=selected:
                                
                                playerblitlist[selected][1]+=30
                                playerblitlist[i][1]-=30
                                selected=i
                                first=False
                            print('selected patta is'+str(selected+1))


                if 0<=selected<=12:
                    
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        
                        
                        for i in range(len(discardblitlist)):
            
                            if discardblitlist[i][0]<=x<=discardblitlist[i][0]+50 and discardblitlist[i][1]<=y<=discardblitlist[i][1]+90:
                                #print("click card"+str(i))
                                selected2=i
                                print('selected discard patta is'+str(selected2+1))
                                playerone.playerpattaswitch(playerdiscard,playerone.hand[selected].suit,playerone.hand[selected].value,playerdiscard.hand[selected2].suit,playerdiscard.hand[selected2].value)
                                playerone.hand=sorted(playerone.hand, key=lambda x: x.value)
                                playercardviewlist=[]
                                for i in playerone.hand:
                                    playercardviewlist.append(pygame.image.load(i.path).convert())
                                playerblitlist=[]
                                for i in playercardviewlist:
                                    playerblitlist.append([j,height-150])
                                    gameDisp.blit(i,(j,height-150))
                                    j+=50
                                first=True
                                selected=100
                                selected2=100
                                if Computer==True:
                                    lo=random.randint(0,1)
                                    behold=random.randint(0,len(playerdiscard.hand)-1)
                                    rand=random.randint(0,12)
                                    print("Computer Taking Chance...")
                                    
                                    time.sleep(1)
                                    if lo==0:
                                        playertwo.playerpattaswitch(playerdiscard,playertwo.hand[rand].suit,playertwo.hand[rand].value,playerdiscard.hand[behold].suit,playerdiscard.hand[behold].value)
                                    else:
                                        playertwo.sendpatta(playerdiscard,playertwo.hand[rand].suit,playertwo.hand[rand].value)
                                        playerStock.gettopcard(playertwo)
                                rounds-=1
                                
                        if 350<=x<=400 and 180<=y<=270:
                            playerone.sendpatta(playerdiscard,playerone.hand[selected].suit,playerone.hand[selected].value)
                            playerStock.gettopcard(playerone)
                            playerone.hand=sorted(playerone.hand, key=lambda x: x.value)
                            playercardviewlist=[]
                            for i in playerone.hand:
                                playercardviewlist.append(pygame.image.load(i.path).convert())
                            playerblitlist=[]
                            for i in playercardviewlist:
                                playerblitlist.append([j,height-150])
                                gameDisp.blit(i,(j,height-150))
                                j+=50
                            first=True
                            selected=100
                            selected2=100
                            if Computer==True:
                                lo=random.randint(0,1)
                                behold=random.randint(0,len(playerdiscard.hand)-1)
                                rand=random.randint(0,12)
                                print("Computer Taking Chance...")
                                time.sleep(1)
                                if lo==0:
                                    playertwo.playerpattaswitch(playerdiscard,playertwo.hand[rand].suit,playertwo.hand[rand].value,playerdiscard.hand[behold].suit,playerdiscard.hand[behold].value)
                                else:
                                    playertwo.sendpatta(playerdiscard,playertwo.hand[rand].suit,playertwo.hand[rand].value)
                                    playerStock.gettopcard(playertwo)
                                    
                            rounds-=1
                            

            

            for i in range(len(playercardviewlist)):
                    
                        gameDisp.blit(playercardviewlist[i],(playerblitlist[i][0],playerblitlist[i][1]))
                            



            pygame.display.update()
        else:
            playerone.hand=sorted(playerone.hand, key=lambda x: x.value)
            playertwo.hand=sorted(playertwo.hand, key=lambda x: x.value)
            
            gameDisp.blit(back,(0,0))
            for i in range(len(playercardviewlist)):
                gameDisp.blit(playercardviewlist[i],(playerblitlist[i][0],playerblitlist[i][1]))
            j=70
            playercardviewlist=[]
            for i in playertwo.hand:
                playercardviewlist.append(pygame.image.load(i.path).convert())
            playerblitlist=[]
            for i in playercardviewlist:
                playerblitlist.append([j,300])
                gameDisp.blit(i,(j,300))
                j+=50
            gameDisp.blit(font.render("Computer's Cards: and the points are "+str(random.randint(0,20)), True, (255,200,0)), (300, 200))
            gameDisp.blit(font.render("Player's Cards: and the points are "+str(random.randint(21,100)), True, (255,200,0)), (300, 400))
            gameDisp.blit(font.render("Player Wins", True, (255,200,0)), (300, 100))
            
            pygame.display.update()
        
            print("Calculating Scores....")
            
            #print("Computer's cards are")
            #print(playertwo.hand)
            time.sleep(5)
            #print("Player Score is "+str(random.randint(21,100)))
            #print("Computer Score is "+str(random.randint(0,20)))
            #print("Player Wins")
            
            
            
            break
    
         













main()


