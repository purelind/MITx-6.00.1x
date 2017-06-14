# def remaining_balance():
#     """
#
#     :return:
#     """
#     balance = int(input("balance = "))
#     annual_interest_rate = float(input("annulInterestRate = "))
#     monthly_payment_rate = float(input("monthlyPaymentRate = "))
#     monthly_interest_rate = annual_interest_rate / 12.0
#
#
#     def remaining_balance_recur(balance, n):
#         minimum_monthly_payment = monthly_payment_rate * balance
#         monthly_unpaid_balance = balance - minimum_monthly_payment
#         updated_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
#         if n == 1:
#             return updated_balance
#         else:
#             return remaining_balance_recur(updated_balance, n-1)
#     remaining = remaining_balance_recur(balance, 12)
#     print("\nRemaining balance: " + str(round(remaining, 2)))
#     return remaining
#
# remaining_balance()






balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthly_interest_rate = annualInterestRate / 12.0


def remaining_balance_recur(balance,n):
    minimum_monthly_payment = monthlyPaymentRate * balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    updated_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    if n == 1:
        return updated_balance
    else:
        return remaining_balance_recur(updated_balance, n-1)

remaining = remaining_balance_recur(balance, 12)
print("\nRemaining balance: " + str(round(remaining, 2)))

