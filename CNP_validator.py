print('TEMA VALIDATOR CNP')
#validam daca CNP are 13 caractere integer
cnp = input('CNP: ')
def validate_len_char(cnp):
    if len(cnp) != 13 or not cnp.isdigit():
        print('length/char CNP is not valid!')
        return False
    else:
        print('length/char CNP is valid!')
        return True

#validam daca cifrele pt sex sunt valide
def validate_sex_digit(cnp):
    if cnp[0] == '0':
        print('sex CNP is not valid!')
        return False
    else:
        print('sex CNP is valid!')
        return True

#validam daca cifrele pt anul nasterii sunt valide
def validate_year_digit(cnp):
    if int(cnp[1:3]) < 00 or int(cnp[1:3]) > 99:
        print('year CNP is not valid!')
        return False
    else:
        print('year CNP is valid!')
        return True

# validam daca cifrele pt luna nasterii sunt valide
def validate_month_digit(cnp):
    if int(cnp[3:5]) < 1 or int(cnp[3:5]) > 12:
        print('month CNP is not valid!')
        return False
    else:
        print('month CNP is valid!')
        return True

# validam daca cifrele pt ziua nasterii sunt valide
def validate_day_digit(cnp):
    if int(cnp[5:7]) < 1 or int(cnp[5:7]) > 31:
        print('day CNP is not valid!')
        return False
    elif cnp[3:5] in ['04', '06', '09', '11'] and cnp[5:7] == '31':
        print('day CNP is not valid!')
        return False
    # elif int(cnp[3:5]) == ['02'] and #validam anul bisect
    else:
        print('day CNP is valid!')
        return True

# validam daca cifrele pt judet sunt valide
def validate_county_digit(cnp):
    if int(cnp[7:9]) < 1 or int(cnp[7:9]) > 46 or cnp[7:9] not in ['51', '52']:
        print('county CNP is valid!')
        return True
    else:
        print('county CNP is not valid!')
        return False

# validam daca cifrele NNN sunt valide
def validate_NNN_digit(cnp):
    if int(cnp[9:12]) < 1 or int(cnp[9:12]) > 999:
        print('NNN CNP is not valid!')
        return False
    else:
        print('NNN CNP is valid!')
        return True

def validate_cnp(cnp):
    validate_len_char(cnp)
    validate_sex_digit(cnp)
    validate_year_digit(cnp)
    validate_month_digit(cnp)
    validate_day_digit(cnp)
    validate_county_digit(cnp)
    validate_NNN_digit(cnp)

validate_cnp(cnp)



#if validare_sex & validare_an & validare_luna & celelalte validari (zi, judet, cod): return False  = pentru a pune toate validari intr-un If







