class Checkbook:
    """
    A class to simulate a simple checkbook with deposit, withdrawal, and balance tracking functionality.
    """

    def __init__(self):
        """
        Initializes the Checkbook with an initial balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Parameters:
        amount (float): The amount to be deposited.

        Prints a confirmation of the deposit and the current balance.
        """
        if amount <= 0:
            print("Amount to deposit must be greater than zero.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook, if sufficient funds exist.

        Parameters:
        amount (float): The amount to be withdrawn.

        Prints a confirmation of the withdrawal and the current balance. If insufficient funds, it prints an error.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance in the checkbook.

        Prints the current balance in a formatted way.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to simulate a checkbook where the user can deposit, withdraw, check balance, or exit.
    """
    cb = Checkbook()  # Create an instance of the Checkbook class
    while True:
        # Ask the user what action they want to perform
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            print("Exiting the checkbook program. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
