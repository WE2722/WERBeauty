"""
Authentication manager for WERBEAUTY.
Handles user login, signup, and session management.
"""

import streamlit as st
import json
import hashlib
import os
from datetime import datetime
from typing import Optional, Dict


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
        }
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
    
    return True, "Login successful!", users[email]


def logout_user() -> None:
    """
    Log out the current user.
    """
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
