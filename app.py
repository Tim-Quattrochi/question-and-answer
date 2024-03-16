

questions = ["What is your favorite color?:\n",
             "What is your favorite food?:\n", "What is your favorite animal?:\n"]

answers = {}


def ask_questions(questions):
    global answers  # I am using the global keyword because I intend to modify the global variable answers
    for question in questions:
        answer = input(question)
        if len(answer) == 0:
            continue
        answers[question] = answer


# Gets the last word of the question, replaces the question mark with an empty string
def last_word(sentence):
    return sentence.split()[-1].replace('?:', '')


ask_questions(questions)

for question, answer in answers.items():
    print(f"Your favorite {last_word(question)} is {answer}")
