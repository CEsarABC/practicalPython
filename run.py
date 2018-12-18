

user_answers = []
riddles_dict = []
riddles = []
answers = []

# Accessing the riddles to pick questions and answers

with open('data/riddles.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)



number_of_riddles = len(riddles)
riddles_and_answers = zip(riddles, answers)
riddles_list = list(riddles_and_answers)

print(riddles_list)
