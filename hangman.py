import random as rand
from wordlist import word_list, word_definitions

def get_random_word():
    return rand.choice(word_list).lower()

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"word: {display}")

    
def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"word: {display}")

def hangman():
    word = get_random_word().lower()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman")

    while attempts > 0:
         display_word(word, guessed_letters)
         guess = input("Guess a letter: ").lower()

         if len(guess) != 1 or not guess.isalpha():
             print("Invalid input buddy. please input a letter")
             continue
         if guess in guessed_letters:
             print("you already guessed that letter buddy.")
             continue
         
         guessed_letters.add(guess)

         if guess in word:
             print("good job buddy")
         else:
             attempts -= 1
             print(f"Wrong buddy get better. you have {attempts} attempts left")

         if all(letter in guessed_letters for letter in word):
            print(f"congrats buddy, you successfully guessed the word: {word}")
            break
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")
    definition = input("Do you want to learn the definition?(y/n): ").lower()
    if definition == 'y':
        word_def = word_definitions.get(word)
        if word_def:
            print(f"the definition for '{word}' is: {word_def}")
        else:
            print(f"Definition for {word} was not found") 
        play_again = input("Would you like to play another game buddy?(y/n): ")
        if play_again == 'y':
            hangman()
        else: 
            print("Thx for playing buddy!")

if __name__ == "__main__":
    hangman()