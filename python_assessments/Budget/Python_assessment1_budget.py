### from datetime import datetime
class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
    def showExpense(self):
         print(f"{self.date} | {self.category} | ${self.amount} | {self.description}")

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = 0
    
    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense.date} | {expense.category} | ${expense.amount} | {expense.description}")

    def add_expenses_tolist(self,amount,category,description):
        expense= Expense(amount,category,description)
        self.expenses.append(expense)

    def add_budget(self,budget):
        self.budget=budget
    def check_budget(self):
        print(f"budget: {self.budget}")
        
    def set_budget(self, amount):
        self.budget = amount

    def check_budget(self):
        total_spent = sum(float(exp.amount) for exp in self.expenses)
        return self.budget - total_spent
        
    def save_expenses(self, expenses, filename):
        expensesSet= set(expenses) #no duplicates
        expensesList=list(expensesSet);
        try:
            with open(filename, 'w') as file:
                for expense in expensesList:
                   # "30.50","travel","travel expenses" , "date"
                    file.write(f"{expense.amount}|{expense.category}|{expense.description}|{expense.date}\n")
        except FileNotFoundError:
            return []
            
    def load_expenses(self,filename):
        try:
            with open(filename, 'r') as file:
                expenses_data = file.readlines()
                
                return [Expense(*line.strip().split('|')) for line in expenses_data]
           
        except FileNotFoundError:
            return []


def main():
    tracker=ExpenseTracker()
    #When no while loop 
    
    #expense = Expense("20.50", "food", "food expenses")
    #expense.showExpense()
    #print("expense tracker")
    #tracker.add_expenses_tolist("30.50","travel","travel expenses")
    #tracker.add_expenses_tolist("20.50", "food", "food expenses")
    #tracker.view_expenses()
    #tracker.set_budget(500)
    #print(tracker.check_budget())

    #with while loop
    while True:
        choice=int(input("Enter you choice:\n 1: Add Expenses to List\n 2: Set Budget\n 3:Show Expenses\n 4:Check budget\n 5:Load expenses from file\n 6:Save to file\n"))
        if(choice==1):
            amount= float(input("Enter amount:\n"))
            category=input("Enter category:\n")
            description= input("Enter description:\n")
            tracker.add_expenses_tolist(amount,category,description)
        elif(choice==2):
            budget= float(input("Set Budget:\n"))
            tracker.set_budget(budget)
        elif(choice==3):
            tracker.view_expenses()
        elif(choice==4):
            print("The Budget Available now is:\n")
            print(tracker.check_budget())
        elif(choice==5):
            filename=input("enter the filename to load the data from , file should be in .txt format and\n the data format should be ex: amount|category|description|date")
            tempexpenses= tracker.load_expenses(filename)
            tracker.expenses.extend( tempexpenses)
        elif(choice==6):
            filename=input("enter the filename to save data to:")
            tracker.save_expenses(tracker.expenses, filename)
        else:
            print("not yet implemented")
            break;
        
            
if __name__ == "__main__":
    main()
