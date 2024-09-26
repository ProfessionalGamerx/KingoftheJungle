import random
#creates a list of animals for the computer to choose from
animalList = ["Lion", "Elephant", "Mouse"]
player_score = 0
computer_score = 0
#defines the function that will be used to determine the winner
def determine_winner(playerChoice, computerChoice):
  #indicate we want to modify the global score variables
  global player_score, computer_score  
  #compares the two choices to see who wins
  if playerChoice.capitalize() == computerChoice:
    print("It's a tie! No battle was fought.")
  #all the ways the player can win
  elif playerChoice.capitalize() == "Lion" and computerChoice == "Mouse":
    print(f"{playerChoice} ate {computerChoice}. You win!")
    player_score += 1 # Increase score by 1 for a win
  elif playerChoice.capitalize() == "Elephant" and computerChoice == "Lion":
    print(f"{playerChoice} stomped on {computerChoice}. You win!")
    player_score += 1 # Increase score by 1 for a win
  elif playerChoice.capitalize() == "Mouse" and computerChoice == "Elephant":
    print(f"{playerChoice} scared {computerChoice} away. You win!")
    player_score += 1 # Increase score by 1 for a win
  #all the ways the computer can win
  elif computerChoice == "Lion" and playerChoice.capitalize() == "Mouse":
    print(f"{computerChoice} ate {playerChoice}. You lose!")
    computer_score += 1
  elif computerChoice == "Elephant" and playerChoice.capitalize() == "Lion":
    print(f"{computerChoice} stomped on {playerChoice}. You lose!")
    computer_score += 1
  elif computerChoice == "Mouse" and playerChoice.capitalize() == "Elephant":
    print(f"{computerChoice} scared {playerChoice} away. You lose!")
    computer_score += 1
#sets up a while loop that loops the game until the player chooses to quit
while True:
  #asks the player to choose an animal
  while True:
    playerChoice = input("Choose Lion, Elephant or Mouse: ")
    if playerChoice.capitalize() == "Lion" or playerChoice.capitalize(
    ) == "Elephant" or playerChoice.capitalize() == "Mouse":
      break
    else:
      print("Invalid input. Please enter a valid choice.")
  #randomly chooses an animal for the computer
  computerChoice = random.choice(animalList)
  print("computer chose: " + (computerChoice))
  #calls the function to determine the winner
  determine_winner(playerChoice.capitalize(), computerChoice)
  # Display current scores
  print(f"Your current score is: {player_score}")
  print(f"Computer's current score is: {computer_score}")
  #asks the player if they want to play again
  play_again = input("Do you want to play again? (yes/no): ")
  #the ! followed by the = sign (!=) means that the variable is not equal to the value
  if play_again.lower() != "yes" and play_again.lower() != "ye" and play_again.lower() != "yea" and play_again.lower() != "y" and play_again.lower() != "yeah" and play_again.lower() != "yesh" and play_again.lower() != "ok": 
    break

#Display final scores
print("Thanks for playing!")
print(f"Your final score is: {player_score}")
print(f"Computer's final score is: {computer_score}")

if player_score > computer_score:
  print("You have a higher score!")
elif computer_score > player_score:
  print("The computer has a higher score!")
elif player_score == computer_score:
  print("The score is tied!")
