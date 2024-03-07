from datetime import datetime

def has_passed(input_date_time):
    input_datetime = datetime.strptime(str(input_date_time), '%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.now()
    expired = input_datetime < current_datetime    
    return expired