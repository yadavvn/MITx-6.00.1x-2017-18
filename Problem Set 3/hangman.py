# Hangman game

import random
import string


WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
# wordlist = loadWords()
loadWords()
# print(chooseWord(wordlist))

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    matchString = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            matchString += letter

    return matchString == secretWord


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWordList = ('_ ' * len(secretWord)).split()

    for pos in range(len(secretWord)):
        if secretWord[pos] in lettersGuessed:
            guessedWordList[pos] = secretWord[pos]

    return ' '.join(guessedWordList)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters += letter

    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    guess = 8
    guessList = []
    while guess > 0 and "_" in getGuessedWord(secretWord, guessList):
        print("-" * 23)
        print("You have {} guesses left.".format(guess))
        print("Available letters: {}".format(getAvailableLetters(guessList)))
        response = input("Please guess a letter: ")

        if response in secretWord:
            if response not in guessList:
                guessList.append(response)
                print("Good guess: {}".format(getGuessedWord(secretWord, guessList)))
            else:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, guessList)))

        else:
            if response not in guessList:
                guessList.append(response)
                print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, guessList)))
                guess -= 1
            else:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, guessList)))

    result = isWordGuessed(secretWord, guessList)
    print("-" * 23)
    if result:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
wordlist = loadWords()
# secretWord = chooseWord(wordlist).lower()
secretWord = 'y'
hangman(secretWord)

