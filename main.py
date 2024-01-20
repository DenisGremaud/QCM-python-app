import PySimpleGUI as sg
import json
import textwrap
import sys

def create_question_window(titre, question, answers, nb_points_by_question):
    layout = [
        [sg.Text(titre, size=(40, 1), justification='left', font=("Helvetica", 35))],
        qcm_question_responsiveness(question),
        qcm_answers(answers),
        [sg.Text(f"Points: {nb_points_by_question}", size=(40, 1), justification='left', font=("Helvetica", 15), pad=(0, 10))],
        [sg.Button('Exit', size=(20, 2)), sg.Button('Next', size=(20, 2))]
    ]

    return sg.Window('QCM', layout, finalize=True,auto_size_text=True)

def qcm_answers(answers):
    layout = []
    for answer in answers:
        answer_wrapped, num_lines = wrap_text(answer)
        layout.append([sg.Checkbox(answer_wrapped, size=(100, num_lines), font=("Helvetica", 15))])
    return layout

def qcm_question_responsiveness(question, max_line_length=100):
    wrapped_text = textwrap.wrap(question, max_line_length+20)
    number_of_lines = len(wrapped_text)
    question_text = "\n".join(wrapped_text)

    layout = [sg.Text(question_text, size=(max_line_length, number_of_lines), justification='left', font=("Helvetica", 15), pad=(0, 10))]
    return layout

def validate_answer(answer, correct_answers, nb_points_by_question):
    total_score = 0
    for i in range(len(answer)):
        if answer[i] in correct_answers[i]:
            total_score += nb_points_by_question[i] / len(correct_answers[i])
    return total_score


def get_answer_text_by_id(question, answer_id):
    for i, ans in enumerate(question["answers"]):
        if i == answer_id:
            return ans
        
def wrap_text(text, max_line_length=100):
    wrapped_text = textwrap.wrap(text, max_line_length)
    return "\n".join(wrapped_text), len(wrapped_text)

def create_result_window_with_resume_button(questions, user_answers, score, nb_points_total):
    question_layouts = []
    for i, q in enumerate(questions):
        title = f"{q['titre']} ({q['nb_points']} points)"
        wrapped_question, num_lines = wrap_text(q['question'])
        wrapped_user_answer, num_lines_user = wrap_text(get_answer_text_by_id(q, user_answers[i]))
        wrapped_correct_answers_text, num_lines_correct = wrap_text(', '.join(get_answer_text_by_id(q, ans_id) for ans_id in q['correct']))
        question_layouts.append([sg.Text(f"{i+1}. {title}", font=("Helvetica", 20), pad=(0, 10))])
        question_layouts.append([sg.Text(wrapped_question, font=("Helvetica", 15), pad=(0, 10), size=(100, num_lines))])
        question_layouts.append([sg.Text(f"Your answer: {wrapped_user_answer}", font=("Helvetica", 15), pad=(0, 10), text_color=("Red" if user_answers[i] not in q["correct"] else "Green"), size=(100, num_lines_user))])
        question_layouts.append([sg.Text(f"Correct answer: {wrapped_correct_answers_text}", font=("Helvetica", 15), pad=(0, 10), text_color="Green", size=(100, num_lines_correct))])

    layout = [
        [sg.Text(f"Your score is {score} out of {nb_points_total}", size=(40, 1), justification='center', font=("Helvetica", 25), pad=(0, 10))],
        [sg.Column(question_layouts, scrollable=True, vertical_scroll_only=True, size=(1000, 600))],
        [sg.Button("Resume", size=(20, 2))]
    ]

    return sg.Window("Result", layout, finalize=True, auto_size_text=True)

def game(questions):
    user_answer = []
    for question in questions:
        window = create_question_window(question["titre"], question["question"], question["answers"], question["nb_points"])
        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                exit()
            elif event == 'Next':
                if len([key for key, value in values.items() if value]) == 0:
                    sg.popup("Please select an answer") 
                else:   
                    user_answer.append([key for key, value in values.items() if value][0])
                    break
        window.close()

    sg.popup("Quiz Completed")
    score = validate_answer(user_answer, [question["correct"] for question in questions], [question["nb_points"] for question in questions])
    window = create_result_window_with_resume_button(questions, user_answer, score, sum([question["nb_points"] for question in questions]))
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Resume':
            window.close()

if __name__ == "__main__":
    # make help
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: python main.py [json file]")
        exit()
    # check if json file is provided
    if len(sys.argv) < 2:
        print("Please provide a json file as argument")
        exit()
    else:
        questions = json.load(open("qcm.json"))
        sg.theme('DarkGrey14')
        game(questions)
