
personality_attributes = ["funny", "serious", "caring",
                          "adventurous", "curious", "creative", "intelligent", "kind"]

questions = ["What is your favorite color?:\n",
             "What is your favorite food?:\n", "What is your favorite animal?:\n", "What is your favorite movie?:\n", "What is your favorite book?:\n"]

answer_scores = {
    "funny": {"pizza", "dog", "the hitchhiker's guide to the galaxy", "yellow", "madea"},
    "serious": {"salad", "cat", "to kill a mockingbird", "green", "the godfather"},
    "caring": {"spaghetti", "bird", "the help", "blue", "the notebook"},
    "adventurous": {"taco", "fish", "the hobbit", "orange", "jaws"},
    "curious": {"hamburger", "rabbit", "the alchemist", "red", "alice in wonderland"},
    "creative": {"chicken", "horse", "harry potter and the philosopher's stone", "purple", "the lion king"},
    "intelligent": {"steak", "elephant", "sapiens: a brief history of humankind", "black", "the matrix"},
    "kind": {"pasta", "dolphin", "wonder", "pink", "finding nemo"}
}


def score_personality(answers, answer_scores):
    personality_scores = {attribute: 0 for attribute in personality_attributes}

    for answer in answers:
        for attribute, answers in answer_scores.items():
            if answer.lower() in answers:
                personality_scores[attribute] += 1

    return personality_scores


def ask_questions(questions):
    answers = []
    for question in questions:
        answer = input(question)
        if len(answer) == 0:  # if the user presses return/enter they skip
            continue
        answers.append(answer)
    return answers


answers = ask_questions(questions)


scores = score_personality(answers, answer_scores)

max_attribute = max(scores, key=scores.get)
max_score = scores[max_attribute]

print(
    f"Your personality attribute with the highest score is {max_attribute} with a score of {max_score}.")


# The following is commented out for future reference.
# -----------------------------------------------------
# Gets the last word of the question, replaces the question mark with an empty string
# def last_word(sentence):
#     return sentence.split()[-1].replace('?:', '')

# for question, answer in answers.items():
#     print(f"Your favorite {last_word(question)} is {answer}")

# new_answers = answers.values()

# list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
# [print(x) for x in new_answers]
