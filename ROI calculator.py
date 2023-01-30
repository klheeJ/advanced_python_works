class ROI_calculator():
    def __init__(self, income, expenses, cash_flow, CAC, CAC_ROI):
        self.income = income
        self.expenses = expenses
        self.expenses = cash_flow
        self.CAC = CAC
        self.CAC_ROI = CAC_ROI
    
    def income_generator(self):
        rent = input("How much is the rent? ")
        parking = input("How much for parking? ")
        laundry = input("How much for laundry? ")
        self.CAC_ROI = {"rent":self.income}
        self.CAC_ROI["rent"] = self.income + int(rent) + int(parking) + int(laundry)
        print("Your total monthly income is: $" + str(self.CAC_ROI["rent"]))

    def expenses_generator(self):
        tax = input("How much is tax? ")
        utilities = input("How much for utilities? ")
        HOA = input("How much for HOA? ")
        self.CAC_ROI["expenses"] = self.expenses + int(tax) + int(utilities) + int(HOA)
        print("Your total monthly expense is: $" + str(self.CAC_ROI["expenses"]))

    def cash_flow_generator(self):
        new_cash_flow = self.CAC_ROI["rent"] - self.CAC_ROI["expenses"]
        self.cash_flow = new_cash_flow
        self.CAC_ROI["cash flow"] = self.cash_flow
        print("Your monthly cash flow is: $" + str(self.CAC_ROI["cash flow"]))
        yearly_cash_flow = self.cash_flow *12
        self.CAC_ROI["yearly cash flow"] = yearly_cash_flow
        print("Your yearly cash flow is: $" + str(self.CAC_ROI["yearly cash flow"]))

    def CAC_generator(self):
        print("Please answer the following questions in total costs (not monthly).")
        down_payment = input("How much was the down payment? ")
        closing_cost = input("How much was the closing cost? ")
        rehab_budget = input("How much for rehab budget? ")
        misc_cost = input("How much of any miscellaneous costs? ")
        self.CAC_ROI["CAC"] = self.CAC + int(down_payment) + int(closing_cost) + int(rehab_budget) + int(misc_cost)
        print("Your total investment cost is $" + str(self.CAC_ROI["CAC"]))
        calculated_CAC = (self.CAC_ROI["yearly cash flow"]/self.CAC_ROI["CAC"]) * 100
        self.CAC_ROI["CAC ROI"] = calculated_CAC
        print("Your cash on cash ROI per year is: " + str(self.CAC_ROI["CAC ROI"]) + "%")

investment = ROI_calculator(0, 0, 0, 0, {})

def run():
        print("Please answer these questions per month unless specifically stated per year.")
        investment.income_generator()
        investment.expenses_generator()
        investment.cash_flow_generator()
        investment.CAC_generator()

run()


