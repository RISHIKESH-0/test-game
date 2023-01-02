import random
word_list=["banana","tomato","guava"]
chosen_word=random.choice(word_list)
display=[]
end_of_game=False
lives = 6
for _ in range(len(chosen_word)):
    display+="_"
while not end_of_game:
    guess = input("guess a letter").lower()
    if guess in display:
        print(f"you have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word(position)
        if letter == guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives ==0:
            end_of_game=True
            print("You lose.")
