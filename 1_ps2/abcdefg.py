import string
help = True
guess = input("Please guess a letter: ")
print(guess.isalpha())
print(guess == "!" and help)
letters_guessed = ["A"]
ab = "adfaASF"
ab = ab.lower()
print(ab)
print(letters_guessed)
letters = string.ascii_lowercase
L = list(letters)


print("Welcome to Hangman!")
print("I am thinking of a word that is " + str(len(L)) + "long")
