import time
import random

boss_list = ["Handsome Cyborg", "Very Elderly Evil Space Cat",
             "Super Swol Grandma", "Space Gecko", "Sentient Cabbage",
             "Goldfish You Flushed Last Week"]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def play_again():
    play_again = input("1. Yes\n"
                       "2. No\n")
    if play_again == '1':
        play_game()
    elif play_again == '2':
        print_pause("Thanks for playing! Goodbye!")
        quit()
    else:
        ("Please Enter Valid Input")
    play_again()


def intro():
    global boss
    boss = random.choice(boss_list)
    print_pause("You fall out of a newly emptied cryostasis pod.\n")
    print_pause("Red emergency lights are flashing and a siren is blaring.\n")
    print_pause("Your head is still spinning when you hear a voice"
                " come through the intercom.\n")
    print_pause(f"Captain, we are under attack by a {boss}!"
                " and need you now.\n")
    print_pause("As the world around you comes back into focus you notice"
                " a locker on your left has popped open.\n")
    print_pause("Straight ahead of you there is the door leading"
                " out to the main coridor of the ship.\n")


def wake_up(items):
    print_pause("Would you like to open the locker or leave the room?\n")
    choice1 = input("1. locker\n"
                    "2. leave room\n")

    if choice1 == '1':
        print_pause("You head over to the locker and open it up.\n")
        if "Uniform" in items:
            print_pause("You already got the uniform out of the locker.\n"
                        "There is nothing else in the locker.\n")
            wake_up(items)
        else:
            print_pause("You find a uniform with your name on it.\n")
            print_pause("You put it on, it brings out your eyes.\n")
            print_pause("More importantly you are no longer naked"
                        " on a space ship.\n")
            items.append("Uniform")
            wake_up(items)
    elif choice1 == '2':
        print_pause("You open the door leading to"
                    " the main coridor of the ship\n")
        if "Uniform" in items:
            print_pause("As you step through the door way"
                        " you are engulfed in a freezing mist\n")
            print_pause("Luckily you are wearing your uniform with"
                        " seat warmer tech built in\n")
        else:
            print_pause("You step out into the coridor completely naked"
                        " and are engulfed in a freezing mist\n")
            print_pause("If only you remembered to get dressed"
                        " before leaving the room\n")
            print_pause("That's the third time that you've been frozen"
                        " naked in the hallway this week\n")
            print_pause("Game Over. Would you like to play again?\n")
            play_again()
    else:
        print_pause("Please enter valid input.")
        wake_up(items)


def bridge(items):
    print_pause("Looking around you see the ship has"
                " taken significant damage\n")
    print_pause("You see a door labeled 'Security' at one end"
                " of the coridor.\n")
    print_pause("At the other end you see a door titled 'Main Bridge.'\n")
    choice2 = input("1. Security\n"
                    "2. Main Bridge\n")
    if choice2 == '1':
        print_pause("You open up the door to security expecting to"
                    " find it empty.\n")
        if "Blaster" in items:
            print_pause("The security guard still hasn't noticed you.\n")
            print_pause("There is nothing else of use to you in this room.\n")
            bridge(items)
        else:
            print_pause("To your surprise there is a security guard with her"
                        " legs kicked up on the console.\n")
            print_pause("She is talking loudly on her holo-phone and hasn't"
                        " noticed the ship is under attack.\n"
                        "You grab a blaster hanging on the wall and head"
                        " back into the corridor.\n")
            items.append("Blaster")
            bridge(items)
    elif choice2 == '2':
        print_pause("You open the door to the Main Bridge.\n")
        if "Blaster" in items:
            print_pause(f"{boss} is holding your crew hostage and forcing"
                        " them to play 'go fish.'\n")
            print_pause("Everyone looks to you as you enter the room"
                        " blaster in hand.\n")
            print_pause(f"{boss} drops the deck of cards and"
                        " makes a run for it.\n")
            print_pause("Everyone ducks for cover as you fire off"
                        " a couple of shots.\n")
            print_pause("One shot even managed to singe the"
                        " butt of your target.\n")
            print_pause(f"The crew breathes a sigh of relief as {boss}"
                        " flies away on their ship.\n")
            print_pause("Congratulatons! You have won the game."
                        " Would you like to play again?\n")
            play_again()
        else:
            fight(items)

    else:
        print_pause("Please Enter Valid Input.")
        bridge(items)


def fight(items):
    print_pause(f"{boss} looks up from an intense game of go fish that he"
                " is forcing your crew to play.\n")
    print_pause("He see's that you are unarmed and a wicked smirk"
                " appears on his face")
    print_pause(f"{boss} begins walking towards you.")
    choice3 = input("1. Fight\n"
                    "2. Run\n")
    if choice3 == '1':
        print_pause(f"{boss} easily overpowers you and forces"
                    " you to join the game.\n")
        print_pause("You and your crew live out your remaining days"
                    " playing the most boring game ever created.\n")
        print_pause("Game Over. Would you like to play again?")
        play_again()
    elif choice3 == '2':
        print_pause("You book it out of there at light speed and find youself"
                    " back in the main coridor.\n")
        bridge(items)
    else:
        print_pause("Please Enter Valid Input.")
        fight(items)


def play_game():
    items = []
    intro()
    wake_up(items)
    bridge(items)
    fight(items)


play_game()
