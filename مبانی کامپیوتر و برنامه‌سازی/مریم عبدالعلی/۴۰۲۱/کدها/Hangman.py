import random

HANGMAN_PICS = ["""
  +--+
  |  |
     |
     |
     |
     |
 =====""",
"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
"""
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
 ====="""]

def main():
    
    WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()
    secret_word = random.choice(WORDS)
    missedLetters, correctLetters = [],[]
    while True:
        drawHangmanPic(missedLetters, correctLetters, secret_word)
        guess = getPlayerGuess(missedLetters, correctLetters)
        if guess in secret_word:
            correctLetters.append(guess)
            if won(correctLetters, secret_word):
                print("You won!")
                print(f"As you guessed, the correct word is \"{secret_word}\"")
                return
            
        elif guess not in missedLetters:
            missedLetters.append(guess)
            
        if len(missedLetters) == len(HANGMAN_PICS)-1:
            print("You have run out of guesses!")
            print(f"The word was \"{secret_word}\"")
            return
        
def drawHangmanPic(missedLetters, correctLetters, secret_word):
    print(HANGMAN_PICS[len(missedLetters)])
    print(f"Missed letters: {' '.join(missedLetters)}")
    blanks = ['_']*len(secret_word)
    for pos in range(len(blanks)):
        if secret_word[pos] in correctLetters:
            blanks[pos]= secret_word[pos]
    print( " ".join(blanks))
    
def won(correctLetters, secret_word):
    for i in secret_word:
        if not i in correctLetters:
            return False
    return True

def getPlayerGuess(missedLetters, correctLetters):
    while True:
        guess = input("Guess a letter \n> ").upper()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in missedLetters + correctLetters:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter a letter")
        else:
            return guess
        
if __name__ == "__main__":
    main()