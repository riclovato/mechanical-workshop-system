from typing import Optional
import re
import email_validator
import phonenumbers
from phonenumbers import PhoneNumberFormat, NumberParseException

def validate_email(email: str) -> bool:
    """
    Validate email address using email validator library

    Args:
        email(str) : Email address to validate

    Returns: 
        bool: True if email is valid, False otherwise
    """

    try:
        email_validator.validate_email(email)
        return True
    except email_validator.EmailNotValidError:
        return False


def validate_cpf(cpf: str) -> bool:
    """
    Validate Brazilian CPF (Cadastro de Pessoas Físicas)
    
    Args:
        cpf (str): CPF number to validate
    
    Returns:
        bool: True if CPF is valid, False otherwise
    """
    # Remove non-digit characters
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # CPF must be 11 digits
    if len(cpf) != 11:
        return False
    
    # Check for repeated digits
    if len(set(cpf)) == 1:
        return False
    
    # Calculate verification digits
    def calculate_digit(cpf_slice):
        total = sum(int(digit) * weight for digit, weight in zip(cpf_slice, range(len(cpf_slice) + 1, 1, -1)))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder
    
    first_check_digit = calculate_digit(cpf[:9])
    second_check_digit = calculate_digit(cpf[:9] + str(first_check_digit))
    
    return cpf.endswith(f"{first_check_digit}{second_check_digit}")


def validate_phone(phone: str, country_code: str = 'BR') -> Optional[str]:
    cleaned_phone = phone.strip()
   
    try:
        parsed = phonenumbers.parse(cleaned_phone, country_code)
        if phonenumbers.is_valid_number(parsed):
            return phonenumbers.format_number(parsed, PhoneNumberFormat.E164)
    except NumberParseException:
        pass
    
    # Regex patterns for specific cases
    patterns = [
        r"^\+55\s?\(?(0?\d{2})\)?\s?\d{4,5}[-\s]?\d{4}$",  # Allow +55 (0XX) ... (takes zero in local context)
        r"^0?(\d{2})[-\s]?\d{4,5}[-\s]?\d{4}$",            # Local format with or without zero (ex: 06197682752)
        r"^0500[\s-]?\d{3}[\s-]?\d{4}$",                   # 0500 numbers (ex: 0500 642 6473)
        r"^\+\d{1,3}\s?\d{1,4}\s?\d{4,10}$"               # Geral International Format
    ]
    
    for pattern in patterns:
        if re.match(pattern, cleaned_phone, re.IGNORECASE):
            digits = re.sub(r"\D", "", cleaned_phone)  # Remove non-digits
            
            # Case 1: International Numbers (ex: +55 61 9768 2752)
            if cleaned_phone.startswith("+"):
                return f"+{digits.lstrip('+')}"
            
            # Case 2: Local Numbers with 0 (ex: (061) 9768-2752 → +556197682752)
            if digits.startswith("0") and len(digits) in (10, 11):
                return f"+55{digits[1:]}"
            
            # Case 3: 0500 Numbers (ex: 0500 642 6473 → +5505006426473)
            if digits.startswith("0500"):
                return f"+55{digits}"
            
            # Default: Add Brazil code
            return f"+55{digits}"
    
    return None


def validate_license_plate(plate: str) -> bool:
    """
    Validate Brazilian license plate format
    
    Args:
        plate (str): License plate to validate
    
    Returns:
        bool: True if license plate is valid, False otherwise
    """
    # Brazilian license plate format: AAA-1234 or AAA1234
    pattern = r'^[A-Z]{3}-?\d{4}$'
    return bool(re.match(pattern, plate))