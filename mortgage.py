def mortgage():
    loanAmount = 1
    while loanAmount != 0:
        loanAmount = float(input("Enter the loan amount, <= 0 to exit: "))
        if loanAmount > 0:
            interestRate = float(input("Enter the loan interest rate % : "))
            loanTerm = float(input("Enter the loan term (number of years): "))
            monthlyRate = (interestRate / 100) / 12
            numPayments = loanTerm * 12
            monthlyPayment = loanAmount * (monthlyRate * pow((1 + monthlyRate), numPayments)) / (pow((1 + monthlyRate), numPayments) - 1)
            totalPayment = monthlyPayment * (loanTerm * 12)
            interestPaid = totalPayment - loanAmount
            print(f"For the loan amount of ${loanAmount:,.2f} for {loanTerm} years with interest rate of {interestRate}%")
            print(f"The monthly payment is ${monthlyPayment:,.2f}")
            print(f"Total amount paid for this loan ${totalPayment:,.2f}")
            print(f"Total interest paid for this loan is ${interestPaid:,.2f}")
            print()
        else:
            print("Exiting Mortgage Program ...")




