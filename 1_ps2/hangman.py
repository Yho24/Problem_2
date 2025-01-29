# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    has_won = False
    L = list(secret_word)
    Lcopy = L[:]
    if secret_word == "":
       return True #check if string is empty
    for x in Lcopy:
        for i in letters_guessed:
            if x == i:
                L.remove(i)  
    
    if len(L) == 0:
      has_won = True
    return has_won


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    L =list(secret_word)
    result = []
    flag = False
    for x in L:
        flag = False
        for i in letters_guessed:
            if i == x:
              result.append(x)
              flag = True
        if not flag:
            result.append("*")
            
    rs ="".join(result)
    return rs

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    L = list(letters)
    Removed_L = []
    if len(letters_guessed) == 0:
        return letters
    Lcopy = L[:]
    for x in letters_guessed:
        if x in Lcopy and x not in Removed_L:
            L.remove(x)
            Removed_L.append(x)
    result = "".join(L)
    return result

def choose_letter(secret_word, available_letters):
    """
    secret word: string of the secret word to guess
    available letters: letters the user hasent guessed yet
    """
    Letters_in_both = []
    for x in secret_word:
        if x in available_letters:
            Letters_in_both.append(x)
    choose_from = "".join(Letters_in_both)
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    Letters = string.ascii_lowercase
    flag = True
    won = False
    already_guessed = False
    L =list(secret_word)
    Unique_letters = []
    for i in L:
        if i not in Unique_letters:
            Unique_letters.append(i)

    number_of_unique_letters = len(Unique_letters)      
    Letters_guessed = []
    vowels = ["a", "e", "i", "o", "u"]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(L)) + " letters long")
    
    while guesses > 0 and not won:
        already_guessed = False
        print("-----------------------")
        print("You have " + str(guesses) + " guesses left")
        print("Available letters: " + get_available_letters(Letters_guessed))
        guess = input("Please guess a letter: ")
        if len(guess) != 1:
            flag = False
        
        if not guess.isalpha():
            flag = False

        if guess.isalpha():
            guess = guess.lower()
            if guess in Letters:
                flag = True
            else:
                flag = False
        
        if guess in Letters_guessed:
            print("Oops! You have already guessed that letter: "+ get_word_progress(secret_word, Letters_guessed))
            flag = False
            already_guessed = True
        
        if flag:
          Letters_guessed.append(guess)
          if guess in secret_word:
              print("Good Guess: " + get_word_progress(secret_word, Letters_guessed))
          else:
              print("Oops! That letter is not in my word: " + get_word_progress(secret_word, Letters_guessed))
              if guess in vowels:
                  guesses = guesses -2
              else:
                  guesses = guesses -1
        
        elif guess == "!" and with_help:
            if guesses < 4:
                print("You dont have enough guesses to ask for a tip")
            else:
                guesses = guesses - 3
                guess = choose_letter(secret_word, get_available_letters(Letters_guessed))
                print("Letter revealed: " + guess)
                Letters_guessed.append(guess)
                print(get_word_progress(secret_word, Letters_guessed))
        
        elif not already_guessed:
          print("Oops! That is not a valid letter. Please input a letter from the alphabet: " + get_word_progress(secret_word, Letters_guessed))
        
        if has_player_won(secret_word, Letters_guessed):
            print("------------------------------")
            print("Congratulations, you won!")
            total_score = guesses + 4 * number_of_unique_letters + 3 * len(secret_word)
            print("Your total score for this game is: " + str(total_score))
            won = True
    
    
    if not won:
        print("--------------------------")
        print("Sorry, you ran out of guesses. The word was " + secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     secret_word = choose_word(wordlist)
     with_help = True
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    #pass

