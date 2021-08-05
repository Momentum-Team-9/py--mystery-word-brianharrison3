import random

#pick mode
game_start = False
while game_start == False:
    if game_start == False:
        game_mode = input("What mode do you want to play, easy = 1, normal = 2, hard = 3 ")
        if game_mode == "1" or game_mode == "2" or game_mode == "3":
            game_start = True

#getting random word
with open("words.txt") as wordstxt:
    all_words = wordstxt.readlines()
random_word = random.choice(all_words)      
random_word = random_word.lower()
random_word = list(random_word)
#random_word = random_word.pop()
print(random_word)

print("The word has" , len(random_word) , "letters")

guess_made = []
#valid = ["a","b", "c", "d","e" ,"f" ,"g" ,"h" ,"i" ,"j" , "k", "l", "m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z"]
#for letter in valid:   
#print(valid)


while game_start == True:
    guess = input("guess a letter ")
    guess = guess.lower()
    if len(guess) > 1:
        print("Error, one letter only or chacter entered is not a valid")
    else:
        guess_made.append(guess)
    print("Guess made: ", guess_made)
    print("Letters in word: ", set(guess_made) & set(random_word))

    #stop game
    if len(guess_made) > 7:
        game_start = False

    
    















    








