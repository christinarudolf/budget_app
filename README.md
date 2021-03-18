# budget_app

Budget App project from freeCodeCamp. View full directions [here](https://repl.it/@chrudolf/boilerplate-budget-app-1#README.md).

Uses 'Category' class to create budget objects.

Each budget object has an associated ledger that displays the previous transactions and overall balance in that budget category. The command 'print("Budget object")' will display the ledger.
*Sample object creation: food = budget.Category("Food")

Methods associated with each budget object and input parameters for each method:

- deposit:
  - deposits a given amount into the budget object. Appends the deposit and description to the ledger
  - (required) amount
  - (optional) description
  *Sample input: food.deposit(1000, 'initial deposit')
 
- withdraw:
  - withdraws a given amount from the budget object and appends the withdrawal to the ledger. If the withdrawal amount is great than the balance of the budget object,     then no withdrawal transaction takes place
  - (required) amount. Must be given as a negative number
  - (optional) description
  
  *Sample input: food.withdraw(15.89, "restaurant and more food for dessert")
  
- get_balance:
  - returns the current balance of the budget object. No inputs required
  
  *Sample use: food.get_deposit()

- transfer:
  - withdraws a given amount from the current budget object and deposits it into a different existing budget object. Appends the description 'Transfer to *Destination budget object*' to the source budget object's ledger; appends the description 'Transfer from *Source budget object*' to the destintion object's ledger
  - (required) amount
  - (required) another budget object
  
  *Sample use: food.transfer(50, clothing)

- check_funds:
  - checks whether the given amount exceeds the current balance of the budget object. Returns 'True' if amount is less than the balance; returns 'False' otherwise
  - (required) amount
  
  *Sample use: food.check_funds(500)

There is an additional function 'create_spend_chart' that is not associated with the Category class. 'create_spend_chart' takes a list of budget objects as input and returns a bar chart that displays the percentage of funds spent in each category. This function takes up to four budget objects as input.

*Sample use: print(create_spend_chart([food, clothing, auto]))
