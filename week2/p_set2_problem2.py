
# balance = 3926
# annulInterestRate = 0.2
# monthly_interest_rate = annulInterestRate / 12.0


def find_minimum_monthly_payment_payoff(balance, annualInterestRate, n):
    """

    :param balance: type float, the outstanding balance on the credit card
    :param annulInterestRate: annual interest rate as a decimal
    :param n: pay constant monthly_payment each month, then pay off a credit card balance
        within n months
    :return:
    """
    monthly_interest_rate = annualInterestRate / 12.0

    def remaining_balance(balance, monthly_payment, n):
        """

        :param balance: type float, the outstanding balance on the credit card
        :param monthly_payment: type int, the payment each month, is does not
            change each month
        :param n: type int, n-th month
        :return: type float, remaining balance after pay monthly_payment each month
            after n month
        """
        monthly_unpaid_balance = balance - monthly_payment
        updated_balance = monthly_unpaid_balance + monthly_unpaid_balance * monthly_interest_rate
        if n == 1:
            return updated_balance
        else:
            return remaining_balance(updated_balance, monthly_payment, n-1)

    test_monthly_payment = 10
    while True:
        if remaining_balance(balance, test_monthly_payment, n) < 0:
            break
        else:
            test_monthly_payment += 10

    print("Lowest Payment: " + str(test_monthly_payment))

balance = 3926
annualInterestRate = 0.2
find_minimum_monthly_payment_payoff(balance, annualInterestRate, n=12)
