
# Enter the secret word
secret_word = 'immortal'
previously_guessed = list('_' * len(secret_word))
guesses = list()
current_stage = 0

# Hangman's Death
StagesOfDeath = [['-----', '  |  '],
          ['-----', '  |  ', '  O  '],
          ['-----', '  |  ', '  O  ', '  |  ', '  |  '],
          ['-----', '  |  ', '  O  ', ' /|  ', '  |  '],
          ['-----', '  |  ', '  O  ', ' /|\ ', '  |  '],
          ['-----', '  |  ', '  O  ', ' /|\ ', '  |  ', ' /  '],
          ['-----', '  |  ', '  O  ', ' /|\ ', '  |  ', ' / \\']]

# Required variables
while (current_stage < len(StagesOfDeath)-1):
    print()
    print(*StagesOfDeath[current_stage], sep='\n', end='\n\n')
    print('Word:', ' '.join(previously_guessed))
    print('Guessed Letters:', ' '.join(sorted(guesses)))
    guess = input("Enter your guess: ").strip()

    # Input
    if len(guess) > 1:
        print('One letter at a time!')
        continue
    elif len(guess) < 1:
        print('Guess a letter!')
        continue
    if guess in guesses:
        print('You have already previously_guessed this letter!')
        continue

    # Logic
    guesses.append(guess)
    if guess in secret_word:
        print('Good guess!')
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                previously_guessed[i] = secret_word[i]
    else:
        print('Uh-oh!')
        current_stage = current_stage + 1
        continue

    if '_' not in previously_guessed:
        break

if current_stage == len(StagesOfDeath) - 1:
    print()
    print(*StagesOfDeath[current_stage], sep='\n')
    print("You lose! Better luck next time!\nThe word was:", secret_word)
else:
    print('\nYou won! You saved Hangman!\nword:', secret_word)