days_in_month = {
    "January": 31, 
    "February": 28, 
    "March": 31, 
    "April": 30,
    "May": 31,
    "June": 30, 
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31, 
    "November": 30,
    "December": 31
}

days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def first_of_next_month(month, first_day_of_month, year):
    if month == "February" and year % 4 == 0:
        first_day_of_month = days_in_week[(days_in_week.index(first_day_of_month) + ((days_in_month[month] + 1) % 7)) % 7]
    else:
        first_day_of_month = days_in_week[(days_in_week.index(first_day_of_month) + (days_in_month[month] % 7)) % 7]
    month = list(days_in_month.keys())[(list(days_in_month.keys()).index(month) + 1) % 12]

    if month == "January":
        year += 1

    return (month, first_day_of_month, year)

