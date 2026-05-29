"""
validators.py - input validation utitlity - reusable
Usage - 
    from validators import validate_email, validate_phone, sanitize_html
"""
import re
from typing import Optional

# Module - level constants
EMAIL_PATTERN = re.compile(r'^[\w.+-]+@[\w]+\.[\w.]+$')
PHONE_PATTERN = re.compile(r'^\+?[\d\s\-().]{7,15}$')
HTML_TAG_PATTERN = re.compile(r'<[^>]+>')

_BLOCKED_DOMAINS = {'tempmail.com', 'junkmail.com', 'throwawaymail.com'}

# ------ APIs ---------------
def validate_email(email: str) -> tuple[bool, Optional[str]]:
    """
        Returns (True, None) -> if valid email
        ex: validate_email(alice@example.com) => (True, None)

        Returns (False, Reason) -> if invalid
        ex: validate_email(alice@tempmail.com) => (False, 'This email domain is not allowed')
    """

    email = email.strip().lower()

    if not EMAIL_PATTERN.match(email):
        return False, 'Invalid email'
    
    domain = email.split('@')[1]

    if domain in _BLOCKED_DOMAINS:
        return False, 'This email domain is not allowed'
    
    return True, None
