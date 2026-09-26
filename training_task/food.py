meal1 = (1, 2.50, 'code sandwich', 'green beans', 'french fries')
meal2 = (2, 2.50, 'cheeseburger', 'french fries')
meal3 = (3, 3.00, 'meatloaf', 'mashed potatoes', 'glazed apples', 'steamed carrots')
meal4 = (4, 2.50, 'spaghetti and meatballs', 'broccoli', 'pears')
meal5 = (5, 2.00, 'chicken nuggets', 'macaroni and cheese', 'grapes')

student1 = ('john doe', 54.25)
student2 = ('bob jackson', 235.98)
student3 = ('jill jackson', 93.54)
student4 = ('jackie johnson', 1.05)
student5 = ('darius terrell', 23.92)
student6 = ('maha connor', 5.65)
student7 = ('oskar ruiz', 32.12)
student8 = ('john doe', 54.25)

menu = set()

menu.add(meal1)
menu.add(meal2)
menu.add(meal3)
menu.add(meal4)
menu.add(meal5)

balances = dict()

balances[1] = student1
balances[2] = student2
balances[3] = student3
balances[4] = student4
balances[5] = student5
balances[6] = student6
balances[7] = student7
balances[8] = student8

meals_ordered = list()

def check_all_balances() -> None:
    for id in balances:
        account = balances[id]
        balance = account[1]
        if balance < 10:
            print(f'WARNING: student #{id} has a low balance of {balance}')
        

def find_meal(meal_id: int) -> tuple or None:
    for m in menu:
        if m[0] == meal_id:
            return m


def checkout(student_id: int, meal_id: int) -> tuple or str:
    meal = find_meal(meal_id)
    meal_price = meal[1]
    meal_ordered = meal
    student_account = balances[student_id]

    if meal_price > student_account[1]:
        print(f'student #{student_id} cannot afford lunch today')
        meal_ordered = 'peanut butter and jelly sandwich'
    else: 
        balances[student_id] = (student_account[0], student_account[1]-meal_price)
        print(f'student #{student_id} has ordered meal #{meal_id}')
        print('${meal_price} has been deducted from their balance')
        print(f'their updated balance is {balances[student_id][1]}')
    
    meals_ordered.append(meal_ordered)
    return meals_ordered
    




