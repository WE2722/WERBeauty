"""
Authentication manager for WERBEAUTY.
Handles user login, signup, and session management.
"""

import streamlit as st
import json
import hashlib
import os
import secrets
import string
from datetime import datetime, timedelta
from typing import Optional, Dict
from utils.email_manager import send_password_reset_email


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256.
    
    Args:
        password: Plain text password
    
    Returns:
        Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def load_users() -> Dict:
    """
    Load users from JSON file.
    
    Returns:
        Dictionary of users
    """
    users_file = "data/users.json"
    
    if os.path.exists(users_file):
        with open(users_file, 'r') as f:
            return json.load(f)
    else:
        # Create empty users file
        os.makedirs("data", exist_ok=True)
        with open(users_file, 'w') as f:
            json.dump({}, f)
        return {}


def save_users(users: Dict) -> None:
    """
    Save users to JSON file.
    
    Args:
        users: Dictionary of users
    """
    users_file = "data/users.json"
    os.makedirs("data", exist_ok=True)
    
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=2)


def signup_user(email: str, password: str, name: str) -> tuple[bool, str]:
    """
    Register a new user.
    
    Args:
        email: User email
        password: User password
        name: User full name
    
    Returns:
        Tuple of (success, message)
    """
    users = load_users()
    
    # Check if email already exists
    if email in users:
        return False, "Email already registered. Please login instead."
    
    # Validate email
    if '@' not in email or '.' not in email:
        return False, "Please enter a valid email address."
    
    # Validate password
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    
    # Create user
    users[email] = {
        "name": name,
        "password": hash_password(password),
        "created_at": datetime.now().isoformat(),
        "profile": {
            "phone": "",
            "address": "",
            "city": "",
            "country": "",
            "birthday": ""
        },
        "preferences": {
            "skin_type": "",
            "favorite_brands": [],
            "newsletter": True
        },
        "cart": [],
        "favorites": []
    }
    
    save_users(users)
    return True, "Account created successfully! Please login."


def login_user(email: str, password: str) -> tuple[bool, str, Optional[Dict]]:
    """
    Authenticate a user.
    
    Args:
        email: User email
        password: User password
    
    Returns:
        Tuple of (success, message, user_data)
    """
    users = load_users()
    
    # Check if email exists
    if email not in users:
        return False, "Email not found. Please sign up first.", None
    
    # Verify password
    if users[email]["password"] != hash_password(password):
        return False, "Incorrect password. Please try again.", None
    
    # Merge session cart and favorites with user's stored data
    session_cart = st.session_state.get("cart", [])
    session_favorites = st.session_state.get("favorites", [])
    
    # Initialize if missing
    if "cart" not in users[email]:
        users[email]["cart"] = []
    if "favorites" not in users[email]:
        users[email]["favorites"] = []
    
    # Merge session items with user's stored items
    # For cart: merge items, avoiding duplicates
    for session_item in session_cart:
        found = False
        for user_item in users[email]["cart"]:
            if user_item["id"] == session_item["id"]:
                user_item["quantity"] += session_item["quantity"]
                found = True
                break
        if not found:
            users[email]["cart"].append(session_item)
    
    # For favorites: merge IDs, avoiding duplicates
    for fav_id in session_favorites:
        if fav_id not in users[email]["favorites"]:
            users[email]["favorites"].append(fav_id)
    
    # Save merged data
    save_users(users)
    
    # Load user's cart and favorites into session
    st.session_state["cart"] = users[email]["cart"]
    st.session_state["favorites"] = users[email]["favorites"]
    
    return True, "Login successful!", users[email]


def logout_user() -> None:
    """
    Log out the current user.
    """
    # Save cart and favorites to user account before logout
    email = get_current_user_email()
    if email:
        users = load_users()
        if email in users:
            users[email]["cart"] = st.session_state.get("cart", [])
            users[email]["favorites"] = st.session_state.get("favorites", [])
            save_users(users)
    
    if "user" in st.session_state:
        del st.session_state["user"]
    if "user_email" in st.session_state:
        del st.session_state["user_email"]


