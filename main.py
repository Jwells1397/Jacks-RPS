import random

def get_choices(): 
  #def says you're going to define a function. get choices is the name of the function. () are needed as sometimes an argument is taken in for a function. : is required to say some processes will be carried out after.
  player_choice = input("Enter a choice (rock, paper, scissors):")
#player choice is indented 2 spaces or a shift, makes it easier to read but also is required by python so it can also read it properly. underscore is required instead of a space, so python can read it properly and avoid naming conventions already built in. = means assign. so player_choice is assigned to what comes after it. input is inbuilt and the parentheses after take in what is called a prompt and this is printed to the standard output (the console) it then reads the input.
  options = ["rock", "paper", "scissors"]
#options is the variable name and it has been assigned to a mutable sequence which contains 3 elements, rock, paper and scissors.
  computer_choice = random.choice(options)
#computer_choice is the variable name and is assigned to what comes after. random variable generator is a imported, it is inbuilt (something to do with C). choice is based off random it is an inbuilt function i think. it randomly choose one of the elements in the sequence. Note sequence must be non empty.     
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
#choices is the variable name. = does the assigning. assigned to key value pairs. Key is the player and player choice is the value. Both are strings. returns the string choices. the return is there as that is the syntax for a function. a function needs to return something.
def check_win(player, computer): #define a function called check_win, which takes two arugments player and computer. 
  print(f"You chose {player}, computer chose {computer}")
#when called the function immediately prints out what is within the quotes within the brackets. the f essentially means I don't have to manually concatonate the strings.
  if player == computer: 
#this line means if a condition is met. Here the condition is player having the same value as computer, then drop a line and go into that if statement. 
    return "It's a tie!"
#this is within the if statement and so if the check win function is called and the if condition is met then the string, it's a tie will be returned.
  elif player == "rock":
#if the first if statement is not met, the the python will read the line which is indented the same amount as the first if. So it will look at elif. so if the player == rock condition is met then carry on within that elif.
    if computer == "scissors":
#this is a nested if statement. so given that player has the value rock, then if the condition that computer has the value scissors. move down within that statement to the next line.
      return "Rock smashes scissors! You win!"
#This is within the nested if statement and given the condition is met then reuturned will be the string rock sashes scirssors! You win!
    else: #This means if none of the above conditions are met then do the following.
      return "Paper covers rock! You lose."
#The following being return the string paper covers rock! you lose.
  elif player == "paper":
#If player wasn't the same as computer or rock then this line will be read. if condition is met then it will read what is within this elif.
    if computer == "rock":
#so if the elif condition is met then it will see if computer has the value rock. if it does it will go into that if statement
      return "Paper covers rock! You win!"
#within that if statement is only the return statement and so the string paper covers rock! you win! will be returned.Note that after a return is read the code exits the if statement.
    else:
      return "Scissors cuts paper! You lose."
#if computer is not rock then it must be scissors and return the string Scissors cuts paper! You lose.
  elif player == "scissors":
#Else if player has the values scissors then run through the nested if statements below
    if computer == "paper":
#if the condition that computer has the value paper then move down within the if statement
      return "Scissors cuts paper! You win!"
#returns the string "Scissors cuts paper! You win!"
    else:
#If above condition is not met then move with this else 
      return "Rock  smashes scissors! You lose."   
#Returned will be Rock smahses scissors, you lose

      
choices = get_choices()
#the function get_choices is assigned a variable name so that it can be called
#It is assigned the name choices
result = check_win(choices["player"], choices["computer"])
#the check_win function is assigned to a variable name called result. 
#it takes two arguments, which are separated by a comma.
#the get_choices function is now called, as it returns a dictionary value, a key must be put in brackets after it is called. so the first key is player and second is computer. These will spit out rock and whatever computer picked. these two values wil now be the arguments for the check_win function. 
print(result)
#the variable result will now be printed to the console.
#Game complete
