# CHECKING MULTIPLE CONDITIONS
# The keywords AND and OR can help you evaluate if you want multiple conditions to be TRUE or if you are satisfied with one or more. 
# Example below:
age = 30
print(f"The age is - {age}.")
if age > 20 and age < 40:
    print("The age is above 20 and below 40.")

# USING OR TO CHECK MULTIPLE CONDITIONS
# The keyword OR allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An OR expression fails only when both individual tests fail.
age = 31
print(f"\nThe age is - {age}.")
if age > 20 or age < 10:
    print("The age is either above 20 or below 10.")
