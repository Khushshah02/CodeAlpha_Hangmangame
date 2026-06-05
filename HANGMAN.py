import random


def wordhardprediction3():
    wordlist=["cat","mat","hat","rat","dog"]
    word=random.choice(wordlist)
    print(word[0]+" _"+" _")
    for i in range(4):
        letter2=input("Predict 2nd letter:")
        if(letter2==word[1]):
            print(word[0]+letter2+" _")
            break
        else:
            print("INCORRECT!Try Again")
            if i==3:
                print("GAME OVER!")
                return
    print("This is a 3 letter word predict 3rd letter")
    for i in range(4):
        letter3=input("predict 3rd letter:")
        if(letter3==word[2]):
            print(word[0]+letter2+letter3)
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+word[1]+" _")
            if i==3:
                print("GAME OVER!")
                return
    print("Successfully predicted the Word:")
    print(word)
    print("YOU WIN!")
    return
  

def wordhardprediction4():
    wordlist=["Hand","Love","Game","Hope"]
    word=random.choice(wordlist)
    print(word[0]+" _"+" _"+" _")
    for i in range(4):
        letter2=input("Predict 2nd letter:")
        if(letter2==word[1]):
            print(word[0]+letter2+" _"+" _")
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+" _"+" _"+" _")
            if i==3:
                print("GAME OVER!")
                return
    print("This is a 3 letter word predict 3rd letter")
    for i in range(4):
        letter3=input("predict 3rd letter:")
        if(letter3==word[2]):
            print(word[0]+letter2+letter3+" _")
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+word[1]+" _"+" _")
            if i==3:
                print("GAME OVER!")
                return
    for i in range(4):
        letter4=input("Predict 4th letter:")
        if(letter4==word[3]):
            print(word[0]+letter2+letter3+letter4)
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+letter2+letter3+" _")
            if i==3:
                print("GAME OVER!")
                return
    print("Successfully predicted the Word:")
    print(word)
    print("YOU WIN!")
    return


def wordhardprediction5():
    wordlist=["Khush","Table","Games","Hopes"]
    word=random.choice(wordlist)
    print(word[0]+" _"+" _"+" _"+" _")
    for i in range(4):
        letter2=input("Predict 2nd letter:")
        if(letter2==word[1]):
            print(word[0]+letter2+" _"+" _"+" _")
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+" _"+" _"+" _"+" _")
            if i==3:
                print("GAME OVER")
                return
    print("This is a 3 letter word predict 3rd letter")
    for i in range(4):
        letter3=input("predict 3rd letter:")
        if(letter3==word[2]):
            print(word[0]+letter2+letter3+" _"+" _")
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+word[1]+" _"+" _"+" _")
            if i==3:
                print("GAME OVER")
                return
    for i in range(4):
        letter4=input("Predict 4th letter:")
        if(letter4==word[3]):
            print(word[0]+letter2+letter3+letter4+" _")
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+letter2+letter3+" _"+" _")
            if i==3:
                print("GAME OVER")
                return
    for i in range(4):
        letter5=input("Predict 4th letter:")
        if(letter5==word[4]):
            print(word[0]+letter2+letter3+letter4+letter5)
            break
        else:
            print("INCORRECT!Try Again")
            print(word[0]+letter2+letter3+letter4+" _")
            if i==3:
                print("GAME OVER!")
                return
    print("Successfully predicted the Word:")
    print(word)
    print("YOU WIN!")
    return

def wordeasyprediction3():
    word3_list=["cat","dog","rat","pet"]
    word=random.choice(word3_list)
    print(word[0]+" _"+" _")
    print("Guess other letters:")
    for i in range(4,0,-1):
        #guess1
        g1=input("Enter A Letter:")
        if(g1==word[1]):
            print(word[0]+word[1]+" _")
            break
        elif(g1==word[2]):
            print(word[0]+" _"+word[2])
            break
        else:
            print("incorrect guess")
            print(f"Lives Left:{i-1}")
            if(i==0):
                print("GAME OVER!")
                return
        pass
    for j in range(4,0,-1):
        #guess2
        g2=input("Enter a Letter:")
        if(g2==word[2] and g1==word[1]):
            print("Successfully guessed a word")
            print(word)
            break
        elif(g2==word[1] and g1==word[2]):
            print("Successfully guessed a word")
            print(word)
            break
        else:
            print("Incorrect Guess")
            print(f"Lives Left:{j-1}")
            if(j==0):
                print("GAME OVER!")
                return

