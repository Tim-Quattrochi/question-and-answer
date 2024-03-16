questions = ["What is your favorite color? ",
             "What is your favorite food? ", "What is your favorite animal? "]

answers = {}

# Gets the last word of the question, replaces the question mark with an empty string


def last_word(sentence):
    return sentence.split()[-1].replace('?', '')


for question in questions:
    answer = input(question)
    if len(answer) == 0:
        continue
    answers[question] = answer

for question, answer in answers.items():
    print(f"Your favorite {last_word(question)} is {answer}")
