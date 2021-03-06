 #import random for choosing word
import random 
def chooseWord():
	 # my list of words
    word_list = ["informatics","hangman","stratosphere","muji","tea","peppermint","furries","strange","hello","wig","oatmeal","roddent"]
    return random.choice(word_list) #return a random selection from the list

def printObscured(obscured):
    for letter in obscured: #for each character in the obscured string
        print(letter+" ",end="") #print the character and a space
    print()    
    
def validInput(user_input):
    return len(user_input) == 1 and str.isalpha(user_input) #if the user input is of length 1 and is alphabetic

def letterInWord(letter,word):
    return letter in word #return if letter is in word

def updateObscured(letter,obscured,word):
    obscured = list(obscured) #change obscured string into a list
    for i in range(len(word)): #loop through the length of the word
        if word[i] == letter: #if the letter at i is the letter given
            obscured[i] = letter #update the obscured list at i to reflect that letter
    return "".join(obscured) #join the list into a string

def main():
    word = chooseWord() #choose a word
    obscured = "_"*len(word) #create the obscured string based on the length of the word
    gameOver = False #game initially not over
    success = False #assume game was not successful
    guesses = 0 #intitially 0 guesses
    while not gameOver: #as long as the game is not over, enter loop
        guesses+=1 #increment guesses
        print("Current Board: ",end="")
        printObscured(obscured) #print the current board
        guess = input("Guess a letter: ").lower() #get the lowe case version of the user guess
        while 1: #loop until break
            if validInput(guess): #if the input is valid
                break #break loop
            guess = input("Enter a valid, single letter guess").lower() #request new input


        if(letterInWord(guess,word)): #if letter is in the word
            print(guess,"in word!") #alert the user
            obscured = updateObscured(guess,obscured,word) #update the obscured word
        else: #otherwise, alert the user
            print(guess,"not in word!")
        if word == obscured: #if the word is the obscured word now
            gameOver = True #game is over
            success = True #game was a success
        elif guesses == 15:  #if guess is 15
            gameOver = True #game is over
    if success: #if the game was successgul
        printObscured(obscured) #print the board
        print("Word solved in",guesses,"guesses") #report guesses
    else:
        print("Max guesses reached. Word was:",word) #tell user answer


main()
    
