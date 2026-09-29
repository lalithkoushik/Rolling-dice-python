# In a LOOP 
  # ASK: for rolling dice (yes/no)
  # If yes: 
  #    roll the dice, generate two random nos
  #    print them
  # If No:
  #    print Thank you message
  #    Terminate code
  # If other than y/n:
  #    print Invalid choice



import random
# In a LOOP 

while True:

  # ASK: for rolling dice (yes/no)
  choice = input('Roll the dice? (y/n): ').lower()

  # If yes: 
  #    roll the dice, generate two random nos
  #    print them
  if choice == 'y':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'({die1}, {die2})')

  # If No:
  #    print Thank you message
  #    Terminate code

  elif choice == 'n':
    print("Thank you for playing!")
    break
  
  # If other than y/n:
  #    print Invalid choice
  else:
    print('Invalid choice')