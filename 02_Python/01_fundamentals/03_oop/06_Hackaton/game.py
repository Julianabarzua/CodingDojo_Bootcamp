from classes.deck import Deck
import random

bicycle = Deck()

class player:
    def __init__(self, name, numb_of_cards):
        self. name = name
        self.hand = random.sample(bicycle.cards,numb_of_cards)
        self.points = 0
        self.play_card = []



class game:
    def __init__(self):
        self.players = []

    def startGame(self):
        p1_name = input("Add player 1 name: ")
        p2_name = input("Add player 2 name: ")
        p1 = player(p1_name,5)
        p2 = player(p2_name,5)
        self.players.append(p1)
        self.players.append(p2)

    def turn(self):
        
        self.players[0].play_card = []
        self.players[1].play_card = []
        
        for player in self.players:

            print(f"\n{player.name} cards:")
            for i in range (len(player.hand)):
                print(f"0{i+1} - {player.hand[i].string_val} of {player.hand[i].suit} : {player.hand[i].point_val} points")
            key = int(input("Select your card to play (01-05): "))
            player.play_card.append(player.hand[key-1])
            player.hand.pop(key-1)
            
        
        
        if self.players[0].play_card[0].point_val > self.players[1].play_card[0].point_val:
            print(f"\n{self.players[0].name} won the turn")
            self.players[0].points += 1

        elif self.players[0].play_card[0].point_val < self.players[1].play_card[0].point_val:
            print(f"\n{self.players[1].name} won the turn")
            self.players[1].points += 1
        else:
            print("Its a tie")

        print(f"\n{self.players[0].name} points: {self.players[0].points} ")
        print(f"{self.players[1].name} points: {self.players[1].points} ")

    def gameEnd(self):
        if self.players[0].points > self.players[1].points :
            print(f"\n{self.players[0].name} IS THE WINNER!!!!")
        
        elif self.players[0].points < self.players[1].points :
            print(f"\n{self.players[1].name} IS THE WINNER!!!!")

        else:
            print ("ITS A TIE!!!!")




game1 = game()

game1.startGame()

for x in range(5):
    game1.turn()

game1.gameEnd()











