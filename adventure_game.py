import random
import time
import sys

# ANSI escape codes for text formatting
class TextStyle:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PURPLE = "\033[95m"
    BLUE = "\033[0;34m"
    PINK = "\033[35m"

# Define the attack data with rarity levels and their ranges
attacks = {
    "common": {"min": 10, "max": 20},
    "rare": {"min": 20, "max": 30},
    "epic": {"min": 30, "max": 40},
    "legendary": {"min": 40, "max": 50}
}

# Define the probabilities for each rarity level
rarities = ["common", "rare", "epic", "legendary"]
rarities_probabilities = [0.6, 0.25, 0.1, 0.05]

def display_intro():
    print(TextStyle.BOLD + "Welcome to The Enchanted Realm!" + TextStyle.RESET)
    print("You find yourself standing at the entrance of a mystical forest.")
    print(f"Your mission is to rescue the kidnapped {TextStyle.PINK}PRINCESS{TextStyle.RESET} and restore balance to the realm.")
    print("Choose your path wisely, for your destiny awaits!")
    print("\n" + "-" * 60)

def get_player_name():
    while True:
        name = input("Enter your character's name: ").strip()  # Strip leading/trailing whitespace
        if name:
            return name
        else:
            print(f"{TextStyle.RED}Please enter a valid name.")

def generate_random_enemy():
    enemies = ["Goblin", "Witch", "Troll", "Dragon Jr", "Zombie", "Skeleton King", "Satan", "Joker"]
    return random.choice(enemies)

def choose_attack(player_attack_bonus=0):
    input("Press Enter to determine your attack rarity...")

    # Randomly select the rarity level based on probabilities
    rarity = random.choices(rarities, rarities_probabilities)[0]

    # Get the attack values based on rarity
    attack_range = attacks[rarity]

    # Randomly select an attack value within the range
    attack_value = random.randint(attack_range["min"], attack_range["max"]) + player_attack_bonus

    print(f"You got {TextStyle.BOLD}{rarity}{TextStyle.RESET} attack")

    return attack_value, rarity

def display_health(player_name, player_health, enemy, enemy_health):
    print(f"{TextStyle.GREEN}{player_name}'s Health: {max(player_health, 0)}{TextStyle.RESET}")
    print(f"{TextStyle.YELLOW}{enemy}'s Health: {max(enemy_health, 0)}{TextStyle.RESET}")

def battle(player_name, is_final_battle=False, player_attack_bonus=0):
    if not is_final_battle:
        enemy = generate_random_enemy()
        print(f"A wild {TextStyle.RED}{enemy}{TextStyle.RESET} appears!")
        print(f"{TextStyle.GREEN}Prepare for battle!{TextStyle.RESET}")
        print("\n" + "-" * 60)

        player_health = 100
        enemy_health = 100

        while player_health > 0 and enemy_health > 0:
            player_attack, player_attack_rarity = choose_attack(player_attack_bonus)
            enemy_attack = random.randint(10, 20)

            print(f"{TextStyle.BOLD}{player_name}{TextStyle.RESET} attacks {TextStyle.RED}{enemy}{TextStyle.RESET} with a {TextStyle.BOLD}{player_attack_rarity}{TextStyle.RESET} attack for {player_attack} damage!")
            enemy_health -= player_attack
            time.sleep(1)

            if enemy_health <= 0:
                enemy_health = 0
                break

            print(f"{TextStyle.RED}{enemy}{TextStyle.RESET} attacks {TextStyle.BOLD}{player_name}{TextStyle.RESET} for {enemy_attack} damage!")
            player_health -= enemy_attack
            time.sleep(1)

            if player_health <= 0:
                player_health = 0

            display_health(player_name, player_health, enemy, enemy_health)

            if player_health <= 0:
                print("You have been defeated. Game over.")
                while True:
                    play_again = input("Don't lose your heart, Let's try again!! (yes/no): ").strip().lower()
                    if play_again == "yes":
                        start_game()
                        return
                    elif play_again == "no":
                        sys.exit()
                    else:
                        print(f"{TextStyle.RED}Invalid input. Please enter 'yes' or 'no'.")

        else:
            print("\n" + "-" * 60)
            print(f"You have defeated the {TextStyle.RED}{enemy}{TextStyle.RESET}! Congratulations!")

    else:
        player_health = 100
        dragon_health = 100

        while player_health > 0 and dragon_health > 0:
            player_attack, player_attack_rarity = choose_attack(player_attack_bonus)
            dragon_attack = random.randint(20, 30)

            print(f"{TextStyle.BOLD}{player_name}{TextStyle.RESET} attacks the {TextStyle.RED}Dragon{TextStyle.RESET} with a {TextStyle.BOLD}{player_attack_rarity}{TextStyle.RESET} attack for {player_attack} damage!")
            dragon_health -= player_attack
            time.sleep(1)

            if dragon_health <= 0:
                dragon_health = 0
                break

            print(f"The {TextStyle.RED}Dragon{TextStyle.RESET} attacks {TextStyle.BOLD}{player_name}{TextStyle.RESET} for {dragon_attack} damage!")
            player_health -= dragon_attack
            time.sleep(1)

            if player_health <= 0:
                player_health = 0

            display_health(player_name, player_health, "Dragon", dragon_health)

        if player_health <= 0:
            print("\n" + "-" * 60)
            print(f"The {TextStyle.RED}Dragon{TextStyle.RESET} has defeated you. Game over.")
            while True:
                play_again = input("Don't lose your heart, Let's try again!! (yes/no): ").strip().lower()  # Strip and convert to lowercase
                if play_again == "yes":
                    start_game()
                    return
                elif play_again == "no":
                    sys.exit()
                else:
                    print(f"{TextStyle.RED}Invalid input. Please enter 'yes' or 'no'.")
                    print("\n" + "-" * 60)

        else:
            print("\n" + "-" * 60)
            print(f"Congratulations! You have defeated the {TextStyle.RED}Dragon{TextStyle.RESET} and retrieved the Crystal of Power!")
            print(f"You have saved The {TextStyle.PINK}PRINCESS{TextStyle.RESET} and {TextStyle.GREEN}Enchanted Realm.")
            print(f"THANK YOU for your Valour and Kindness{TextStyle.RESET}")
            print("\n" + "-" * 60)
            time.sleep(1)
            play_again = input("Would you like to Play again? (yes/no): ").strip().lower()  # Strip and convert to lowercase
            if play_again == "yes":
                start_game()
                return
            elif play_again == "no":
                sys.exit()
            else:
                print(f"{TextStyle.RED}Invalid input. Please enter 'yes' or 'no'.{TextStyle.RESET}")
                print("\n" + "-" * 60)

