import random


class China:
    print("\t\t\tRock-Paper-Scissors Game")
    print("To play the game, input R for Rock,  P for Paper, or S for Scissors")

    def main(self):

        option = ['R', 'P', 'S']

        player_choice = input("Enter your choice: ")
        player_choice = player_choice.upper()

        # The player will be continually prompted provided his/her input is not in the option
        while player_choice not in option:
            print('*Error* \nchoice not in options ')
            player_choice = input("re-enter your choice: ")
            player_choice = player_choice.upper()

        self.convert_and_play(player_choice)  # passes the player's input as argument

    def convert_and_play(self, value):

        options = ['Rock', 'Paper', 'Scissors']

        COM_choice = random.choice(options)  # This sets the CPU's choice

        # Converting the player's choice from a single character to its equivalent in the options list
        player_choice = value

        if player_choice == 'R':
            player_choice = options[0]

        elif player_choice == 'P':
            player_choice = options[1]

        elif player_choice == 'S':
            player_choice = options[2]

        #  After conversion, the play_game function is called, and accepts the player and CPU choices as arguments
        self.play_game(player_choice, COM_choice)

    def play_game(self, player, com):
        print(f"\nPlayer({player}): CPU({com})\n")

        # The main logic of the game
        if \
                        (player == 'Rock' and com == 'Scissors') or \
                        (player == 'Scissors' and com == 'Paper') or \
                        (player == 'Paper' and com == 'Rock'):
            return print("Winner: Player")
        elif \
                        (com == 'Rock' and player == 'Scissors') or \
                        (com == 'Scissors' and player == 'Paper') or \
                        (com == 'Paper' and player == 'Rock'):
            return print("Winner: CPU")

        elif player == com:
            print("it's a Tie \nPlay again")
            return self.main()


bob = China()  # Create an instance of the Class

bob.main()  # Execute the game