def is_logged_in() -> bool:
    """
    Check if a user is logged in.
    
    Returns:
        True if user is logged in
    """
    return "user" in st.session_state and st.session_state["user"] is not None


def get_current_user() -> Optional[Dict]:
    """
    Get current logged in user data.
    
    Returns:
        User data dictionary or None
    """
    return st.session_state.get("user", None)


def get_current_user_email() -> Optional[str]:
    """
    Get current logged in user email.
    
    Returns:
        User email or None
    """
    return st.session_state.get("user_email", None)


def update_user_profile(email: str, profile_data: Dict) -> tuple[bool, str]:
    """
    Update user profile information.
    
    Args:
        email: User email
        profile_data: Dictionary with profile fields to update
    
    Returns:
        Tuple of (success, message)
    """
    users = load_users()
    
    if email not in users:
        return False, "User not found."
    
    # Update profile fields
    for key, value in profile_data.items():
        if key in ["name", "phone", "address", "city", "country", "birthday"]:
            if key == "name":
                users[email]["name"] = value
            else:
                users[email]["profile"][key] = value
    
    save_users(users)
    
    # Update session state
    if "user" in st.session_state:
        st.session_state["user"] = users[email]
    
    return True, "Profile updated successfully!"


def update_user_preferences(email: str, preferences: Dict) -> tuple[bool, str]:
    """
    Update user preferences.
    
    Args:
        email: User email
        preferences: Dictionary with preference fields to update
    
    Returns:
        Tuple of (success, message)
    """
    users = load_users()
    
    if email not in users:
        return False, "User not found."
    
    # Update preferences
    for key, value in preferences.items():
        users[email]["preferences"][key] = value
    
    save_users(users)
    
    # Update session state
    if "user" in st.session_state:
        st.session_state["user"] = users[email]
    
    return True, "Preferences updated successfully!"


def change_password(email: str, old_password: str, new_password: str) -> tuple[bool, str]:
    """
    Change user password.
    
    Args:
        email: User email
        old_password: Current password
        new_password: New password
    
    Returns:
        Tuple of (success, message)
    """
    users = load_users()
    
    if email not in users:
        return False, "User not found."
    
    # Verify old password
    if users[email]["password"] != hash_password(old_password):
        return False, "Current password is incorrect."
    
    # Validate new password
    if len(new_password) < 6:
        return False, "New password must be at least 6 characters long."
    
    # Update password
    users[email]["password"] = hash_password(new_password)
    save_users(users)
    
    return True, "Password changed successfully!"


def sync_cart_to_user() -> None:
    """
    Sync current session cart to user account.
    Call this after cart operations when user is logged in.
    """
    email = get_current_user_email()
    if email:
        users = load_users()
        if email in users:
            users[email]["cart"] = st.session_state.get("cart", [])
            save_users(users)


def sync_favorites_to_user() -> None:
    """
    Sync current session favorites to user account.
    Call this after favorites operations when user is logged in.
    """
    email = get_current_user_email()
    if email:
        users = load_users()
        if email in users:
            users[email]["favorites"] = st.session_state.get("favorites", [])
            save_users(users)


def load_user_data_to_session() -> None:
    """
    Load user's cart and favorites from account into session.
    Call this after login.
    """
    email = get_current_user_email()
    if email:
        users = load_users()
        if email in users:
            # Initialize if missing
            if "cart" not in users[email]:
                users[email]["cart"] = []
            if "favorites" not in users[email]:
                users[email]["favorites"] = []
            
            st.session_state["cart"] = users[email]["cart"]
            st.session_state["favorites"] = users[email]["favorites"]


def generate_reset_token(length: int = 12) -> str:
    """
    Generate a secure random token for password reset.
    
    Args:
        length: Length of the token
    
    Returns:
        Random token string
    """
    # Use letters and digits for easy copying
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


