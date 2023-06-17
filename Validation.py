def CorrectCheckText(string):
    return not False in [char.isalpha() for char in string]

def CorrectCheckNumber(string):
    return not False in [char.isdigit() for char in string]