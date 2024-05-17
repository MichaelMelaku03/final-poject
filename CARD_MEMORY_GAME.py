import random
import time

# Defining the list of card suits and ranks
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_ranks = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.cards = []

def play_game():
    # Initializing the deck and shuffle the cards
    deck = [Card(su, ra) for su in card_suits for ra in card_ranks]
    random.shuffle(deck)

    # Get the number of players
    num_players = int(input("How many players? "))

    # Creating the players
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    while True:
        print("\nNew Round!")

        # Deal a variable number of cards to each player
        num_cards = random.randint(1, 5)
        for player in players:
            player.cards = [deck.pop() for _ in range(num_cards)]
            print(f"{player.name} has the following cards:")
            for card in player.cards:
                print(card)
                time.sleep(2)  # Display each card for 2 seconds

            # Ask the players to identify the suit or rank
            question_type = random.choice(['suit', 'rank'])
            answers = input(f"{player.name}, what are the {question_type}s of your cards in the order they were dealt? ").split()

            # Check if the user answered correctly
            correct_answers = [getattr(card, question_type) for card in player.cards]
            points = sum(answer == correct_answer for answer, correct_answer in zip(answers, correct_answers))
            if question_type == 'rank':
                points *= 2  # Ranks are worth double points
            player.score += points

            print(f"{player.name}'s current score: {player.score}")

        again = input("Play another round? (y/n) ")
        if again.lower() != 'y':
            break

    # Save scores
    with open('scores.txt', 'w') as f:
        for player in players:
            f.write(f"{player.name}: {player.score}\n")

if __name__ == "__main__":
    play_game()