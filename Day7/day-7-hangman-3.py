import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range (word_length):
    display += "_"

#1 end_of_game = False 
end_of_game = False

#2 while not end_of_game: 
while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

print(display)

#3 if "_" not in display:
if "_" not in display:
    end_of_game = True
    print("You win!")