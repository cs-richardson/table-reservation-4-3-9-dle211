"""
This program asks the user for their name, then it compares the name to the
name of the reservation, and then it tells the user if there's a table reserved
for them or not.
"""

# Asks the user for their name
name = input("Name: ")
reservation_name = "Justin"

# If the name is Justin, then there's a table reserved for them.
if name == "Justin":
    print "Right this way!"

# Otherwise, there is no table reserved for them.
else:
    print "Sorry, we don't have a reservation under that name."
