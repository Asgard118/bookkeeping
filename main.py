from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime

current_date = datetime.now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(current_date)