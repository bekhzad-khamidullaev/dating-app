def calculate_monthly_payment(cost, annual_interest_rate, duration):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    num_payments = duration
    monthly_payment = (cost * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_payment

def main():
    print("Welcome to the leasing calculator!")
    cost = float(input("Enter the cost of the leased item: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    duration = int(input("Enter the duration of the lease in months: "))

    monthly_payment = calculate_monthly_payment(cost, annual_interest_rate, duration)
    print(f"The monthly payment for the lease is: ${round(monthly_payment, 2)}")

if __name__ == "__main__":
    main()
