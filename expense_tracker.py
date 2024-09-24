from expense import Expense
from datetime import datetime
from text_formatting import green,red,blue,bold
from months import monthofyear
from clear_program import clear_file
import calendar

def main():

#getting date and time
    today = datetime.now()
    current_month = today.month
    total_days_in_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = total_days_in_month - today.day
#***********************************************************************

    print()
    print(bold(f'\n   🎯Welcome to Expense Tracker!🥰'))
    print('      ************************')


    budget = int(input('\n▶Enter your Monthly Budget🤑:'))



    safe_spend=budget//remaining_days
    print(f'▶Safe amount to spend:',end=' ')
    print(blue(f'Rs.{safe_spend}/day'))

#create file path
    file_path="expense_data.csv"

#calling expense_returned function
    expense_returned=expense_details()

#calling save_to_file function
    save_to_file(expense_returned,file_path)

#calling budget_summery function
    budget_summery(file_path,budget,remaining_days,current_month)

    option(file_path)

#*****************************************************************************


#get user input for expense details.

def expense_details():

#collecting name
    product_name=input('\n1.Enter the name of product😻:')
    print(f"➡Product Name: {product_name} ")

#collecting amount
    product_expense=float(input('2.Enter the Amount of the product💸:'))
    print(f"➡Amount of the {product_name} is ₹{product_expense}")

#category part
    category_list=[
        '🤤Food',
        '🏡Home',
        '🚙Car',
        '💼Work',
        '🎉Fun',
        '🌟Others'
    ]
#while True loop, loop brakes when the return works
    while True:
        print('\n3.Enter the category of the product below📜')
        for i,categories in enumerate(category_list,1):
            print(f'          {i}.{categories}')
        selected_category=int(input("⭕Enter the category here ➡ "))-1
        if selected_category in range(len(category_list)):
            category_name=category_list[selected_category]
            expense_from_class=Expense(name=product_name,category=category_name,amount=product_expense)
            return expense_from_class
        else:
            print()
            print('*'*100)
            # Printing bold and underlined green text

            print(f'🔴Invalid category ! select from [1 to {len(category_list)}]🔴\n')
#**********************************************************************************************************8


#write it to a file.
def save_to_file(expense_returned,file_path):

    with open(file_path,"a") as f:
        f.write(f'{expense_returned.name},{expense_returned.category},{expense_returned.amount}\n')
#*************************************************************************************************************

#reading and summerizing part
def budget_summery(file_path,budget,remainig_days,cur_month):
    print("\n📓HERE IS THE SUMMERY OF YOUR EXPENSES📓")
    expense_list=[]

    with open(file_path,"r") as f:
        lineBYread=f.readlines()


        for i in lineBYread:
            item,cat,amt=i.rstrip('\n').split(',')
            summery_class_ob=Expense(name=item,category=cat,amount=float(amt))
            expense_list.append(summery_class_ob)

    item_dic={}
    for i in expense_list:
        key=i.category
        if key not in item_dic:
            item_dic[key]=i.amount
        else:
            item_dic[key]+=i.amount
    print(f"\n📃Your spending on each category are:\n")
    for k,v in item_dic.items():
        print(f'  {k}:₹{v}/.')
    total_spend=0
    for i in item_dic:
        total_spend+=item_dic[i]
    month_return=monthofyear(cur_month)
    print(f"\n{month_return} spends💰:",end=' ')
    print(red(total_spend))

    bal=budget-total_spend
    convert_negative = abs(bal)

    if bal<0:
        print(red(f"\n⚠You've Exceeded ₹{convert_negative} from your monthly Budget⚠"))
    else:
        print(green(f"Balance amount:₹.{bal}"))

        safe_spend=bal//remainig_days
        print(f"Safe to spend the remaining day=",end=' ')
        print(blue(f'₹{int(safe_spend)}/day'))
    print('*'*100,'\n')

# delete file data
def option(path):
    print("\nChoose an option:")
    print("1. Clear the file")
    print("2. Exit")


    option = input("Enter the number of your choice: ").strip()

    if option == '1':
        clear_file(path)
    elif option == '2':
        print("Exiting the program.")
    else:
        print("Invalid option. Please choose a valid option.")

if __name__=='__main__':
    main()
