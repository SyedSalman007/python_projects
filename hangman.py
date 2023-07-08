import random
import hangman_ascii_art as ascii
import hangman_words_list as word

print(ascii.logo)
selected_word = random.choice(word.word_list)
selected_word = list(selected_word) # converting the single word into list
# duplicate_selected_word = selected_word.copy()

total_lives = 7
word_length = len(selected_word)

guess_string = []
for _ in range(word_length):
    guess_string.append("_")

while total_lives:
    test_char = input("Enter a character: ").lower()
    for position in range(word_length):
        letter = selected_word[position]
        if letter == test_char:
            guess_string[position] = test_char
    if test_char not in selected_word:
        print(ascii.stages[total_lives - 1])
        total_lives -= 1
    print(guess_string)

    if "_" not in guess_string:
        print("You Won")
        break
else:
    print("You lose")
    print(f"The word was {selected_word}")