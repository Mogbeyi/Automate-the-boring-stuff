from capitals import capitals
import random

NUMBER_OF_FILES = 3

def generate_random_quizfiles():
    for quiz_num in range(NUMBER_OF_FILES): 
        quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w') 
        answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w') 
        quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quiz_file.write((' ' * 20) + f'state capitals quiz (form {quiz_num + 1})')
        quiz_file.write('\n\n')

        shuffled_state = shuffle_states()
        generate_questions(shuffled_state, quiz_file, answer_key_file)

    quiz_file.close()
    answer_key_file.close()


def shuffle_states():
    states = list(capitals.keys())
    random.shuffle(states)
    return states

def generate_questions(states, quiz_file, answer_file):
    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        write_to_quiz_file(quiz_file, question_num, states, answer_options)
        write_to_answer_file(answer_file, question_num, answer_options, correct_answer)


def write_to_quiz_file(quiz_file, question_num, states, answer_options):
    #Write the question and the answer question to the quiz file.
    quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
    for i in range(4):
        quiz_file.write(f"     {'ABCD'[i]}. {answer_options[i]}\n")
    quiz_file.write('\n')

def write_to_answer_file(answer_file, question_num, answer_options, correct_answer):
    answer_file.write(f"{question_num + 1}.{'ABCD'[answer_options.index(correct_answer)]}")
    answer_file.write(' ')

def main():
    generate_random_quizfiles()

main()



