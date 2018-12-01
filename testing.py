

user_answers = []
riddles_dict = []
riddles = []
answers = []

# Accessing the riddles to pick questions and answers

with open('data/riddles1.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)


def ask_riddle():
    number_of_riddles = len(riddles)
    riddles_and_answers = zip(riddles, answers)
    riddles_list = list(riddles_and_answers)


    score = 0

    for riddle, answer in riddles_list:
        guess_answer = input(riddle+"\n" + '>>')
        if guess_answer == answer:
            score += 1
            print('Right!')
        else:
            user_answers.append(guess_answer)
            print('Wrong! ' + 'the answer is >> ' + answer)
        print(' you got {0} correct out of {1}'.format(score, number_of_riddles))

#ask_riddle()

def my_function(fname):
    if fname.islower():
        print ('it worked')
    else:
        print(fname.lower() + " Refsnes")

my_function("EMIL")
my_function("tobias")
my_function("Linus")
