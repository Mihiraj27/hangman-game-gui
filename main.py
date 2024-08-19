import random;

letter_list = ['Hangman', 'Python', 'Audacix', 'Bottle', 'Pen']
guesses = ['e','r']
picked_word = ""
done = False
maximum_attemp = 0


picked_word = random.choice(letter_list)
maximum_attemp = round(len(picked_word)/2)
   

while not done:
    for letter in picked_word:
        if letter.lower() in guesses:
           print(letter,end=" ")
        else:
            print("_",end=" ") 
    done = True 

    guess = input(f"Alowed Errors Left {maximum_attemp}, Next Guess :")
    guesses.append(guess.lower())

    if guess.lower() not in picked_word.lower():
        maximum_attemp -=1
        if maximum_attemp ==  0:
            break

    #done = True
    for letter in picked_word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You won the Game : Word Is : {picked_word} !")
else:
    print(f" Game Over You Loss")

