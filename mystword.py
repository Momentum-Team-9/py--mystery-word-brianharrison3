import random


#pick mode
game_start = False
while game_start == False:
    if game_start == False:
        game_mode = input("What mode do you want to play, easy = 1, normal = 2, hard = 3 ")
        if game_mode == "1" or game_mode == "2" or game_mode == "3":
            game_start = True

#getting random word for right game mode

    with open("words.txt") as wordstxt:
        all_words = wordstxt.readlines()
    random_word = random.choice(all_words)      
    random_word = random_word.lower()
   
    if game_mode == "1":
        while len(random_word) <= 3 or len(random_word) > 7:
            random_word = random.choice(all_words)      
            random_word = random_word.lower()
    if game_mode == "2":
        while len(random_word) <= 5 or len(random_word) > 8:
            random_word = random.choice(all_words)      
            random_word = random_word.lower()
    if game_mode == "3":
        while len(random_word) <= 7:
            random_word = random.choice(all_words)      
            random_word = random_word.lower()

#random_word 
print(random_word)
print("The word has" , len(random_word) , "letters")
guess_made = ''
# valid guesses
valid = ["a","b", "c", "d","e" ,"f" ,"g" ,"h" ,"i" ,"j" , "k", "l", "m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z"]  
while game_start == True:
    count = 0
    guesses_left = 7
    guess = input("guess a letter ")
    guess = guess.lower()
#guess input errors
    if len(guess) > 1 or guess not in valid:
        print("Error, one letter only or chacter entered is not a valid")
    else:
        guess_made += guess 
        print("Guesses made: ", guess_made)
        print(random_word)
        for letter in random_word:
            if letter in guess:
                print("There is a", letter, "in the word")
                count = count + 1
                #if count == 0:
      
        if guess not in random_word:
            print("WRONG, be carefull you only have", guesses_left , "wrong guesses")
            guesses_left = guesses_left - 1
        for letter in random_word:
            if letter in guess_made:
                print(letter)
            else:
                print("-")
#stop game
        print(len(random_word) - 1)
        print(count)
        if guesses_left == 0:
            print("out of guesses")
            game_start = False
        if (len(random_word) - 2) == count:
            game_start = False
    
    















    








