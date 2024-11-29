def hangman():
    print("Let's Play Hangman")
    print("Hint: This movie title means ""Crown""in English.It’s a 1989 film starring Mohanlal and is well-known for its emotional depth.")
    # while film==name
    film1=[]
    film=["k","i","r","e","e","d","a","m"]
    print(f"you have {len(film)} digits ")
    for i in range(len(film)):
        film1+="_"
    print(film1)
    print("\nenter the letters")
    lives=6
    over=False

    while not over:
        if lives==0:
            exit        
        else:
            guessed_letter=input("enter guess letter\n").lower()
            for i in range(len(film)):
                letter=film[i]
                if letter==guessed_letter:
                    film1[i]=guessed_letter
                    print("guess is correct")
            
            print(film1)
            if guessed_letter not in film:
                print("guess is not correct")
                lives-=1
                print(f"{lives} chances left")  
                if lives==0:
                    print("you lose")
                    exit
            if '_' not in film1:
                print("you win the game")
                over=True
        
    
hangman()


        