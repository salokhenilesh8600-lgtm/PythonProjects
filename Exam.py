import random
questions = {
    "What color is the sky on a clear day?": "Blue",
    "How many legs does a dog have?": "Four",
    "What sound does a cat make?": "Meow",
    "Which fruit is yellow and monkeys like to eat?": "Banana",
    "How many days are there in a week?": "Seven",
    "What do bees make?": "Honey",
    "What planet do we live on?": "Earth",
    "Which animal is known as the king of the jungle?": "Lion",
    "What do you use to write on paper?": "Pencil",
    "Which shape has three sides?": "Triangle",
    "What do cows drink?": "Water",
    "What is 2 + 3?": "5",
    "Which bird can say words like humans?": "Parrot",
    "What do plants need to grow?": "Water and sunlight",
    "Which season is very cold?": "Winter"
}


def Exam():
    question_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(question_list,total_questions)

    for idx,question in enumerate(selected_questions):
        print(f'{idx + 1} . {question}')
        user_answer = input("Your answer : ").lower().strip()
        correct_answer = questions[question]
        if user_answer == correct_answer.lower():
            print('Correct! \n')
            score+=1
        else:
            print(f'Wrong. The correct answer is : {correct_answer} . \n')

    print(f'Game over! Your final score is {score} / {total_questions}')


Exam()


# import random
# print(f'All the best for Exam:')
# score = 0
# total_questions = 5
# for i in range(1, total_questions+1):
#     num1 = random.randint(1,100)
#     num2 = random.randint(1,100)
#     print(f'{i} ) {num1} + {num2}')
#     user_answer = eval(input('Your answer :'))
#     correct_answer = num1+num2
#     if user_answer == correct_answer:
#         print('Correct!')
#         score += 1
#     else:
#         print(f'Wrong, correct answer is {correct_answer}')

# print(f'Game Over! Your score is {score}/{total_questions}')




