# Version 1: Initial version - basic input and output

# Collect user inputs
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

# Combine first and last name
full_name = first_name + " " + last_name

# Display raw output without formatting
print("\n--- Formatted Output ---")
print("Name:", full_name)
print("Name Code:", full_name)
print("Section:", section)
print("Favorite Subject:", favorite_subject)
print("Character Count:", len(full_name))
