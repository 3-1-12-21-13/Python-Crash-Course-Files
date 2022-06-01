# EXERCISE 5.3
# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien = "green"
if alien == "green":
    print("The player has earned 5 points.")
elif alien == "red":
    print("The player has earned 15 points.")
else:
    print("The player has earned 10 points.")

alien = "yellow"
if alien == "green":
    print("The player has earned 5 points.")
elif alien == "red":
    print("The player has earned 15 points.")
else:
    print("The player has earned 10 points.")

alien = "red"
if alien == "green":
    print("The player has earned 5 points.")
elif alien == "red":
    print("The player has earned 15 points.")
else:
    print("The player has earned 10 points.")
