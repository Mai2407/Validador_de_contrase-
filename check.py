import re

password = re.compile(r'''(
     ^(?=.* [A-Z].*[A-Z])
     (?=.*[!@#$&*])
     (?=.*[0-9].*[0.9])
     ([a-z].*[a-z].*[a-z])
     .{10,}
     $
     )''', re.VERBOSE)


#Pide la clave por pantalla y validad si es weak o strong
def PasswordCheck():
    passw = input('Introduce una contraseña: ')
    m=password.search(passw)

    if (not m):
        print('Weak password')
        return False

    else:        
        print('Strong password') 
        return True

PasswordCheck()