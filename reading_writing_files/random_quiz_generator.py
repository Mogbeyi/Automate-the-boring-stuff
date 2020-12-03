import random
# the quiz data. keys are states and values are their capitals.
capitals = {
    'alabama': 'montgomery', 'alaska': 'juneau', 'arizona': 'phoenix',
    'arkansas': 'little rock', 'california': 'sacramento', 'colorado': 'denver', 
    'connecticut': 'hartford', 'delaware': 'dover', 'florida': 'tallahassee', 
    'georgia': 'atlanta', 'hawaii': 'honolulu', 'idaho': 'boise', 'illinois': 'springfield', 
    'indiana': 'indianapolis', 'iowa': 'des moines', 'kansas': 'topeka', 'kentucky': 'frankfort', 
    'louisiana': 'baton rouge', 'maine': 'augusta', 'maryland': 'annapolis', 'massachusetts': 'boston', 'michigan': 
    'lansing', 'minnesota': 'saint paul', 'mississippi': 'jackson', 'missouri': 'jefferson city', 'montana': 'helena', 
    'nebraska': 'lincoln', 'nevada': 'carson city', 'new hampshire': 'concord', 'new jersey': 'trenton', 'new mexico': 'santa fe', 
    'new york': 'albany', 'north carolina': 'raleigh','north dakota': 'bismarck', 'ohio': 'columbus', 'oklahoma': 'oklahoma city', 
    'oregon': 'salem', 'pennsylvania': 'harrisburg', 'rhode island': 'providence', 'south carolina': 'columbia', 'south dakota': 'pierre', 
    'tennessee': 'nashville', 'texas': 'austin', 'utah': 'salt lake city', 'vermont': 'montpelier', 'virginia': 'richmond', 'washington': 'olympia',
    'west virginia': 'charleston', 'wisconsin': 'madison', 'wyoming': 'cheyenne'
}

for quiz_num in range(3):
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w') 
    answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w') 
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'state capitals quiz (form {quiz_num + 1})')
    quiz_file.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        #Write the question and the answer question to the quiz file.
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f"     {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        answer_key_file.write(f"{question_num + 1}.{'ABCD'[answer_options.index(correct_answer)]}")
        answer_key_file.write(' ')

quiz_file.close()
answer_key_file.close()