def explore_forest(player_name):
    print(f"{TextStyle.BOLD}{player_name}{TextStyle.RESET}, you enter the mystical forest.")
    print("As you venture deeper, you encounter a fork in the path.")
    print("Which path will you choose?")
    print("\n" + "-" * 60)

    while True:
        path = input("Enter 'left' or 'right': ").strip().lower()  # Strip and convert to lowercase
        print("\n" + "-" * 60)

        if path == "left":
            encounter_chance = random.random()  # Random number between 0 and 1
            if encounter_chance <= 0.3:
                print("You follow the left path and encounter a group of hostile creatures!")
                battle(player_name)
            else:
                print("You follow the left path and continue your journey.")
                print("As you explore further, you find a powerful sword.")
                print(f"{TextStyle.BLUE}You equip the sword and gain +5 attack power!{TextStyle.RESET}")
                time.sleep(1)
                print("\n" + "-" * 60)
                return True
        elif path == "right":
            print("You choose the right path and encounter a group of hostile creatures!")
            battle(player_name)
        else:
            print(f"{TextStyle.RED}Invalid choice. Please enter 'left' or 'right'.{TextStyle.RESET}")

def visit_village(player_name):
    print(f"Welcome to the peaceful village, {TextStyle.BOLD}{player_name}{TextStyle.RESET}!")
    print("The villagers are grateful for your bravery.")
    print("They offer you a food and shelter.")
    print(f"To repay them for their kindness you have decided to go to {TextStyle.RED}{TextStyle.BOLD}DRAGON'S CAVE{TextStyle.RESET} and rescue the {TextStyle.PINK}PRINCESS")
    print("\n" + "-" * 60)
    time.sleep(2)

def final_battle(player_name, player_attack_bonus=0):
    print(f"{TextStyle.BOLD}{player_name}{TextStyle.RESET}, you have reached the final destination.")
    print(f"Before you stands the fearsome {TextStyle.RED}Dragon of Darkness{TextStyle.RESET}.")
    print("Prepare yourself for the ultimate battle!")
    print("\n" + "-" * 60)

    battle(player_name, is_final_battle=True, player_attack_bonus=player_attack_bonus)

def start_game():
    display_intro()
    player_name = get_player_name()
    sword_bonus = explore_forest(player_name)
    visit_village(player_name)
    final_battle(player_name, player_attack_bonus=5 if sword_bonus else 0)

start_game()
