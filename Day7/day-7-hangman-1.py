import random

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)

print(f'pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length): #0~5까지 총 6개의 _가 추가
    display += "_"
print(display)

guess = input("Guess a letter : ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)