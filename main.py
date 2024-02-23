import random
from art import logo
import os

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
print(logo)
def deal_card():
    """This will return a random card number"""    
    card_numbers= [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(card_numbers)
    return card
def calculate_score(cards):
    """Takes cards and returns score of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack"
    elif user_score == 0:
        return "YOu Win"
    elif computer_score > 21:
        return "Opponent went Over, they lose, you win"
    elif user_score > 21:
        return "You went over, Opponent won"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():   
    user_card = []
    computer_card = []
    game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            go_again = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if go_again == 'y':
                user_card.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Start Game(y/n)?: ").lower() == "y":
    clear_console()
    play_game()


