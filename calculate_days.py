from sys import argv
from datetime import date, timedelta as td

def process_date(datestring: str):
    nums = datestring.split('-')
    nums = [int(num) for num in nums]
    return date(nums[2], nums[1], nums[0])

def parse_line(line: str):
    line = line.split()
    out = process_date(line[0])
    back = process_date(line[1])
    return out, back

def time_between_two_dates(out, back):
    return (back - out).days - 1

def calculate_start_date(end_date, period):
    # Add support for months, weeks, days and leap years
    if period[-1] == 'y':
        return end_date - td(365*int(period[:-1]) - 1)


def calculate_absences(filename: str, end_date, period: str):
    total_absences = 0
    start_date = calculate_start_date(end_date, period)
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '#':
                pass
            else:
                out, back = parse_line(line)
                if back > start_date:
                    if out > start_date:
                        total_absences += time_between_two_dates(out, back)
                    else:
                        total_absences += time_between_two_dates(start_date, back)
    return total_absences

def print_answer(ans: int):
    print(f"Total number of days absent is {ans}")

if __name__ == '__main__':
    if len(argv) == 1:
        print("Need file path")
    elif len(argv) == 2:
        print_answer(calculate_absences(argv[1], date.today(), '5y'))
    else:
        end_date = process_date(argv[2])
        if len(argv) == 3:
            print_answer(calculate_absences(argv[1], end_date, '5y'))
        else:
            print_answer(calculate_absences(argv[1], end_date, argv[3]))
