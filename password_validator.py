#password strength validator
user_choice=input("insert password or type done to quit:\n")
if user_choice.lower().strip()=="done":
    quit()
import re
import string
def length_funct():
    if len(user_choice)<12 and len(user_choice)>8:
        return"normal length\u26A0\ufe0f"
    elif len(user_choice)>=12:
        return"strong length\u2705"
    else:
        return"weak length\u274c"
def special_characters():
    if any(special in string.punctuation for special in user_choice):
        return"contains special characters\u2705"
    else:
        return"does not contain special characters\u274c"
def upper_letters():
    has_upper=re.search(r"[A-Z]",user_choice) is not None
    has_lower=re.search(r"[a-z]",user_choice) is not None
    if has_upper and has_lower:
        return "includes upper and lower letters\u2705"
    elif has_upper:
        return "includes only upper letters\u274c"
    elif has_lower:
        return "includes only lower letters\u274c"
    else:
        return "no letters included\u274c"
def numbers_pass():
    has_numbers=re.search(r"[0-9]",user_choice) is not None
    if has_numbers:
        return"includes numeric characters\u2705"
    else:
        return"numeric characters not included\u274c"
def load_common_passwords():
    fhand=open("rockyou.txt","r")
    found=False
    for line in fhand:
        striping=line.rstrip().lower()
        if user_choice.rstrip().lower()==striping:
            found=True
            break
    if found:
        return "very common password\u274c"
    else:    
        return"not so common password\u2705"      
print(length_funct())
print(special_characters())
print(upper_letters())
print(numbers_pass())
print(load_common_passwords())
while True:
    user_choice=input("insert password or type done to quit:\n")
    if user_choice.strip().lower()=="done":
        quit()
    print(length_funct())
    print(special_characters())
    print(upper_letters())
    print(numbers_pass())
    print(load_common_passwords())