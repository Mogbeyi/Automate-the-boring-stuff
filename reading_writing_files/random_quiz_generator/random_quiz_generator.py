from capitals import capitals
import random

number_of_files = 3

def generate_random_quizfiles():
    for quiz_num in range(number_of_files): 
        quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w') 
        answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w') 
        quiz_file.write('name:\n\ndate:\n\nperiod:\n\n')
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
    quiz_file.write(f'{question_num + 1}. what is the capital of {states[question_num]}?\n')
    for i in range(4):
        quiz_file.write(f"     {'abcd'[i]}. {answer_options[i]}\n")
    quiz_file.write('\n')

def write_to_answer_file(answer_file, question_num, answer_options, correct_answer):
    answer_file.write(f"{question_num + 1}.{'abcd'[answer_options.index(correct_answer)]}")
    answer_file.write(' ')

def main():
    generate_random_quizfiles()

main()
