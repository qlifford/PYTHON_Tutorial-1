def validate_password(pwd):
    if len(pwd) < 8 and len(pwd) <= 15:
        return "Password must be between 8 and 15 characters"
    lower   = False        
    upper   = False
    digit   = False
    special = False 

    for chr in pwd:
        if chr.islower():
            lower = True
        elif chr.isupper():
            upper = True
        elif chr.isdigit():
            digit = True
        elif (not chr.isalnum()):
            special = True
    if not upper:
        return "Password must contain at least one uppercase letter"
    if not lower:
        return "Password must contain at least one lowercase letter"
    if not digit:
        return "Password must contain at least one number"
    if not special:
        return "Password must contain at least one special character(@, ?, %, $, #, *, !, &)"        
    return "✅ Password is valid !"
