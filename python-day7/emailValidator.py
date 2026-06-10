email=input("Enter your email: ")

def validateEmail(email):
    if (email==" " or email.count("@")!=1):
        return False
    em=email.split("@")
    username=em[0]
    domain=em[1]
    if username.startswith(".") or username.endswith(".") or (".." in username):
        return False
    
    for everyCh in username:
        allowedChars="._-!#$%&'*+/=?^{|}~`"
        if not(everyCh.isalnum() or everyCh in allowedChars):
                return False
    if len(username)>64 or len(domain)>255:
        return False
    if domain.startswith(".") or username.endswith(".") or ("." not in domain) or (".." in domain):
        return False
    if domain.startswith("-") or domain.endswith("-"):
        return False
    domainParts=domain.split(".")
    tld=domainParts[-1]
    if len(tld)<2:
        return False
    for eachCh in tld:
        if not(eachCh.isalpha()):
            return False
    for otherParts in domainParts[:-1]:
        if not(otherParts):
            return False
        for eachChar in otherParts:
            if not (eachChar.isalnum() or eachChar=="-"):
                return False
    return True

if(validateEmail(email)):
    print(f"The E-Mail address {email} is valid")
else:
    print(f"The E-Mail address {email} is invalid")

