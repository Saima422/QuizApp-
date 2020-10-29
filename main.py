import random
import time
from Question import Question
from timer import Timer
from question_bank import Ques_bank
from func_timeout import func_timeout, FunctionTimedOut

t = Timer()     # timer object

def timed_process():
    quiz_questions = random.sample(Ques_bank(), k=5)        # 5 random questions from question bank returned by Ques_bank() is stored in quiz_questions in form of list

    def run_quiz(questions):
        score = 0
        t.start()       # start timer
        for question in questions:
            t.pause()       # pause timer and note the time taken by a question
            answer = input(question.prompt + "Ans: ")       # display the question with options
            if answer == question.answer:       # check the answer and note the score (+1: correct ans, 0: wrong ans)
                score += 1
        t.pause()
        end_quiz = input("\nDo you want to SUBMIT quiz before the time limit?(y/n): ")      # submit early option
        return score, end_quiz


    print("\n**Welcome to Quiz Application**\n")
    print("It is a timed Quiz. The Quiz will automatically submit after 10 minutes.\n")

    name = input("Enter your Name: ")
    marks, end_quiz = run_quiz(quiz_questions)      # run_quiz function call
    correct_ans = marks
    wrong_ans = 5 - marks
    print("\n")

    if end_quiz == "n" or end_quiz == "N":      # this block is executed when the user selects not to submit the quiz early
        Time = time.perf_counter()
        if Time < 600:
            time.sleep(600 - Time)
        print("Time Up!!!\n")
    
    # printing the values of name, marks obtained, no. of correct ans, no. of wrong ans
    print("*RESULT* \nName: {} \nMarks Obtained: {}/5 \nNo. of Correct Answers: {} \nNo. of Wrong Answers: {}\n".format(name, marks, correct_ans, wrong_ans))
    
    question_time = t.result()      # list of time taken by each question.....returned via result function of timer.py
    print("\nTime taken for---")
    for index in range(1, 6):
         print(" Question {}: {:0.2f} minutes".format(index, question_time[index]/60))  # time taken by answer each question   var: list- question_time

    elapsed_time = t.stop()
    print("\nTime taken to complete Quiz: {:0.2f} minutes\n".format(elapsed_time/60))   #total time taken to complete quiz   var: elapsed_time
    # return name, marks, correct_ans, wrong_ans


try:
    doitReturnValue = func_timeout(600, timed_process)    # timeout function for executing the script for 10 minutes

except FunctionTimedOut:
    print ("10 minutes Timed Out!!")    #exception occurs when the specified time is elapsed
    