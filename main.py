from random import randint
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_shuffles():
    current_cards=[]
    
    for i in range(2):
        index=randint(0,len(cards)-1)
        current_cards+=[cards[index]]
        
    return current_cards

def extra_cards():
    index=randint(0,len(cards)-1)
    extra_card=cards[index]
    return extra_card
    

def new_game():
    
    play=input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()[0]
    
    if play=="n":
        print("\nSee you soon!\n")
    elif play=="y":
        clear()
        # print(logo)
        
        user_cards=card_shuffles()
        com_cards=card_shuffles()
        
        def user_score_counter():  
            user_score=0
            user_aces=0
            for i in user_cards:
                if i==11:
                    user_aces+=1
                user_score+=i
            if user_score>21 and user_aces!=0:
                user_score-=10
            return user_score
        user_score=user_score_counter() 
        
        def com_score_counter():
            com_aces=0
            com_score=0
            for i in com_cards:
                if i==11:
                    com_aces+=1
                com_score+=i
            if com_score>21 and com_aces!=0:
                com_score-=10
            return com_score
        com_score=com_score_counter() 
        
        print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {com_cards[0]}")
        
        if com_score==21:
            print(logo)
            print(f"\nyour final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {com_cards}, final score: {com_score}")
            print("\nYou lose! Computer has a Blackjack!")
            new_game()
        elif user_score==21:
            print(logo)
            print(f"\nyour final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {com_cards}, final score: {com_score}")
            print("\nYou won! It's a Blackjack!")
            new_game()
        else:
            add_card=True
            while add_card:
                add_another=input("Type 'y' to get another card, or type 'n' to pass: ").lower()[0]
                if add_another=="y":
                    user_cards.append(extra_cards())
                    user_score=user_score_counter()
                    if user_score>21:
                        print(f"\nyour final hand: {user_cards}, final score: {user_score}")
                        print(f"Computer's final hand: {com_cards}, final score: {com_score}") 
                        print("\nYou went over 21! Computer won!")
                        add_card=False
                        new_game()
                    elif user_score==21 and com_score!=21:
                        print(logo)
                        print(f"\nyour final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {com_cards}, final score: {com_score}")
                        print("\nYou won! It's a Blackjack!")
                        add_card=False
                        new_game()
                    else:
                        print(f"Your cards: {user_cards}, current score: {user_score}")
                        print(f"Computer's first card: {com_cards[0]}")
                        add_card=True
                elif add_another=="n":
                    while com_score<16:
                        com_cards.append(extra_cards())
                        com_score=com_score_counter()
            
                    print(f"\nyour final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {com_cards}, final score: {com_score}")
                    if com_score>21:
                        print("\nComputer went over 21! You won!")
                        
                    elif com_score==21 and user_score!=21:
                        print(logo)
                        print("\nYou lose! Computer has a Blackjack!")
                        
                    elif com_score>user_score:
                        print("\nYou lose! Computer scored higher!")
                        
                    elif com_score<user_score:
                        print("\nYou won!")
                        
                    else:
                        print("\nIt's a draw!")
                    add_card=False
                    new_game()
                else:
                    print("Wrong input! Please type 'y' or 'n'")
                    add_card=True
    
    else:
        print("Wrong Command! Please enter 'y' or 'n'")
        new_game()
new_game()
