 # Hangman game


import random

WORDLIST_FILENAME = "words.txt"  # Make sure words.txt is in the current working directory

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



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    word = ""
    for letter in secretWord:
        if letter not in lettersGuessed:
            word+='_'
        else:
            word+=letter
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    word = string.ascii_lowercase
    wordList = list(word)
    for letter in lettersGuessed:
        wordList.remove(letter)
    word = ''.join(wordList)
    return word
    

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
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    noOfGuesses = 8
    lettersGuessed = []
    while(noOfGuesses):
        print("-"*20)
        print("You have", noOfGuesses ,"guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter:")
        guessInLowerCase = guess.lower()
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase in secretWord:
            lettersGuessed.append(guessInLowerCase)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase not in secretWord:
            lettersGuessed.append(guessInLowerCase)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            noOfGuesses-=1
        
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("-"*20)
            print("Congratulations, you won!")
            return isWordGuessed(secretWord, lettersGuessed)
         
    print("-"*20)   
    print("Sorry, you ran out of guesses. The word was", secretWord, ".")






secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
