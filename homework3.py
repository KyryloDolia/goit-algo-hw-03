from datetime import datetime
import random

def get_days_from_today(date):
    try:
        form_date = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        days_from_today = today_date - form_date
        return days_from_today.days
    
    except ValueError:
        print("Неправильний формат вводу. Має бути - 'РРРР-ММ-ДД'")


def get_numbers_ticket(min, max, quantity):
    try:
        if 1 <= min <= 1000 and 1 <= max <= 1000:
            return sorted(random.sample(range(min, max + 1), quantity))
        else:
            return []
    except:
         return []

