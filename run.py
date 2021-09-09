FHA_MININUM = 3.5

class RealEstateCalc:
    def __init__(self, cost, num_plex, rental_value_per_plex):
        self.cost = cost
        self.num_plex = num_plex - 1
        self.rental_value_per_plex = rental_value_per_plex
        self.mortgage_magic = 0.00449044688
        self.principal = self.cost
    
    def get_down_payment(self, percent_down=FHA_MININUM):
        return self.cost * (percent_down / 100.0)
    
    def get_principal(self, percent_down=FHA_MININUM):
        return self.cost - self.get_down_payment(percent_down)
    
    def get_mortgage_monthly(self, percent_down=FHA_MININUM):
        return self.get_principal(percent_down) * self.mortgage_magic
    
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

comp = RealEstateCalc(299900, 3, 2000)
comp.generate_report(3.5)