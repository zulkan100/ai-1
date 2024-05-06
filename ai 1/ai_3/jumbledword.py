# while True:
#   answer = input("Do you want to loop this argument? Type yes or no: ")
#   if answer.lower() == "yes":
#     print("Okay let’s go!")
#   else:
#     print("Good byee...")
#     break

import random
score = 0
player_name = input("Please enter your name: ")

while True:
  words = ["Python", "Computer", "Programming", "condition", "else", "break", "input", "print", 
           "while", "for"]
  pick = random.choice(words)

  random_word = random.sample(pick, len(pick))
  jumbled = "".join(random_word)
  print("Jumbled word is " + jumbled)
  answer = input("What's in your mind?")

  if answer == pick.lower():
    score +=1
    print("Your score is: ", score)
    if (score == 10):
      print("congratulations!", player_name, "you win!")
      print("your score is", score)
      break
  else:
    print("Better luck next time, correct word is: ", pick)

    cont = input("Press y to continue and n to quit: ")
    if (cont == "n"):
      print(player_name, "your score is: ", score)
      print("Thank you for playing....")
      break