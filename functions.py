# quiz_functions.py

def show_student_questions(question):
    """
 show a question and the multiple choice options for the student
    """
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)


def get_student_answers():
    """
    ask the students for their answers and ensuring it is 'a', 'b', or 'c'.
    """
    while True:
        choice = input("Choose your answer (a, b, or c): ").lower()
        if choice in ["a", "b", "c"]:
            return choice
        else:
            print("Invalid choice. Please enter 'a', 'b', or 'c'.")


def calculate_student_score(student_responses):
    """
    Compares the student's responses to the correct answers and calculates the score.
    """
    from social_studies_quiz import questions  
    score = 0
    for i in range(len(questions)):
        if student_responses[i] == questions[i]["answer"].lower():
            score += 1
        return score



def show_final_score(score, num_questions):
    """
    Displays the user's final score and determine if they pass or fail based on 60% pass mark.
    """
    passing_score = 0.6 * num_questions 
    print(f"\nYour final score is: {score}/{num_questions}")
    if score >= passing_score:
        print("Result: Pass")
    else:
        print("Result: Fail")