def initiate_password_reset(email: str) -> tuple[bool, str]:
    """
    Initiate password reset process for a user.
    Generates a temporary password and sends it via email.
    
    Args:
        email: User email
    
    Returns:
        Tuple of (success, message)
    """
    users = load_users()
    
    # Check if email exists
    if email not in users:
        # Don't reveal if email exists or not for security
        return True, f"If an account exists with {email}, a password reset email has been sent."
    
    # Generate temporary password
    temp_password = generate_reset_token(12)
    
    # Store temporary password and expiration (1 hour from now)
    users[email]["temp_password"] = hash_password(temp_password)
    users[email]["temp_password_expires"] = (datetime.now() + timedelta(hours=1)).isoformat()
    
    save_users(users)
    
    # Send email with temporary password
    user_name = users[email].get("name", "User")
    success, message = send_password_reset_email(email, temp_password, user_name)
    
    if success:
        return True, f"Password reset instructions have been sent to {email}. Check your email for the temporary password."
    else:
        return False, message


def login_with_temp_password(email: str, temp_password: str) -> tuple[bool, str, Optional[Dict]]:
    """
    Authenticate user with temporary password.
    
    Args:
        email: User email
        temp_password: Temporary password from reset email
    
    Returns:
        Tuple of (success, message, user_data)
    """
    users = load_users()
    
    # Check if email exists
    if email not in users:
        return False, "Email not found.", None
    
    # Check if temporary password exists
    if "temp_password" not in users[email]:
        return False, "No active password reset request. Please use your regular password or request a new reset.", None
    
    # Check if temporary password has expired
    if "temp_password_expires" in users[email]:
        expiry = datetime.fromisoformat(users[email]["temp_password_expires"])
        if datetime.now() > expiry:
            # Clean up expired temp password
            del users[email]["temp_password"]
            del users[email]["temp_password_expires"]
            save_users(users)
            return False, "Temporary password has expired. Please request a new password reset.", None
    
    # Verify temporary password
    if users[email]["temp_password"] != hash_password(temp_password):
        return False, "Incorrect temporary password.", None
    
    # Clean up temporary password after successful login
    del users[email]["temp_password"]
    if "temp_password_expires" in users[email]:
        del users[email]["temp_password_expires"]
    save_users(users)
    
    # Merge session cart and favorites (same as regular login)
    session_cart = st.session_state.get("cart", [])
    session_favorites = st.session_state.get("favorites", [])
    
    if "cart" not in users[email]:
        users[email]["cart"] = []
    if "favorites" not in users[email]:
        users[email]["favorites"] = []
    
    for session_item in session_cart:
        found = False
        for user_item in users[email]["cart"]:
            if user_item["id"] == session_item["id"]:
                user_item["quantity"] += session_item["quantity"]
                found = True
                break
        if not found:
            users[email]["cart"].append(session_item)
    
    for fav_id in session_favorites:
        if fav_id not in users[email]["favorites"]:
            users[email]["favorites"].append(fav_id)
    
    save_users(users)
    
    st.session_state["cart"] = users[email]["cart"]
    st.session_state["favorites"] = users[email]["favorites"]
    
    return True, "Login successful! Please change your password immediately in your profile settings.", users[email]


def verify_temp_password_and_login(email: str, password: str) -> tuple[bool, str, Optional[Dict]]:
    """
    Attempt login with either regular password or temporary password.
    This is a wrapper that tries both methods.
    
    Args:
        email: User email
        password: Password (could be regular or temporary)
    
    Returns:
        Tuple of (success, message, user_data)
    """
    users = load_users()
    
    if email not in users:
        return False, "Email not found. Please sign up first.", None
    
    # First try regular password
    if users[email]["password"] == hash_password(password):
        # Regular login flow
        return login_user(email, password)
    
    # If regular password fails, try temporary password
    if "temp_password" in users[email]:
        return login_with_temp_password(email, password)
    
    return False, "Incorrect password. Please try again or use 'Forgot Password'.", None

