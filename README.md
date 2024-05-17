Card Memory Game

This project is a simple interactive card memory game implemented in Python. Players are dealt a random set of cards and must remember and identify the suits or ranks to earn points. The game is played via the terminal.

Table of Contents
- How It Works(how-it-works)
- Classes
- Functions(functions)
- Usage(#usage)
  - Running the Game(running-the-game)
  - Example Gameplay(example-gameplay)
  - Requirements(requirements)
- License(#license)

How It Works

1. Initialize the Game:
   - The game begins by asking for the number of players.
   - A standard deck of 52 cards is created, consisting of 4 suits (Hearts, Diamonds, Clubs, Spades) and 13 ranks (2-10, Jack, Queen, King, Ace).
   - The deck is shuffled to randomize the order of the cards.

2. Game Rounds:
   - In each round, each player is dealt a random number of cards, ranging from 1 to 5.
   - Players are shown their cards one by one, with a brief delay to help them memorize the cards.
   - After seeing their cards, players are asked to recall either the suits or ranks of their cards in the order they were dealt.
   - Points are awarded based on correct answers:
     - 1 point for each correct suit and 2 points for each correct rank.

3. Continuing or Ending the Game:
   - After each round, players can choose to play another round or end the game.
   - When the game ends, the scores of all players are saved to a file named `scores.txt`.

Classes

Card
- Description: Represents a single card in the deck.
- Attributes: Each card has a suit (Hearts, Diamonds, Clubs, Spades) and a rank (2-10, Jack, Queen, King, Ace).
- Methods: Provides a way to display the card as a string (e.g., "Ace of Spades").

Player
- Description: Represents a player in the game.
- Attributes: Each player has a name, a score that starts at zero, and a list of cards they have been dealt.
- Methods: Initializes the player with a name and tracks their score and cards.

Functions

play_game
- Description: The main function that runs the game.
- Flow:
  - Initializes and shuffles the deck of cards.
  - Prompts the user to input the number of players.
  - Creates player objects for each participant.
  - Enters a loop to manage game rounds:
    - Deals cards to each player and displays them with a delay.
    - Asks players to recall the suits or ranks of their cards.
    - Checks the players' answers and updates their scores based on correct responses.
    - Prompts players to decide whether to play another round or end the game.
  - Upon ending the game, saves the final scores to `scores.txt`.

Usage

Running the Game
To play the game, you need to run the script in a Python environment. Make sure you have Python installed on your system.

1. Open a terminal or command prompt.
2. Navigate to the directory containing the game script.
3. Run the script using Python:
   ```sh
   python card_memory_game.py

MIT License

Copyright (c) 2024 Michael Melaku

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
