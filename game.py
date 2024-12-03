'''Author:Diya krishna
version 1.1
DATE:3/12/2024'''
def stick_game():
    print("Welcome! to stick game ")
    print("Rules of the game are :you can pick 1,2 & 3 in one turn AND player who picks last stick will lose")
    person1=input("Enter name of first player:")
    person2=input("Enter second player name:")
    print("game started")
    sticks=int(input("Enter the number of sticks :"))
    remaining_sticks=sticks
    if (remaining_sticks) <=0:
            print("You lose")
    else:
        while person1:
            take=int(input(f"{person1} Enter your choice from 1,2 or 3:"))
            remaining_sticks = remaining_sticks-take
            print("no of remaining_sticks are", remaining_sticks)
            while person2:
                take = int(input(f"{person2} Enter your choice from 1,2 or 3:"))
                remaining_sticks = remaining_sticks - take
                print("no of remaining_sticks are", remaining_sticks)
            break
stick_game()