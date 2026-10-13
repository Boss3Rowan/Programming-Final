# HW, MM, CK, 7th, Build a Game


start = input("Would you like to start the game? ").strip().capitalize().lower()
if start == "yes":
    first_choice = input("You start at ucas.\nWould you like to enter the AC, or UVU: ").strip().upper()
elif start == "no":
    print("Okay, Bye.")
else:
     print("Invalid answer.")

if first_choice == "UVU":
    print("As you walk to UVU, you see Marco sprint past.") # Caleb King
    user = input("You walk up to the front desk and see Marco. You ask him why he is there.\nHe says that he works there and asks what your name is: ").strip().capitalize() # Hazel West
    bowling = input(f"Nice to meet you {user}\nWould you like to go bowling?\nYes or No: ").strip().capitalize()
    if bowling == "Yes":
        print("Marco asks for your UVU ID, but you don't have one, so you go back to Ucas.")


elif first_choice == "AC":# Caleb King
    print("You walk into the AC\nEverything seems quiet...\nToo quiet...\nYou listen closely and you hear a faint hiss above you.") # Caleb King
    drop_down = input("Do you look(l) up or do you keep walking(w): ").strip().lower() # Caleb King
    if drop_down == "l": # Caleb King
        user2 = input("As soon as you look up you see a giant spider fall on you...\nYou wake up and see your friend Marco sitting in the corner of the AC\nHe asks what your name is.\nWhat do you tell him: ").strip().capitalize() # Caleb King
        print(f"Well Hiya {user2}")
        story = input("Marco talks about how he saved you from that spider monster\nHe tells you all about his heroic fight and did not stop until his story was finished perfectly.\nHe tells you that he knows a place where we can hide from that hideous monster.\nDo you follow(f) him, or don't(d) follow him")
        
    
#2 Therapy tree --> Hazel
tree = input("After running outside you stop at the Therapy tree.\n Do you want to climb(c) the tree or keep running(r)? ").lower().strip()

if tree == "r":
        print("You run away from the tree and the spider starts chasing you.\n Your too slow; Game over!!!").lower().strip()


print("You climb the tree and find a UVU card. After putting it in your pocket you see the giant spider run up to the base of the tree.\n Good news! The spider can't climb the tree! ")

#3 UVU ---> Hazel
final_choice = input("After waiting for the monster to leave, you get out of the tree.\n Do you want to go to the UVU building(b) or back to class(c)?").lower().strip()
if final_choice == "c":
    print("You run back to the main building and once your in the hall way you hear scrapping noises above you...\n You look up and the spider falls on your face. Game over!!!")

print("Okay, you walk across the street and into the UVU building. You swipe your UVU card and decide to go bowling.\n After a few minmutes of bowling your friend Marco walks in.\n He says hi to you and starts bowling in his own lane.")

adjective = input("You walk up to bowl again and many bowling balls appear.\nTell me an adjective for the bowling ball you picked: ")
print(f"You throw your {adjective} bowling ball and strike it! Good job!\n Then you hear marco").strip()


save = input("Ctrl S")

def choose(prompt, options):
    """Ask until the player enters one of the listed options."""
    answer = input(prompt).strip().lower()
    while answer not in options:
        answer = input(f"Please choose {', '.join(options)}: ").strip().lower()
    return answer


def play_game():
    print("Welcome to the UCAS Adventure!")
    start = choose("Would you like to start the game? (yes/no): ", ["yes", "no"])
    if start == "no":
        print("Okay, bye!")
        return

    location = choose(
        "\nYou start at UCAS. Where do you want to go?\n"
        "Enter AC to visit the Academic Center, or UVU to visit the university: ",
        ["ac", "uvu"],
    )

    if location == "uvu":
        print("\nAs you walk to UVU, you see Marco sprint past.")
        name = input(
            "You ask Marco why he is there. He says he works there and asks your name: "
        ).strip()
        if name:
            print(f"Nice to meet you, {name}!")
        else:
            print("Marco smiles and says, 'Nice to meet you!'")

        tree_choice = choose(
            "\nYou run outside and stop at the Therapy Tree. A giant spider is nearby.\n"
            "Do you want to climb the tree (climb) or keep running (run)? ",
            ["climb", "run"],
        )
        if tree_choice == "run":
            print(
                "\nThe spider chases you, and you can't get away. "
                "You were caught. Game over!"
            )
            return

        print(
            "\nYou climb the tree and find a UVU access card. "
            "The spider climbs after you!"
        )
        final_choice = choose(
            "Do you want to swipe the card at the emergency lab door (swipe) "
            "or jump down and run (run)? ",
            ["swipe", "run"],
        )
        if final_choice == "swipe":
            print(
                "\nThe door opens just in time. You slip inside and lock it, "
                "trapping the spider outside.\n"
                "You escaped and won by using the UVU access card!"
            )
        else:
            print("\nThe spider catches up before you reach safety. Game over!")

    else:
        print(
            "\nYou head to the Academic Center. Marco tells you that a giant "
            "spider is loose nearby."
        )
        ac_choice = choose(
            "Do you want to search the library (library) or cut through the "
            "courtyard (courtyard)? ",
            ["library", "courtyard"],
        )
        if ac_choice == "courtyard":
            print(
                "\nThe spider spots you in the courtyard and chases you. "
                "You can't get away. Game over!"
            )
            return

        print(
            "\nIn the library, you find an emergency radio. Marco tells you "
            "that security can help if you call them."
        )
        final_choice = choose(
            "Do you want to use the radio to call security (radio) or try to "
            "sneak past the spider alone (sneak)? ",
            ["radio", "sneak"],
        )
        if final_choice == "radio":
            print(
                "\nYou call security on the radio. They arrive with Marco and "
                "lead you to safety.\n"
                "You escaped and won by calling for help!"
            )
        else:
            print("\nThe spider sees you sneaking and catches you. Game over!")


if __name__ == "__main__":
    play_game()
