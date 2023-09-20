print('TEMA VALIDATOR CNP')

cnp = input('CNP: ')

sex = int(cnp[0])
year = int(cnp[1:3])
month = int(cnp[3:5])
day = int(cnp[5:7])
county = int(cnp[7:9])
NNN_digit = int(cnp[9:12])
control_digit_C = int(cnp[12])

#validam daca CNP are 13 caractere integer
def validate_len_char(cnp):
    if len(cnp) != 13 or not cnp.isdigit():
        print('length/char CNP is not valid!')
        return False
    else:
        print('length/char CNP is valid!')
        return True

#validam daca cifrele pt sex sunt valide
def validate_sex_digit(cnp):
    if sex == 0:
        print('sex CNP is not valid!')
        return False
    else:
        print('sex CNP is valid!')
        return True

#validam daca cifrele pt anul nasterii sunt valide
def validate_year_digit(cnp):
    if year < 00 or year > 99:
        print('year CNP is not valid!')
        return False
    else:
        print('year CNP is valid!')
        return True

# validam daca cifrele pt luna nasterii sunt valide
def validate_month_digit(cnp):
    if month < 1 or month > 12:
        print('month CNP is not valid!')
        return False
    else:
        print('month CNP is valid!')
        return True

# validam daca cifrele pt ziua nasterii sunt valide
def validate_day_digit(cnp):
    if day < 1 or day > 31:
        print('day CNP is not valid!')
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        print('day CNP is not valid!')
        return False
    elif month == 2 and (day > 29) or (day == 29 and not (day % 4 == 0 and (day % 100 != 0 or day % 400 == 0))):
        print('day CNP is not valid!')
        return False
    else:
        print('day CNP is valid!')
        return True

# validam daca cifrele pt judet sunt valide
def validate_county_digit(cnp):
    if 1 <= county <= 46 or county in [51, 52]:
        print('County CNP is valid')
        return True
    else:
        print('County CNP is not valid')
        return False

# validam daca cifrele NNN sunt valide
def validate_NNN_digit(cnp):
    if NNN_digit < 1 or NNN_digit > 999:
        print('NNN CNP is not valid!')
        return False
    else:
        print('NNN CNP is valid!')
        return True

# validam cifra de control "C"
def validate_C_digit(cnp):
    validation_cod = '279146358279'
    control_no = 0

    for i in range(12):
        cnp_digit = int(cnp[i])
        validation_C = int(validation_cod[i])
        control_no += cnp_digit * validation_C

    rest = control_no % 11

    if rest == 10:
        control_no = 1
        print('C digit CNP is valid!')
        return True
    elif rest == control_digit_C:
        print('C digit CNP is valid!')
        return True
    else:
        print('C digit CNP is not valid!')
        return False

# validam intregul CNP
def validate_cnp(cnp):
    validations = [
        validate_len_char(cnp),
        validate_sex_digit(cnp),
        validate_year_digit(cnp),
        validate_month_digit(cnp),
        validate_day_digit(cnp),
        validate_county_digit(cnp),
        validate_NNN_digit(cnp),
        validate_C_digit(cnp)
    ]

    return all(validations)

if validate_cnp(cnp):
    print(f'Your CNP {cnp} is valid!')
else:
    print(f'Your CNP {cnp} is not valid!')







