print("Welcome to the Tip Calculator")

def tip_calculator(total_bill_value: float, tip_amount: int, number_of_paying_customers: int) -> None:
    """
    Calculates the total amount of a bill and the tip, divided by the number of paying customers.

    Args:
        * total_bill_value: Total amount consumed
        * tip_amount: Total tip amount (Ex.: 10 = 10%)
        * number_of_paying_customers: Number of people who will split the bill.
    """
    tip_value_perc = tip_amount / 100

    bill_with_tip = total_bill_value * (1 + tip_value_perc)
    divided_bill = bill_with_tip / number_of_paying_customers
    
    print("\n" + "----- BILL-----")
    print(f"> The tip was {tip_amount}%")
    print(f"> The total bill with tip included was {bill_with_tip:.2f}$")
    print(f"> For {number_of_paying_customers} paying customers the divided bill is {divided_bill:.2f}$")

total_bill: float = float(input("What was the total bill? $ "))
tip_value: int = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_paying_people: int = int(input("How many people to split the bill? "))

tip_calculator(total_bill, tip_value, number_of_paying_people)