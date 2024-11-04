# main.py

from functions import show_student_questions, get_student_answers, calculate_student_score, show_final_score
from social_studies_quiz import questions

def run_quiz():
    """
    Function to run the quiz application.
    """
    print("Welcome to the Primary 5 Social Studies Quiz!")
    student_responses = []

    # Loop through each question and get the student's answer
    for question in questions:
        show_student_questions(question)
        answer = get_student_answers()
        student_responses.append(answer)

    # Calculate the score based on the student's responses
    score = calculate_student_score(student_responses)

    # Display the final score and pass/fail result
    show_final_score(score, len(questions))

if __name__ == "__main__":
    run_quiz()
