#Name = Sebastian Murga
#Period = PM
#Theme Park Admission & Ride Eligibility System

#welcome message
print("Welcome to the Sammy Python Adventure Park!")
print("We're going to get your ticket ready at the sammy park.")
print("We'll also find out which rides you can go on!")

# questions for guest info
guest_name = input("Whats your name? ")
age = int(input("How old are you? "))
height = int(input("How tall are you in inches? "))
ticket_type = input("Ticket type (regular or premium): ")
park_member = input("Are you a park member? ")
visiting_with_adult = input("Are you visiting with an adult: ")
visit_time = input("What time are you visiting? (morning or evening): ")
print()

# admission cost based on age
def calculate_admission(guest_age):
    if guest_age <= 4:
        return 0
    elif guest_age <= 12:
        return 15
    elif guest_age <= 64:
        return 30
    else:
        return 20

# member discount
def calculate_discount(price, member, time_of_day):
    if member == "yes" and time_of_day == "evening":
        discount = 10
    elif member == "yes":
        discount = 5
    elif time_of_day == "evening":
        discount = 3
    else:
        discount = 0
    total_price = price - discount

    #make sure no nagatives
    if total_price < 0:
        total_price = 0
    return total_price

# what rides can dey ride
def ride_level(guest_age, guest_height):
    if guest_height >= 54 and guest_age >= 16:
        return "Extreme Rides"
    elif guest_height >= 48 and guest_age >= 12:
        return "Thrill Rides"
    elif guest_height >= 42 and guest_age >= 8:
        return "Family Rides"
    elif guest_height >= 36:
        return "Kiddie Rides"
    else:
        return "No Rides"

# do dey got an adult
def check_supervision(guest_age, has_adult):
    if guest_age < 13 and has_adult != "yes":
        return "Adult Required"
    else:
        return "Approved"

# price and ride lvls
base_price = calculate_admission(age)
final_price = calculate_discount(base_price, park_member, visit_time)
qualifying_ride = ride_level(age, height)
supervision_status = check_supervision(age, visiting_with_adult)

if ticket_type == "premium":
    perk_message = "Premium ticket: Free food and skip the lines"
else:
    perk_message = "Standard ticket: No free food and skip the line"

# print report
print("PYTHON ADVENTURE PARK GUEST REPORT")
print()
print("Guest Name: " + guest_name)
print()
print("Age: " + str(age))
print("Height: " + str(height) + " inches")
print("Ticket Type: " + ticket_type)
print("Park Member: " + park_member)
print()
print("Base Admission: $" + str(base_price))
print("Final Admission: $" + str(final_price))
print()
print("Highest Ride Level: " + qualifying_ride)
print()
print("Supervision Status: " + supervision_status)
print()
print("Perks: " + perk_message)
print()
print("Have an awesome day at Python Adventure Park")
print()
print()

# fun little personalized message
if qualifying_ride == "Extreme Rides":
    print(guest_name + ", you can rides at the park, have fun")
elif qualifying_ride == "No Rides":
    print("Sorry " + guest_name + ", but you cannot ride any rides")
else:
    print("Have fun " + guest_name + "!")