#!/usr/bin/env python3




def password_strength(pswd):

    score = 0

    if len(pswd) >= 8:
        has_number = any(s.isdigit() for s in pswd)
        has_schar = any(not s.isalnum() for s in pswd)
        has_letters = any(s.isalpha() for s in pswd)

        if has_letters:
            score+=1
        if has_number:
            score+=1
        if has_schar:
            score+=1

        if score == 3:
            return "Password is strong"
        elif score == 2:
            return "Password is meduim"
        else:
            return "Password is weak"
    else:
        return "Password length should be 8 or more."

password = input("Enter password: ")

print(password_strength(password))