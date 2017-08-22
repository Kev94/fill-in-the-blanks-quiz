# Kevin Belasco Fill-In-The-Blanks Quiz
# Credit due to GitHub repos for some guidance

first_statment = '''The capital of the United States is _1_.  The current president of the U.S. is _2_.  The main legislative document used to govern the United States is _3_.  The first president was _4_.  His face is on the _5_ dollar bill.'''
second_statement = '''Kitten is to cat as puppy is to _1_.  If you drive a car, then you _2_ a plane.  The answer to addition is called the _3_.  If clockwise goes to the right, then counter clockwise goes to the _4_.  There are _5_ hours in a day.'''
third_statement = '''The capital of Pennsylvania is _1_.  The capital of Ohio is _2_.  The capital of Texas is _3_.  The capital of Arizona is _4_.  The capital of Georgia is _5_.'''

question_list = ["_1_","_2_","_3_","_4_","_5_"]
first_answer = ["Washington D.C.", "Donald Trump", "The Constitution", "George Washington", "one"]
second_answer = ["dog", "fly", "sum", "left", "24"]
third_answer = ["Harrisburg", "Columbus", "Austin", "Phoenix", "Atlanta"]

# prompts the user for the quiz and gives them a total amount of attempts
#assigns each level of difficulty to its respective string and returns the statement,answers and list of blanks
#Inputs: 1) The level of difficulty, with respect to 1 = easy, 2 = medium, 3 = hard
#Outputs: Nothing
def organize_game(difficulty):
    print "\nPlease fill in the blanks with the correct answer and no spaces after the last character of your answer.  You only have four tries,though!  Good Luck!\n"
    if difficulty == "1":
        print "\nLevel 1: Easy\n"
        print first_statment
        blank(first_statment, first_answer,question_list)
    elif difficulty == "2":
        print "\nLevel 2: Medium\n"
        print second_statement
        blank(second_statement, second_answer,question_list)
    else:
        print "\nLevel 3: Hard\n"
        print third_statement
        blank(third_statement, third_answer,question_list)

#prompts user to enter a level of difficulty and executes the assignment of statements to answers and the list of blanks
#Inputs: None || Outputs: executes the program / quiz
def choice_level():
    difficulty = raw_input("\nPlease enter difficulty(1, 2 or 3): ")
    if difficulty == "1" or difficulty == "2" or difficulty == "3":
        organize_game(difficulty)

#main function that prompts user to enter answer and replaces the blank if the user is correct until all blanks are filled
#if the user is wrong, it advances attempts until 4 attempts are reached and exits the program
#Inputs: 1) The quiz statements 2) The list of answers that go with their respective statements 3) The list of blanks
#Outputs: Outputs the replaced paragraph with the correct user input or prompts user to try again if incorrect
def blank(statement,answer,question_list):
    index = 0
    attempts =4
    while index < len(question_list):
        user_input = raw_input("\nPlease enter solution for " + str(index +1) + ": ")
        if user_input == answer[index]:
            statement = statement.replace(question_list[index],answer[index])
            index +=1
            print "\n Great! That's correct!\n " + "\n" + statement
        else:
            attempts = attempts - 1
            print "\nThats incorrect! You have " + str(attempts) + " attempt(s) left!\n" + "\n" + statement
            if attempts == 0:
                print "\nGame Over!"
                quit()
    print "\nCongrats! You won!"


choice_level()
