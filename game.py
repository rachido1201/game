import random

# setup

#  definir aleatoirement un chiffre


answer = random.randint(1, 101)
print("answer :", answer)
guess_number = 0
user_wins = False
attempts = 0

# loop


while user_wins is False:
    try:
        print("user_wins :", user_wins)
        # 1  - on demande un chiffre et on le caste
        guess_number = int(input("Enter a number between 1 and 101 :"))
        # 2 - on augmente le nombre de tentative
        attempts += 1  # attempts = attempts + 1
        print("attempts : ", attempts)
        # 3 - checker si le nombre de l'utilisateur est égal à answer
        if guess_number == answer:
            user_wins = True
        elif guess_number > answer:
            print("the secret number is smaller")
        elif guess_number < answer:
            print("the secret number is bigger")
        print("user_wins : ", user_wins)
    except:
        print(" you have a invalid number !!")

# loop
if attempts == 1:
    attempt_word = "attempt"
else:
    attempt_word = "attempts"
# display
print(" you have found the number !")
print(" You found it in ", attempts, attempt_word)
