def line_for_table():
    print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format("+", "-" * 20, "+", "-" * 20, '+'))

def header_table():
    line_for_table()
    print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', 'x', "|", 'y', '|'))
    line_for_table()
