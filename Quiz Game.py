print("Welcome to the quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let's play!")
score = 0

answer = input("Who is Canada's current PM? ")
if answer.lower() == "justin trudeau":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

answer = input("What is the capital city of Canada? ")
if answer.lower() == "ottawa":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer = input("What is the capital city of Ontario? ")
if answer.lower() == "toronto":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer = input("Who is the Premier of Ontario? ")
if answer.lower() == "doug ford":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%. ")

