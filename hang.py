import random
#import time
name = input('whats your name : ')
print("welcom to Hangman "+name+'.')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
again = 'y'
while again=='y' or again == 'Y':
    word = random.choice(words)

    geusses = ''
    turns = 12
    #print(word)
    while turns > 0:
        failed = 0
        for char in word :

            if char in geusses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0 :
            print("You Win.")
            print('the word is :' + word)
            break
        user_input = input('enter you char :')
        geusses += user_input
        if user_input not in word:
            print("Wrong , try again .")
            turns -= 1
            print(" You still have "+str(turns)+" chance")

            if turns ==0:
                print('You Lose.')
    again = input('do you want to try again ?(Y/*) : ')
print('have a good lukc ' + name + '.')