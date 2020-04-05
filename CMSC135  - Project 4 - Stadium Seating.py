# Purpose: To make a program that will utilize the "function" of python.
# This prorgam will ask how many tickets for each class of seats sold, then
# displays the amount of income generated from ticket sales.


# Global Constants
COSTOFCLASSASEATS = float(20.00) # Class A seats cost $20.00
COSTOFCLASSBSEATS = float(15.00) # Class B seats cost $15.00
COSTOFCLASSCSEATS = float(10.00) # Class C seats cost $10.00

# Define Function
def main():
    # Variables to hold how many seats of each class were sold
    countASeats = int(input("Enter count of A seats: ")) # Hold class A
    countBSeats = int(input("Enter count of B seats: ")) # Hold class B
    countCSeats = int(input("Enter count of C seats: ")) # Hold class C
    ShowIncome(countASeats, countBSeats, countCSeats) # Call the ShowIncome Function


def ShowIncome(countA, countB, countC):
    totalIncome = float(0.00) # Variable to hold the total income made

    seatAIncome = countA * COSTOFCLASSASEATS #Class A income calculation
    totalIncome += seatAIncome # Adds the class A income to total income

    # Display the income from Class A seats
    print("Income from class A seats: $", format(seatAIncome, ".2f"))
    seatBIncome = countB * COSTOFCLASSBSEATS #Class B income calculation
    totalIncome += seatBIncome # Adds the class B income to total income

    # Display the income from Class B seats
    print("Income from class B seats: $", format(seatBIncome, ".2f"))
    seatCIncome = countC * COSTOFCLASSCSEATS #Class C income calculation
    totalIncome += seatCIncome # Adds the class C income to total income

    # Display the income from Class C seats
    print("Income from class C seats: $", format(seatAIncome, ".2f"))

    # Display the total income from all seat sales
    print("Total Income : $", totalIncome)

main()
input("please enter")
