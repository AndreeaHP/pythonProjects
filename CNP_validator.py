print('TEMA VALIDATOR CNP')

cnp = input('CNP: ')
def validate_cnp(cnp):
    if len(cnp) != 13 or not cnp.isdigit():
        return False
    else:
        return True

validation = validate_cnp(cnp)
if validation:
    print('CNP is valid!')
else:
    print('CNP is not valid!')

def validate_sex_digit(cnp):
    if cnp[0] == '0':
        return False
    else:
        return True
validate_sex = validate_sex_digit(cnp)
if validate_sex:
    print('CNP is valid!')
else:
    print('CNP is not valid!')

#validam daca cifrele pt anul nasterii sunt valide
def validate_year_digit(cnp):
    if int(cnp[1:3]) < 00 or int(cnp[1:3]) > 99:
        return False
    else:
        return True
validate_year = validate_year_digit(cnp)
if validate_year:
    print('CNP is valid!')
else:
    print('CNP is not valid!')

# validam daca cifrele pt luna nasterii sunt valide
def validate_month_digit(cnp):
    if int(cnp[3:5]) < 0o1 or int(cnp[3:5]) > 12:
        return False
    else:
        return True
validate_month = validate_month_digit(cnp)
if validate_month:
    print('CNP is valid!')
else:
    print('CNP is not valid!')

# validam daca cifrele pt ziua nasterii sunt valide
def validate_day_digit(cnp):
    if int(cnp[5:7]) < 1 or int(cnp[5:7]) > 31:
        return False
    elif cnp[3:5] in ['04', '06', '09', '11'] and cnp[5:7] == '31':
        return False
    # elif int(cnp[3:5]) == ['02'] and #validam anul bisect
    else:
        return True
validate_day = validate_day_digit(cnp)
if validate_day:
    print('CNP is valid!')
else:
    print('CNP is not valid!')

# validam daca cifrele pt judet sunt valide
def validate_county_digit(cnp):
    if cnp[7:9] < 1 or cnp[7:9] > 46 or != ['51', '52']:
        return False
    else:
        return True
validate_day = validate_day_digit(cnp)
if validate_day:
    print('CNP is valid!')
else:
    print('CNP is not valid!')


#if validare_sex & validare_an & validare_luna & celelalte validari (zi, judet, cod): return False  = pentru a pune toate validari intr-un If

# 0123456789
# SAAMMDDJJ
# 2850302270061




