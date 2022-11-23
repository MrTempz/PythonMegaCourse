import json
from os import path


questions_path = path.join(path.curdir, '15_bonus', 'files', 'quiz_data.json')
with open(questions_path, 'r') as file:
    content = file.read()

#print(content)
data = json.loads(content)
#print(data[0])

correct_answers = 0
for question in data:
    print(question["question text"])
    alternatives = question["alternatives"]
    for index, alternative in enumerate(alternatives):
        print(f'{index + 1} - {alternative}')
    user_input = 0
    while user_input < 1:
        try:
            user_input = int(input())
        except ValueError:
            print('Not a number, try again')
            continue
        if user_input > len(alternatives):
            print(f'Answer {user_input} is higher than acceptable answer. Max number is {len(alternatives)}. Try again')
            user_input = 0
            continue
        else:
            if user_input == question["correct answer"]:
                correct_answers += 1
print(f'Your score is {correct_answers}/{len(data)}')


