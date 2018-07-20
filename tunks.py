# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:18:48 2018

@author: kopur
"""

import deckOfCards as dc
import sys

# Evaluate scores of players hands and add to palyers scores
def evaluate(deck_size, player_hands, player_points, tunk_caller):
    hand_sum = []
    for x in range(len(player_hands)):
        hand_sum.append(player_hands[x].value())
        print("Player " + str(x) + " has a point value of " + str(hand_sum[x]))
    if deck_size == 0:
        print("The deck ran out! The person with the lowest value is the loser!")
        print("Player " + str(hand_sum.index(min(hand_sum))) + " lost!")
        player_points[hand_sum.index(min(hand_sum))] += 40
    elif min(hand_sum) == hand_sum[tunk_caller]:
        print("Player " + str(tunk_caller) + " won!")
        hand_sum[tunk_caller] == 0
        player_points = [player_points[x] + hand_sum[x] for x in range(len(hand_sum))]
    else: 
        print("Player " + str(tunk_caller) + " was wrong :c")
        player_points[tunk_caller] += 40
    for index, elem in enumerate(player_points):
            print("Player " + str(index) + "'s total points is " + str(elem))
    return player_points, -1
        
# Print brief overview of the game.
def get_instructions():
    print("""You can use the following commands: 
        exit: quit the game 
        show: display the cards in your hand
        sort: sort the cards in hand by rank
        tunks: see if your hand has the lowest value!
        garbage: see the top card of the garbage
        If you want to select cards, enter the position number they appear in your hand separated by spaces. (1-indexed)""")

# Checks to see if selected cards are valid!
def check_cards(player_hand, command):
    try:
        command = command.split(" ")
        index = []
        card_val = []

        for x in command:
            index.append(int(x)-1)

        for y in index:
            card_val.append(player_hand[y].rank)

        if len(set(card_val)) > 1:
            print("Selected cards have different values")
            return False
        return True

    except Exception as e:
        print("Selected cards break rules.")
        return False

# Obtain user input and check if command is legitimate input, then execute
def get_input(player_num, player_hands, garbage, deck):
    valid = False
    while not valid:
#        try:
            command = input("What would you like to do? ")

            if command == "show":
                player_hands[player_num].show()

            elif command == "sort":
                player_hands[player_num].sort()
                player_hands[player_num].show()

            elif command == "exit":
                print("Thanks for playing! To start another game enter \"game()\"")
                sys.exit()

            elif command == "tunks":
                return None, None, None

            elif command == "garbage":
                garbage.top().name()

            elif check_cards(player_hands[player_num], command):
                command = [int(x)-1 for x in command.split(" ")]
                draw = input("Pick up from deck or garbage? ")
                dealt = player_hands[player_num].play(command)

                if draw == 'deck':
                    player_hands[player_num].append(dc.Set(deck.flip()))
                    garbage.append(dealt)

                else:
                    player_hands[player_num].append(dc.Set(garbage.top()))
                    garbage.append(dealt)
                
                print("Player " + str(player_num) + " dealt the following:")
                dealt.show()
                print("Player drew from the " + draw)
                return player_hands, garbage, deck

            else:
                get_instructions()

#        except Exception as e:
#            print("This is not a valid move, please try again!")
#            print(e)
#            
            
def main():
    # Setup game
    print("Welcome to tunks!")
    print("How many players do you want in your game? ")
    number_players = input("Please enter the number of players playing this game. ")

    while (not isinstance(int(number_players), int)) and (int(number_players) > 1):
        number_players = ("That is not a number greater than 1. Please try again.") 
    
    
    player_points = [0]*int(number_players)
    tunk_caller = -1
    
    while max(player_points) < 200:
        deck = dc.Deck(False)
        deck.shuffle()
        player_hands = [deck.deal(5) for x in range(int(number_players))]
        garbage = dc.Set([deck.flip()])
        print("A new round begins!")
        get_instructions()

        while deck.size() > 0:  
            round_done = False
            for x in range(int(number_players)):
                h, g, d = get_input(x, player_hands, garbage, deck)
                if h is None:
                    round_done = True
                    tunk_caller = x
                    break
                player_hands = h
                garbage = g
                deck = d
            if round_done:
                break
        player_points, tunk_caller = evaluate(deck.size(), player_hands, player_points, tunk_caller)
    
        
if __name__ == "__main__":
     main()