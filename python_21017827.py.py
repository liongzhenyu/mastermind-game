def playing():
    # making answer random choices
    import random
    list= ('R','P','B','Y')
    mastermindsecret = (random.choices(list,k=4))
    print(mastermindsecret)
    print()
        
    #greeting
    print('Hello everyone!!! :)')
    print('Welcome to play mastermind game!!!')
    print('This is the most interest game that let you guess the four colours.')
    print('If you can guess all correct, you are a genius!!!')
    print('Please guess four colour,')
    print('You can only choose P, B, Y and R')
    print('P = pink, B = blue, Y = yellow and R = red')


    #Program start
    tries=0

    # Loop until player get correct
    while True:
        print()
        guess1=(input('Please enter your guess:').upper()) #Read user input
        if guess1 not in list:
            while guess1 not in list:
                print('Hello:), you only can choose P, B, Y and R.')
                print('P=pink, B=blue, Y=yellow, R=red. Thank you:)')
                guess1 =(input('Please enter your guess:').upper())
                
        guess2 =(input('Please enter your guess:').upper()) #Read user input
        if guess2 not in list:
            while guess2 not in list:
                print('Hello:), you only can choose P, B, Y and R.')
                print('P=pink, B=blue, Y=yellow, R=red. Thank you:)')
                guess2 =(input('Please enter your guess:').upper())
                

        guess3 =(input('Please enter your guess:').upper()) #Read user input
        if guess3 not in list:
            while guess3 not in list:
                print('Hello:), you only can choose P, B, Y and R.')
                print('P=pink, B=blue, Y=yellow, R=red. Thank you:)')
                guess3 =(input('Please enter your guess:').upper())

                    
        guess4 =(input('Please enter your guess:').upper()) #Read user input
        if guess4 not in list:
            while guess4 not in list:
                print('Hello:), you only can choose P, B, Y and R.')
                print('P=pink, B=blue, Y=yellow, R=red. Thank you:)')
                guess4 =(input('Please enter your guess:').upper())
                    
        tries+=1
        print()
        yourguess=[guess1,guess2,guess3,guess4]
        print('Your input:',yourguess)
        print()
        
    #mastermindsecret=['Y','Y','B','B']
    #position           0   1   2   3 
    #Define player scores

        score1=0
        if guess1==mastermindsecret[0]:
            score1+=2
        elif guess1 not in mastermindsecret:
            score1+=0
        else:
            score1+=1
                
        score2=0
        if guess2==mastermindsecret[1]:
            score2+=2
        elif guess2 not in mastermindsecret:
            score2+=0
        else:
            score2+=1

        score3=0
        if guess3==mastermindsecret[2]:
            score3+=2
        elif guess3 not in mastermindsecret:
            score3+=0
        else:
            score3+=1

        score4=0
        if guess4==mastermindsecret[3]:
            score4+=2
        elif guess4 not in mastermindsecret:
            score4+=0
        else:
            score4+=1

        score22=((score1==2)+(score2==2)+(score3==2)+(score4==2))
        print('Correct colour and in right place:',score22)
    
        score21=((score1==0)+(score2==0)+(score3==0)+(score4==0))
        print('Wrong colour and in wrong place:  ',score21)
            
        score23=((score1==1)+(score2==1)+(score3==1)+(score4==1))
        print('Correct colour but in wrong place:',score23)


    #calculatre the score
        sumscore=(score1+score2+score3+score4)

        if sumscore==8:
            print()
            print('Congragulation,you guess all corrects.')
        if tries==1 and sumscore==8:
            print('Great! You took',tries,'guess :)')
            print('Thank you. Hoping you can play again :)')
            break
        if tries!=1 and sumscore==8:
            print('Great! You took',tries,'guesses :)')
            print('Thank you. Hoping you can play again :)')
            break


# Loop to let players can play this game anytime
playing()
print()
while True:
    print()
    print('Do you want to play again?')
    print('You only can type YES or NO.')
    user=(input().upper())
    abcd=['YES','NO']
    if user not in abcd:                                            #If the players don't answer yes or no
        while user not in abcd:
            print('Hello:),you can only type yes or no.')
            print('Do you want to play again?')
            user=(input().upper())
    #    abcd=['YES','NO']
    #position=   0     1
    if user == abcd[0]:
        print()
        playing()
    else:
        print('Thank you for your response,hoping you can play again:)')
        break
