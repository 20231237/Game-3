#filename : CS112_A1_T2_GameNumber3_20231237

# Purpose:  it’s a game cosist of number of coins non sqirel may be random number between 100and500 or number between 10to1000 you choose and two players each of them remove non-zero squire number the player who remove the last coin is the winner

# Author: Radwa Ashraf Nagah rashed

# ID: 20231237
import math
import random

def valid_moves(n):
    moves = []
    i = 1
    while i*i <= n:
        moves.append(i*i)
        i += 1
    return moves

def player_move(player, coins):
    print(f"\nPlayer {player}'s turn:")
    print(f"Coins left: {coins}")

    while True:
        move_input = input("Enter the number of coins you want to remove: ")

        # Check if the input is a digit
        if not move_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        move = int(move_input)

        # Check if the move is valid
        if move in valid_moves(coins):
            coins -= move
            return coins
        else:
            print("Invalid move. Choose a non-zero square number less than or equal to coins left.")

def is_square(num):
    return math.isqrt(num)**2 == num

def identify_square(variable):
    if is_square(variable):
        print(f"{variable} is a square number.")
    else:
        print(f"{variable} is not a square number.")

def main():
    choice = input("Choose the initial number of coins: '1' for between 10 and 1000, '2' for a random number between 100 and 500: ")

    while choice not in ['1', '2']:
        print("Invalid choice. Please enter '1' or '2'.")
        choice = input("Choose the initial number of coins: '1' for between 10 and 1000, '2' for a random number between 100 and 500: ")

    if choice == '1':
        while True:
            coins_input = input("Enter the initial number of coins in the pile (between 10 and 1000): ")

            # Check if the input is a digit
            if not coins_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            coins = int(coins_input)

            if 10 <= coins <= 1000:
                break
            else:
                print("Invalid input. Please enter a number between 10 and 1000.")
    elif choice == '2':
        coins = random.randint(100, 500)
        print(f"Randomly generated initial number of coins: {coins}")

    while is_square(coins):
        print("Invalid input. Please enter a non-square number of coins.")
        coins_input = input("Enter the initial number of coins in the pile: ")

        # Check if the input is a digit
        if not coins_input.isdigit():
            print("Invalid input. Please enter a number.")
            return

        coins = int(coins_input)

    player = 1

    while coins > 0:
        coins = player_move(player, coins)
        if coins == 0:
            print(f"\nPlayer {player} wins!")
            break
        player = 1 if player == 2 else 2

