
def interest():
    p = int(1)
    while p != 0:
        p = float(input("Enter the starting principle, <= 0 to exit: "))
        if p > 0:
            r = float(input("Enter the annual interest rate: "))
            n = int(input("How many times per year will the interest be compounded? "))
            t = float(input("For how many years will the account earn interest? "))
            total = p * (1 + float(r/100)/n) ** (n * t)
            interest = total - p
            print(f"At the end of {t} years you will have ${total:,.2f} with interest earned ${interest:,.2f}")
            print()
        else:
            print("program exiting ....")



