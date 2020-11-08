secret_word = "kiwi"
guess = input("What is the secret word? ")

if secret_word == guess:
    print("Congratulations! You've found the secret word!")
else:
    print(" Ooops! You didn't guess the secret word!")
print("Let's play again!")