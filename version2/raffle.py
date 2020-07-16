"""Randomly pick customer and print customer info"""

from random import choice
from customers import get_customers_from_file

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))


def run_raffle():
    """Run the weekly raffle."""

    customers_ = get_customers_from_file("customers.txt")
    pick_winner(customers_)

# Hint: remember to import any functions you need from
# other files or libraries

if __name__ == "__main__":
    run_raffle()