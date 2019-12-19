import datetime
if __name__ == '__main__':
    from application.salary import calculate_salary as calculating
    from application.Директория.people import get_employees as all_employees
    print("Текущая дата: ", datetime.datetime.now())
