"""
Helper utilities for WERBEAUTY. 
Common functions used across the application. 
"""

import re
import random
import string
from datetime import datetime
from typing import Optional


def format_price(price: float, currency: str = "$") -> str:
    """
    Format a price with currency symbol. 
    
    Args:
        price: Price value
        currency: Currency symbol (default: $)
    
    Returns:
        Formatted price string
    """
    return f"{currency}{price:.2f}"


def generate_order_id() -> str:
    """
    Generate a unique order ID.
    
    Returns:
        Order ID string
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"WER-{timestamp}-{random_suffix}"


def validate_email(email: str) -> bool:
    """
    Validate an email address format.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid email format
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_card_number(card_number: str) -> bool:
    """
    Validate a credit card number using Luhn algorithm. 
    
    Args:
        card_number: Credit card number (can include spaces)
    
    Returns:
        True if valid card number
    """
    # Remove spaces and dashes
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if all digits
    if not card_number.isdigit():
        return False
    
    # Check length (13-19 digits for major cards)
    if len(card_number) < 13 or len(card_number) > 19:
        return False
    
    # Luhn algorithm
    digits = [int(d) for d in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(divmod(d * 2, 10))
    
    return checksum % 10 == 0


def validate_expiry_date(month: int, year: int) -> bool:
    """
    Validate credit card expiry date. 
    
    Args:
        month: Expiry month (1-12)
        year: Expiry year (2-digit or 4-digit)
    
    Returns:
        True if expiry date is valid and in the future
    """
    if month < 1 or month > 12:
        return False
    
    # Handle 2-digit year
    if year < 100:
        year += 2000
    
    now = datetime.now()
    expiry = datetime(year, month, 1)
    
    return expiry >= datetime(now.year, now.month, 1)


def validate_cvv(cvv: str) -> bool:
    """
    Validate CVV code.
    
    Args:
        cvv: CVV code (3 or 4 digits)
    
    Returns:
        True if valid CVV
    """
    return cvv.isdigit() and len(cvv) in [3, 4]


def mask_card_number(card_number: str) -> str:
    """
    Mask a credit card number for display.
    
    Args:
        card_number: Full card number
    
    Returns:
        Masked card number (e.g., **** **** **** 1234)
    """
    card_number = card_number.replace(" ", "").replace("-", "")
    if len(card_number) < 4:
        return "*" * len(card_number)
    
    masked = "*" * (len(card_number) - 4) + card_number[-4:]
    
    # Format with spaces
    return " ".join([masked[i:i+4] for i in range(0, len(masked), 4)])


def calculate_delivery_date(shipping_method: str) -> str:
    """
    Calculate estimated delivery date based on shipping method. 
    
    Args:
        shipping_method: Shipping method key
    
    Returns:
        Formatted delivery date range string
    """
    from config.constants import SHIPPING_OPTIONS
    
    shipping = SHIPPING_OPTIONS.get(shipping_method, SHIPPING_OPTIONS["standard"])
    days_text = shipping.get("days", "5-7 business days")
    
    return days_text


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length. 
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add when truncated
    
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)]. rsplit(' ', 1)[0] + suffix


def highlight_text(text: str, query: str) -> str:
    """
    Highlight matching text with HTML span. 
    
    Args:
        text: Original text
        query: Query to highlight
    
    Returns:
        Text with highlighted matches
    """
    if not query:
        return text
    
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(f'<span class="search-highlight">{query}</span>', text)