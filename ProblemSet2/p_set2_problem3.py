def find_minimum_monthly_payment_payoff(balance, annualInterestRate, n=12):
    """

    :param balance: type float, the outstanding balance on the credit card
    :param annulInterestRate: annual interest rate as a decimal
    :param n: pay constant monthly_payment each month, then pay off a credit card balance
        within n months
    :return:
    """
    monthly_interest_rate = annualInterestRate / 12

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

    monthly_payment_low = balance / 12.0
    monthly_payment_upper = balance * (1 + monthly_interest_rate)**12 / 12

    while monthly_payment_low <= monthly_payment_upper:
        monthly_payment_mid = (monthly_payment_low + monthly_payment_upper) / 2.0
        if remaining_balance(balance, monthly_payment_mid, n) > 0:
            monthly_payment_low = monthly_payment_mid
        elif remaining_balance(balance, monthly_payment_mid, n) < -0.01:
            monthly_payment_upper = monthly_payment_mid
        else:
            break

    print("Lowest Payment: " + str(round(monthly_payment_mid, 2)))

balance = 999999
annualInterestRate = 0.18
find_minimum_monthly_payment_payoff(balance, annualInterestRate)
