import random

total_life=10
word_list=["Apple" ,"Monster" ,"Academy" ,"Sugar" ,"Salt" ,"Korea" ,"English" ,"Mouse" ,"Keyboard" ,"Cup" ,"Line" ,"Camera" ,"Time" ,"Clock" ,"Number" ,"Strength" ,"Weak" ,"Dog" ,"Stack" ,"Book" ,"Tissue" ,"Words" ,"Hangman" ,"Wing" ,"Thunder" ,"Rain" ,"Say" ,"Brian" ,"Glue" ,"Crab" ,"Squid" ,"Closet" ,"Star" ,"Moon" ,"Pillow"]
answer_index=random.randint(0,len(word_list)-1)
answer_list=list(word_list[answer_index])
game_list=[]
input_list=[]

for count in range(len(answer_list)):
    game_list.append("_")

while True:
    print("What? : ",end="")
    for alpha in game_list:
        print(alpha," ",end="")
    print()
    
    #input any alphabet and check
    print("Your life : ",str(total_life))
    while True:
        whatis=input("input alphabet: ")
        if len(whatis) != 1:
            print("only one alphabet please")
        elif input_list.count(whatis) > 0:
            print("already did it")
        else:
            input_list.append(whatis)
            break
    
    #alphabet check
    check_point=0
    for check in range(0,len(answer_list)):
        if whatis==answer_list[check]:
            game_list[check]=whatis
            check_point=check_point+1
        
    #life check
    if check_point > 0:
        print("Correct!\n")
        
    else:
        print("Oh no\n")
        total_life=total_life-1

    #end game?
    if game_list.count("_") == 0:
        print("** Clear **")
        break

    if total_life==0:
        print("** Die **")
        break

    

    
            

