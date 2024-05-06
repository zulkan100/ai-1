import random
import string
# print('Hello and welcome to password maker!')
# adjectives_list = ["sleepy", "slow", "fluffy", "weird", "smart", "evil", "ancient"]
# nouns_list = ['Dinosaur', 'Panda', 'Ball', 'Bass', 'AirConditioner', 'Duck', 'Hammer']

# adjective = random.choice(adjectives_list)
# noun = random.choice(nouns_list)
# number = random.randrange(0, 100)
# char = random.choice(string.punctuation)

# password = adjective + noun + str(number) + char
# print("Recommended Password: " + password)

# print("Hello! This is the email generator")
# user_list = ["taylor", "jays", "chucky", "chrisye", "dvd", "elephant", "duck", "domino", "monopoly"]
# adjective_list = ["slow", "fat", "speedy", "clean", "neat", "musical", "super", "rich", "tasty"]

# adjective = random.choice(adjective_list)
# user = random.choice(user_list)
# number = random.randrange(0, 100)
# email = "@mail.com"

# generated_email = user + adjective + str(number) + email
# print("Recommended Email: " + generated_email)

#weather forecast
print("What will the weather be tomorrow?")
temperature_list = [
  [2, 4, 6, 5],
  [15, 10, 16, 10],
  [24, 20, 22, 23],
  [30, 33, 32, 31]
]
recommend_list = ["Best drink water", "Best buy food", "Best bring umbrella", "Best stay at home"]

temperature = random.choice(temperature_list)
recommend = random.choice(recommend_list)
generated_forecast = "Weather range: " + str(temperature) + " degrees, " + recommend
print(generated_forecast)
