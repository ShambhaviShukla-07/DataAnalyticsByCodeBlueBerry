username=input("Enter username: ")

def usernameFormatting(username):
    if username.startswith(" ") or username.endswith(" "):
        username=username.strip()
    for eachCh in username:
        if not (eachCh.isalnum() or eachCh=="_" or eachCh=="-"):
            return False
    if username.endswith("-") or username.endswith("_"):
        return False
    if username.startswith("-") or username.startswith("_"):
        return False
    if(len(username)<6 or len(username)>20):
        return False
    
    return True

if(usernameFormatting(username)):
    print(f"Your username {username} is acceptable")
else:
    print(f"Your username {username} is not acceptable")
    