age = int(input("please enter your age "))

if age in range (0, 17):
    print("Please go home you're still a kid and can't vote")

if age in range (18, 50):
    print("you're eligible to vote and your vote is counted")

else:
    print("you're too old to be here Man!")