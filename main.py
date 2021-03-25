import time
import random

# Introduction
print("Welcome to where if your bad at math you will likely fail in 3 seconds")
time.sleep(2)
print("You must find the answer of the multiplication problem that the AI will spit out")
time.sleep(2)
print("If you get the product correct you move on to a another multiplication problem")
time.sleep(2)
print("If you get the product wrong, G A M E    O V E R ")
time.sleep(0.5)
print("Say 'I am ready' if you are ready")
ready = input("Are you ready to start the game?: ")
points = 0

# Code Block
while(ready == "I am ready" or "i am ready"):
  number1 = random.randint(0,12)
  number2 = random.randint(0,12)
  print("Please find the product of this multiplication question: " + str(number1) + " x " + str(number2))
  starttime = time.time()
  userInput = input("Please enter the product here: ") 
  endtime = time.time() 
  print("You have taken around " + str(round(endtime - starttime)) + " seconds")
  if(int(userInput) == number1 * number2):
    print("You are moving on to the next one...")
    points += 1 
  else:
    print("GAME OVER")
    print("You have earned " + str(points) + " points total")
    ready = input("If you want to rage quit say 'no' if you want to continue say 'I am ready'")
    points = 0
    if(ready == "no" or "No"):
      break
print("Thanks for not playing anything")
time.sleep(420)
print("here is a easter egg \n"
"You suck")