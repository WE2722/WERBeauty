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
