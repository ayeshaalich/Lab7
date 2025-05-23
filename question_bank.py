#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What does DNA stands for?", "deoxinecleouacid")]
    "Sports":[
        ("who is the GOAT of football?", "Messi"),
        ("Which is the worst time of cricket?", "India")]
    "Gaming":[
        ("Which is the best console game?","RDR2"),
         ("Which is the best first person shooter?","COD")]
    "Arts":[
        ("Who drew mona lisa?", "Ibrahim"),
        ("Who is the best artist?", "Ayesha")]
    "Movies":[
        ("Which is my favourite movie?", "Divergent"),
        ("What is the best jake gyllenhal movie?", "nightcrawler")]
    "Animal":[
        ("Biggest animal?", "elephant"),
        ("Smallest animal?", "Zainab")]
    "Nature":[
        ("Highest mountain peak?", "K2"),
        ("Smallest mountain peak?", "Shimla")]
         
        # Add more questions as tuples (question, answer)
    ],
}

hints = {
    "Science": [ "blood"
        # Pair each question with a corresponding hint.
    ], "Sports": ["ball"],
    "gaming":["R"],
    "Arts":["painting"],
    "movies":["jk"],
    "animal":["b"],
    "nature":["sky"]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    if category not found in questions:
        return question[category]
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    if player_answer == correct_answer:
        return True
    else:
        return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    if question in category and question in question[category]:
        question[category].pop(question)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    
    print(f"{question}")
    ans=input()
    return ans
    
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    questions[question]
    
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    print("Yes it's correct!",correct_answer)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




