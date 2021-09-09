FHA_MININUM = 3.5

class RealEstateCalc:
    def __init__(self, cost, num_plex, rental_value_per_plex):
        self.cost = cost
        self.num_plex = num_plex
        self.rental_value_per_plex = rental_value_per_plex
        self.principal = self.cost
    
    def get_down_payment(self, percent_down=FHA_MININUM):
        return self.cost * (percent_down / 100.0)
    
    def get_principal(self, percent_down=FHA_MININUM):
        return self.cost - self.get_down_payment(percent_down)
    
    def get_mortgage_magic(self, r, n):
        numerator = r * pow(1 + r, n)
        denominator = pow(1 + r, n) - 1
        magic = (numerator / denominator)
        return magic
    
    def get_mortgage_monthly(self, interest_rate=3.05, loan_term_years=30, percent_down=FHA_MININUM):
        monthly_interest_rate = (interest_rate / 100.0) / 12.0
        total_loan_payments = loan_term_years * 12
        mortgage_magic = self.get_mortgage_magic(monthly_interest_rate, total_loan_payments)

        return self.get_principal(percent_down) * mortgage_magic
    
    def get_cash_flow(self, percent_down=FHA_MININUM):
        after_expenses = (self.num_plex * self.rental_value_per_plex) / 2.0
        return after_expenses - self.get_mortgage_monthly(percent_down)
    
    def generate_report(self, percent_down=FHA_MININUM):
        total_income = self.num_plex * self.rental_value_per_plex
        mortgage_monthly = self.get_mortgage_monthly(percent_down)
        principal = self.get_principal(percent_down)
        down_payment = self.get_down_payment(percent_down)
        cash_flow = self.get_cash_flow(percent_down)
        cash_flow_per_plex = cash_flow / self.num_plex

        print("Property Breakdown:")
        print("\tRentable Units: {}".format(self.num_plex))
        print("\tIncome per Unit: ${:.2f} /mo".format(self.rental_value_per_plex))
        print("\tTotal Income: ${:.2f} /mo\n".format(total_income))

        print("\tMortgage: ${:.2f} /mo".format(mortgage_monthly))
        print("\tDown: ${:.2f}".format(down_payment))
        print("\tPrincipal: ${:.2f}\n".format(principal))
        print("\tCash Flow: ${:.2f} /mo".format(cash_flow))
        print("\tCash Flow per Unit: ${:.2f} /mo".format(cash_flow_per_plex))

        if cash_flow_per_plex > 300:
            print("\t\tExcellent cash flow.")
        elif cash_flow_per_plex > 200:
            print("\t\tGreat cash flow.")
        elif cash_flow_per_plex > 100:
            print("\t\tGood cash flow.")
        elif cash_flow_per_plex > 0:
            print("\t\tPositive cash flow.")
        elif cash_flow_per_plex == 0:
            print("\t\tBreak-even cash flow.")
        elif cash_flow_per_plex < 0:
            print("\t\tNegative cash flow.")

if __name__ == "__main__":
    try:
        cost = int(input("Cost of property (numeric, e.g., 299900): "))
    except:
        print("Invalid number. Assuming 299000\n")
        cost = 299000
    
    try:
        num_plex = int(input("Number of rentable units (numeric, e.g., 2 = Duplex): "))
    except:
        print("Invalid number. Assuming 2\n")
        num_plex = 2
    
    try:
        avg_rent = int(input("Expected income per unit (numeric, e.g., 2000): "))
    except:
        print("Invalid number. Assuming 2000\n")
        avg_rent = 2000
    
    try:
        percent_down = float(input("Percent down (numeric, e.g., 3.5): "))
    except:
        print("Invalid number. Assuming 3.5\n")
        percent_down = 3.5

    comp = RealEstateCalc(cost, num_plex, avg_rent)
    comp.generate_report(percent_down)