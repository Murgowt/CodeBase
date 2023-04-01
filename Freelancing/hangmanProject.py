import random

# +------------------------------+
# |                              |
# |       _ _ _ _ _ _ _ _        |
# |                              |
# |     Letters remaining: 8     |
# |                              |
# |     Guesses remaining: 5     |
# |                              |
# |       Guessed letters        |
# |       ---------------        |
# |                              |
# +------------------------------+
def draw_hangman(tiles, remaining_letters, guesses, guessed_string):
    tiles_string = ''
    for i in range(len(tiles)):
        tiles_string+=tiles[i]
        if(i!=len(tiles)-1):
            tiles_string+=" "
    tiles_string=tiles_string.center(32)
    tiles_string=list(tiles_string)
    tiles_string[0]="|"
    tiles_string[-1]="|"
    tiles_string=''.join(tiles_string)

    lmString = "Letters remaining: "+str(remaining_letters)
    lmString = lmString.center(32)
    lmString = list(lmString)
    lmString[0],lmString[-1]="|","|"
    lmString = ''.join(lmString)

    gsString = "Letters remaining: "+str(guesses)
    gsString = gsString.center(32)
    gsString = list(gsString)
    gsString[0],gsString[-1]="|","|"
    gsString = ''.join(gsString)


    guessed_string_letters = ""
    for i in range(len(guessed_string)):
        guessed_string_letters+=guessed_string[i]
        if(i!=len(guessed_string)-1):
            guessed_string_letters+=","
    guessed_string_letters=guessed_string_letters.center(32)
    guessed_string_letters = list(guessed_string_letters)
    guessed_string_letters[0] = "|"
    guessed_string_letters[-1] = "|"
    guessed_string_letters = ''.join(guessed_string_letters)

    print("\n+------------------------------+")
    if(guesses<5):
        line2="|   .---.                      |"
        line3="|  |     |                     |"
        line4="|  |     |                     |"
        line5="|  |     |                     |"
        line6="|   '---'                      |"
        if(guesses==3):
            line3="|  | o   |                     |"
        elif(guesses==2):
            line3 = "|  | o o |                     |"
        elif(guesses == 1):
            line3 = "|  | o o |                     |"
            line4 = "|  |  >  |                     |"
        elif(guesses ==0):
            line3 = "|  | o o |                     |"
            line4 = "|  |  >  |                     |"
            line5 = "|  | '-' |                     |"
        print(line2)
        print(line3)
        print(line4)
        print(line5)
        print(line6)
    if(guesses==5):
        print("|                              |")
    print(tiles_string)
    print("|                              |")
    print(lmString)
    print("|                              |")
    print("|     Guesses remaining: "+str(guesses)+"     |")
    print("|                              |")
    print("|       Guessed letters        |")
    print("|       ---------------        |")
    print(guessed_string_letters)
    print("+------------------------------+\n")

# List of words to choose from
words = ['spartan', 'cedar', 'football', 'programming', 'computer', 'business', 'accounting', 'broad','major', 'minor', 'graded', 'project', 'algorithm', 'branching', 'nested']


while True:
    seed_response = input('Would you like to enter a seed? (y/n):')
    seed=''
    if seed_response.lower() == 'y':
        while True:
            seed = input('Please enter a seed:')
            if seed.isnumeric() and int(seed) >= 0:
                
                break
            else:
                print('ERROR: Invalid seed.')
        break
    elif seed_response.lower() == 'n':
        random.seed()
        break
    else:
        print('Error: answer must be y or n')

# Select random word from list
random.seed(int(seed))
word = random.choice(words)
random.seed(int(seed))
word = random.choice(words)
print(word)
# Initialize variables
word_length = len(word)
tiles = ['_' for i in range(word_length)]
remaining_letters = word_length
guesses_remaining = 5
guessed_letters = []

# Begin game loop
while guesses_remaining > 0 and '_' in tiles:
    draw_hangman(tiles, remaining_letters, guesses_remaining, ''.join(guessed_letters))
    guess = input('Enter a letter:')[0].lower()
    if not guess.isalpha():
        print('Invalid input. Please enter a letter.')
    elif guess in guessed_letters:
        print('You have already guessed that letter!')
    elif guess in word:
        for i in range(word_length):
            if word[i] == guess:
                tiles[i] = guess
        remaining_letters = tiles.count('_')
        guessed_letters.append(guess)
    else:
        guesses_remaining -= 1
        guessed_letters.append(guess)
else:
    draw_hangman(tiles, remaining_letters, guesses_remaining, ''.join(guessed_letters))
    if '_' not in tiles:
        print('You win!')
    else:
        print('You lost!')
    print('The word was ' + word+"!")


# +------------------------------+
# |                              |
# |       _ _ _ _ _ _ _ _        |
# |                              |
# |     Letters remaining: 8     |
# |                              |
# |     Guesses remaining: 5     |
# |                              |
# |       Guessed letters        |
# |       ---------------        |
# |                              |
# +------------------------------+


#|       _ _ _ _ _ a _ _        |
#