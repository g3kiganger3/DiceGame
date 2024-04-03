import random
play_again = True
def main():
    print ("Welcome to the Dice Game!")
    player_count_and_rolls()
    if new_game() is not True:
        exit()

def dice_total(dice_count):
    roll = 0
    total_roll = 0
    for dice in range(dice_count):
        dice_roll = random.randint(1,6)
        total_roll = total_roll + dice_roll
        print(f"Roll {dice + 1}: {dice_roll}")
    return total_roll

def winner(player_totals):
    high_score = 0
    tie = 0
    winner = str()
    tied_players = []
    for players,totals in player_totals.items():
        if totals > high_score:
            high_score = totals
            winner = players
        elif totals == high_score:
            tie += 1
    for players,totals in player_totals.items():
        if high_score == totals:
            tied_players.append(players)           
    if tie <= 1:
        print(f"{winner} Wins!")
    else:
        winner = ", ".join(tied_players)
        print(f"{winner} Tied!")
#need to add some input exception handling
def player_count_and_rolls():
    player_list = []
    player_totals = {}
    total_players = int(input("How many players?: "))
    for players in range(total_players):
        player = (input(f"Player {players + 1} Name:"))
        player_list.append(player)
    dice_count = int(input("How many dice rolls?: "))
    for players in player_list:
        print(f"{players}'s Rolls:")
        player_totals[players] = dice_total(dice_count)
        print(f"{players} Total: {player_totals[players]}")
    winner(player_totals)

def new_game():
    new_game = input("Would you like to play again?").lower()
    if (new_game == "y") or (new_game == "yes"):
        play_again = True
        return True
    else:
        return False 

while play_again:
    main()

