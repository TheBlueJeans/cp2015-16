name = input("Please enter name: \n")
hours = float(input("Please enter the number of hours worked weekly: \n"))
rate = float(input("Please enter the hourly pay rate ($): \n"))
CPF = float(input("Please enter the CPF contribution rate (%): \n"))
print("\nPayroll statement for {0}: \n".format(name))
print("Number of hours worked in a week:", hours)
print("Hourly pay rate: ${0}".format(rate))
print("Gross pay: ${0}".format(round(rate*hours, 2)))
print("CPF contribution at {0}%".format(CPF))
print("\nNet pay: ${0}".format(round(rate*hours/100*(100-CPF), 2)))
