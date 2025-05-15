from bank_accounts import *

Umanga = BankAccount(1000, "Umanga")
Sara = BankAccount(2000, "Sara")

Umanga.getBalance()
Sara.getBalance()

Sara.deposit(500)

Umanga.withdraw(100)

Umanga.transfer(100,Sara)

Jimmy = InterestRewardsAcct(1000, "Jimmy")

Jimmy.getBalance()

Jimmy.deposit(100)

Jimmy.transfer(100, Umanga)

Ramu = SavingsAcct(1000, "Ramu")

Ramu.getBalance()

Ramu.deposit(100)

Ramu.transfer(1000, Sara)
Ramu.transfer(200,Sara)