from typing import Optional
import re
import email_validator
import phonenumbers

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
    """
    Validate phone number using phonenumbers library
    
    Args:
        phone (str): Phone number to validate
        country_code (str, optional): Country code. Defaults to 'BR' (Brazil)
    
    Returns:
        Optional[str]: Formatted phone number if valid, None otherwise
    """
    try:
        parsed_phone = phonenumbers.parse(phone, country_code)
        if phonenumbers.is_valid_number(parsed_phone):
            return phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
        return None
    except phonenumbers.phonenumberutil.NumberParseException:
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