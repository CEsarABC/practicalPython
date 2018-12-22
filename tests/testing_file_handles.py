

user_answers = []
riddles_dict = []
riddles = []
answers = []

''' testing the files handle, by bringing the main functions
and print results after input '''

with open('../data/riddles2.txt', 'r') as file:
    lines = file.read().splitlines()

for i, text in enumerate(lines):
    if i % 2 == 0:
        riddles.append(text)
    else:
        answers.append(text)
        
print(riddles)
print(answers)

''' manual testing for game core funtionality '''

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




ask_riddle()


'''testing the input in capital letters,
    if the user inserts any capitals we need to be sure
    the word of phrase is converted to match the case
    in the list with answers'''

def my_function(answer):
    if answer.islower():
        print (answer + ' this answer is fully lower case')
    else:
        print(answer.lower() + " This answer had capital letters")


my_function("ANSWER")
my_function("AnSweR")
my_function("answer")

''' function to verify the input text is does not have numbers or
speceial characters or is an empty string '''

def count_letters(answer):
    return (sum([1 for letter in answer if letter.isupper() or letter.islower()]))

count_letters('My name is JOHN')
count_letters('')

assert count_letters('') == 0, 'empty string'
assert count_letters('Answer') == 6, '6 characters'
assert count_letters('%$£&*') == 0, 'Special characters'
assert count_letters('234') == 0, 'numbers present'

print ('all tests passed')
