A short script calculating the number of days absent from the UK, as per UKVI naturalisation guidelines.

Python version: python 3.6 or higher.

Usage:
`python calculate_days.py <path_to_file> <end_date> <period>`

If no end_date and period are supplied, the program assumes today and 5 year period.

Each of the text file rows must be of the format:  
DD-MM-YY DD-MM-YY irrelevant irrelevant irrelevant  
Where the first day is date of leaving the UK, and second date is date of return. 

