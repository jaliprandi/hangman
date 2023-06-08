def make_wordlist():
    wordlist=[]
    with open('dictionary.txt') as file:
        for line in file:
            wordlist.append(line.rstrip())
    return wordlist

def choose_word(wordlist):
    from random import randint
    return wordlist[randint(0,len(wordlist)-1)]

def user_input(past_guesses):
    guess = input('Enter a single letter\n')
    if guess in past_guesses:
        print('You already guessed',guess)
        user_input(past_guesses)
    else:
        past_guesses.append(guess)
    past_guesses.sort()

def make_clue(word,guesses):
    clue=[]
    for letter in word:
        if letter in guesses:
            clue.append(letter)
        else:
            clue.append('_')
    return ' '.join(clue)

def make_gallows(num):
    repl=[('O',15),('|',21),('/',20),('\\',22),('/',27),('\\',29)]
    template=''' ___
|   |
|    
|     
|     
|_____
'''
    gallows=list(template)
    for i in range(num):
        gallows[repl[i][1]] = repl[i][0]
    return ''.join(gallows)

def get_score(guesses,word):
    score=0
    for guess in guesses:
        if guess not in word:
            score+=1
    return score

def check_win(word,guesses):
    for letter in word:
        if letter not in guesses:
            return False
    #if all of the letters were guessed
    return True
    
def game():
    word=choose_word(make_wordlist())
    guesses = []
    while True:
        score=get_score(guesses,word)
        print(make_gallows(score))
        print(make_clue(word,guesses),' '.join(guesses),sep='\t|\t')
        if score >= 6:
            print('You lose')
            print('The word was',word)
            break
        elif check_win(word,guesses):
            print('You win!')
            break
        user_input(guesses)

game()
