class InvalidEmailException(Exception):
    pass


def send_email(email, subject, content):
    if not "@" in email:
        raise InvalidEmailException("email does not contain '@'")
    
try:
    send_email("xyz", "t11", "t22")
except InvalidEmailException:
    print("Ungültige Email")
finally:
    print("always executed, cleaning up...")
    
    
    
