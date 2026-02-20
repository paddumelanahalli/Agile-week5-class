import re

def validate_password(password):
    # Defensive programming: ensure input is correct type
    assert isinstance(password, str), "Input must be a string"
    
    if len(password) < 8: return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*()]", password))
    
    return all([has_upper, has_lower, has_digit, has_special])
