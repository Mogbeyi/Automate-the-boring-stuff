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

for quiz_num in range(2):
    with open(f'capitalsquiz{quiz_num + 1}.txt', 'w') as quiz_file:
        quiz_file.write('name:\n\ndate:\n\nperiod:\n\n')
        quiz_file.write((' ' * 20) + f'state capitals quiz (form {quiz_num + 1})')
        quiz_file.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

for question_num in range(50):
    correct_answer = capitals[states[question_number]]
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(anwer_options)
