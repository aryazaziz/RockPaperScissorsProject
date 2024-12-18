import random

def action():
    
    user_count = 0
    comp_count = 0
    
    while comp_count < 3 and user_count <3:
        user_choice = input("first to reach 3 points wins.\nwhat is your choice? r) for rock, p) for paper, s) for scissors:\n")
        comp_choice = random.choice(["r", "p", "s"])

        print(f"the computer has chose: {comp_choice}")
       
        if user_choice == comp_choice: 
             user_choice = input("the result is a draw and no points will be added on,\n try again:\n")


        elif (user_choice == "r" and comp_choice == "s") or \
             (user_choice == "s" and comp_choice == "p") or \
             (user_choice == "p" and comp_choice == "r"):
            print("the user has won this round gaining a point!")
            user_count += 1
            print(f"computer has {comp_count} points, user has {user_count} points")


        
        elif (user_choice == "s" and comp_choice == "r") or \
             (user_choice == "p" and comp_choice == "s") or \
             (user_choice == "r" and comp_choice == "p"):
            print("the computer has won this round gaining a point!")
            comp_count += 1
            print(f"computer has {comp_count} points, user has {user_count} points")
    
    if user_count > comp_count:
        print("well done, you have beat the computer.")

    elif user_count < comp_count:
        print("the computer has won.")


action()