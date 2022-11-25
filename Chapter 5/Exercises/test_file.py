# Finger exercise
# Write code that asks the user to enter their birthday
#  in the form mm/dd/yyyy, and then prints a string of 
# the form ‘You were born in the year yyyy.’

date_of_birth = input("Input your birthday as DD/MM/YYYY: ")
year_of_birth = (date_of_birth[-4:])
print(f"You were born in the year - {year_of_birth}.")