def wordeasyprediction4():
    word4_list=["Hand","Dogs","Eyes","Ears"]
    word=random.choice(word4_list)
    print(word[0]+" _"+" _"+" _")
    print("Guess other letters:")
    for i in range(3,-1,-1):
        #guess1
        g1=input("Enter A Letter:")
        if(g1==word[1]):
            print(word[0]+word[1]+" _"+" _")
            break
        elif(g1==word[2]):
            print(word[0]+" _"+word[2]+" _")
            break
        elif(g1==word[3]):
            print(word[0]+" _"+" _"+word[3])
            break
        else:
            print("incorrect guess")
            print(f"Lives Left:{i-1}")
            if(i==0):
                print("GAME OVER!")
                return
        pass
    for j in range(4,0,-1):
        #guess2
        g2=input("Enter a Letter:")
        if(g2==word[2] and g1==word[1]):
            print(word[0]+word[1]+word[2]+" _")
            break
        elif(g2==word[1] and g1==word[2]):
            print(word[0]+word[1]+word[2]+" _")
            break
        elif(g2==word[1] and g1==word[3]):
            print(word[0]+word[1]+" _"+word[3])
            break
        elif(g2==word[3] and g1==word[1]):
            print(word[0]+word[1]+" _"+word[3])
            break
        elif(g2==word[2] and g1==word[3]):
            print(word[0]+" _"+word[2]+word[3])
            break
        elif(g2==word[3] and g1==word[2]):
            print(word[0]+" _"+word[2]+word[3])
            break
        else:
            print("Incorrect Guess")
            print(f"Lives Left:{j-1}")
            if(j==0):
                print("GAME OVER")
                return
        pass
    for k in range(4,0,-1):
        #guess3
        g3=input("Enter A letter:")
        if(g1==word[2] and g2==word[1] and g3==word[3]):
            print(word[0]+word[1]+word[2]+word[3])
            print("Successfully Guessed a word")
            print("YOU WIN")
            break
        elif(g1==word[1] and g2==word[2] and g3==word[3]):
            print(word[0]+word[1]+word[2]+word[3])
            print("Successfully Guessed a word")
            print("YOU WIN")
            break
        elif(g1==word[1] and g2==word[3] and g2==word[2]):
            print(word[0]+word[1]+word[2]+word[3])
            print("Successfully Guessed a word")
            print("YOU WIN")
            break
        elif(g1==word[3] and g2==word[1] and g3==word[2]):
            print(word[0]+word[1]+word[2]+word[3])
            print("Successfully Guessed a word")
            print("YOU WIN")
            break
        elif(g1==word[2] and g2==word[3] and g3==word[1]):
            print(word[0]+word[1]+word[2]+word[3])
            print("Successfully Guessed a word")
            print("YOU WIN")
            break
        elif(g1==word[3] and g2==word[2] and g3==word[1]):
            print(word[0]+word[1]+word[2]+word[3])
            print("Successfully Guessed a word")
            print("YOU WIN")
            break
        else:
            print("Incorrect Guess")
            print(f"Lives Left:{k-1}")
            if(k==0):
                print("GAME OVER!")
                return

def easywordprediction():
    print("In this easy mode of game you have to guess the letters 1st letter will be given to you.")
    print("You will be given 4 lives to guess the word correctly.")
    print("In this easy mode you can guess the letter and if it is there in a word then it will guessed correctly.")
    print("Lets start the game")
    print("1.3 Letter Word(Easy)")
    print("2.4 Letter Word(Medium)")
    print("3.5 Letter Word(Hard)")
    print("4. Back to Menu")
    option=int(input("Enter Your Option:"))
    if(option==1):
        wordeasyprediction3()
    elif(option==2):
        wordeasyprediction4()
    elif(option==3):
        wordeasyprediction5()
    elif(option==4):
        return

def hardwordprediction():
    print("In this hard mode of game you have to guess the letters 1st letter will be given to you.")
    print("You will be given 4 lives to guess the word correctly.")
    print("In this hard mode you have to guess the letter one by one if your guess is wrong you will loose a life.")
    print("Lets start the game")
    print("1.3 Letter Word(Easy)")
    print("2.4 Letter Word(Hard)")
    print("3. Back to Menu")
    option=int(input("Enter Your Option:"))
    if(option==1):
        wordhardprediction3()
    elif(option==2):
        wordhardprediction4()
    elif(option==3):
        return
while True:
    print("-----------------WELCOME TO THE HANGMAN GAME-----------------")
    print("----------------------------MENU-----------------------------")
    print("1.Easy Mode:")
    print("2.Hard Mode:")
    print("3.Exit")
    option=int(input("Enter Your Option:"))
    if(option==1):
        easywordprediction()
    elif(option==2):
        hardwordprediction()
    elif(option==3):
        print("Thank You For Playing The Game!")
        break   