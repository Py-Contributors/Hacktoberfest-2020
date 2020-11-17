from datetime import date, timedelta


def friday_13_in_year(y):
    day = date(y, 1, 1)
    end = date(y, 12, 31)
    one_day = timedelta(days=1)
    while day < end:
        if day.weekday() == 4 and day.day == 13:
            yield day
        day += one_day

print([str(d) for y in range(2000, 2020) for d in friday_13_in_year(y)])
