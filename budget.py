class Category:

    def __init__(self, category_name): 
        self.category_name = category_name
        self.ledger = []

    def get_balance(self):

        balance = 0

        for item in self.ledger:
            number = item["amount"]
            balance += number

        return balance

    def check_funds(self, amount):

        balance = self.get_balance()

        if balance >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

        return self.ledger

    def withdraw(self, amount, description = ""):

        if self.check_funds(amount) == True:

            self.ledger.append({"amount": -1 * amount, "description": description})

            return True

        else:
            return False

    def category_withdrawals(self):
        category_withdrawals = 0
        for item in self.ledger:
            if item["amount"] < 0:
                category_withdrawals += item["amount"]
        return category_withdrawals

    def transfer(self, amount, category):

        if self.check_funds(amount) == True:

            self.ledger.append({"amount" : -amount, "description" : "Transfer to %s" % category.category_name})

            category.ledger.append({"amount" : amount, "description" : "Transfer from %s" % self.category_name})

            return True

        else:
            return False

    def __str__(self):
        str_ledger = ""
        for line in self.ledger:
            description_str = str(line["description"])
            description_str = description_str[:23]
            amount = "{:.2f}".format(line["amount"])
            amount_str = str(amount)
            str_ledger += description_str.ljust(23, " ")
            str_ledger += "{:>7}".format(amount_str)
            str_ledger += "\n"

        return "{0:*^30}".format(self.category_name) + "\n" + str_ledger + "Total: " + str(self.get_balance())

def create_spend_chart(categories):

    total_withdrawals = 0
    spending = []

    #overall spending
    for category in categories:
        for item in category.ledger:
            spent = 0
            if item["amount"] < 0:
                spent += item["amount"]
                spending.append(spent)

    total_withdrawals = sum(spending)

    #chart
    chart = "Percentage spent by category\n"

    row_100 = "100|"
    row_90 = " 90|"
    row_80 = " 80|"
    row_70 = " 70|"
    row_60 = " 60|"
    row_50 = " 50|"
    row_40 = " 40|"
    row_30 = " 30|"
    row_20 = " 20|"
    row_10 = " 10|"
    row_0 = "  0|"
    sep_row = "    "
    cat_names = []
    names_row = ""

    for category in categories:
        #calculate the percent spent in each category
        perc_spent = category.category_withdrawals() / total_withdrawals * 100

        if perc_spent == 100:
            row_100 += " o "
        else:
            row_100 += "   "
        if perc_spent >= 90:
            row_90 += " o "
        else:
            row_90 += "   "
        if perc_spent >= 80:
            row_80 += " o "
        else:
            row_80 += "   "
        if perc_spent >= 70:
            row_70 += " o "
        else:
            row_70 += "   "
        if perc_spent >= 60:
            row_60 += " o "
        else:
            row_60 += "   "
        if perc_spent >= 50:
            row_50 += " o "
        else:
            row_50 += "   "
        if perc_spent >= 40:
            row_40 += " o "
        else:
            row_40 += "   "
        if perc_spent >= 30:
            row_30 += " o "
        else:
            row_30 += "   "
        if perc_spent >= 20:
            row_20 += " o "
        else:
            row_20 += "   "
        if perc_spent >= 10:
            row_10 += " o "
        else:
            row_10 += "   "

        row_0 += " o "
        sep_row += "---"

        cat_names.append(category.category_name)

    maxi = max(cat_names, key=len)

    for x in range(len(maxi)):
        nameStr = '     '
        for name in cat_names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        nameStr += '\n'
        names_row += nameStr
        #names_row = names_row.rstrip()


    chart += row_100 + " \n" + row_90 + " \n" + row_80 + " \n" + row_70 + " \n" + row_60 + " \n" + row_50 + " \n" + row_40 + " \n" + \
    row_30 + " \n" + row_20 + " \n" + row_10 + " \n" + row_0 + " \n" + sep_row + "-" + "\n" + names_row.rstrip() + "  "
    return chart
