#tehdään ohjelma joka luo pankki tilin ja sinne voi tallettaa ja sieltä voi nostaa rahaa
class Account:
    def __init__(self, initial_balance: float = 0):
        if initial_balance < 0:
            raise ValueError("Alkusaldo ei voi olla negatiivinen.")
        self._balance = initial_balance

    def get_balance(self) -> float:
        return self._balance

    def add(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Lisättävä summa ei voi olla negatiivinen.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Nostettava summa ei voi olla negatiivinen.")
        if amount > self._balance:
            raise ValueError(f"Sorry, you have only {self._balance}€, the withdrawal cannot be completed.")
        self._balance -= amount
        return self._balance

# Luo tilin annetulla alkusaldoilla, käsittelee mahdolliset virheet
def create_account(initial_balance: float = 0) -> Account:
    try:
        return Account(initial_balance)
    except ValueError as e:
        print(f"Virhe tilin luonnissa: {e}")
        return Account()

# Käsittelee rahan lisäämisen tilille
def handle_add(account: Account) -> None:
    try:
        amount = float(input("How many euros will be added? "))
        account.add(amount)
    except ValueError as e:
        print(f"Virhe lisättäessä summaa: {e}")

# Käsittelee rahan nostamisen tililtä
def handle_withdraw(account: Account) -> None:
    try:
        amount = float(input("How many euros will be withdrawn? "))
        account.withdraw(amount)
    except ValueError as e:
        print(f"{e}")

# Luo tilin ja suorittaa talletuksia ja nostoja
def main():
    account = create_account(2000)
    print("Bank account created.")
    print(f"Bank account balance: {account.get_balance()}€")

    handle_add(account)
    print(f"Bank account balance: {account.get_balance()}€")

    handle_withdraw(account)
    print(f"Bank account balance: {account.get_balance()}€")

    handle_withdraw(account)

if __name__ == "__main__":
    main()

   
