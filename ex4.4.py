def gen_secs():
    """
    Generator that yields all possible seconds in a minute (0-59).
    """
    for sec in range(60):
        yield sec


def gen_minutes():
    """
    Generator that yields all possible minutes in an hour (0-59).
    """
    for minute in range(60):
        yield minute


def gen_hours():
    """
    Generator that yields all possible hours in a day (0-23).
    """
    for hour in range(24):
        yield hour


def gen_time():
    """
    Generator that yields all possible times in a day (hh:mm:ss format).
    Combines the gen_hours, gen_minutes, and gen_secs generators.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=2019):
    """
    Generator that yields years starting from 'start' (default 2019) and continues indefinitely.
    """
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    """
    Generator that yields all months in a year (1-12).
    """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generator that yields all days in a given month.
    Takes into account whether it's a leap year or not.

    Args:
    - month (int): The month (1-12).
    - leap_year (bool): Whether it's a leap year (default True).
    """
    # Days in each month
    days_in_month = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for day in range(1, days_in_month[month - 1] + 1):
        yield day


def is_leap_year(year):
    """
    Function to determine if a given year is a leap year.

    Args:
    - year (int): The year to check.

    Returns:
    - bool: True if leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def gen_date():
    """
    Generator that yields full datetime stamps in the format dd/mm/yyyy hh:mm:ss.
    Combines the year, month, day, hour, minute, and second generators.
    """
    for year in gen_years():
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


# Test the generator by printing every millionth date-time stamp
if __name__ == "__main__":
    date_gen = gen_date()
    for i in range(1, 5000001):  # Limiting the number of iterations for practical reasons
        current_date = next(date_gen)
        if i % 1000000 == 0:
            print(current_date)
