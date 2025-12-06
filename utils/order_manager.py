"""
Order management utilities for WERBEAUTY.
Handles order creation, storage, and retrieval.
"""

import streamlit as st
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from utils.auth_manager import get_current_user_email


def load_orders() -> Dict:
    """
    Load all orders from JSON file.
    
    Returns:
        Dictionary with user emails as keys and their orders as values
    """
    orders_file = "data/orders.json"
    
    if os.path.exists(orders_file):
        with open(orders_file, 'r') as f:
            return json.load(f)
    else:
        os.makedirs("data", exist_ok=True)
        with open(orders_file, 'w') as f:
            json.dump({}, f)
        return {}


def save_orders(orders: Dict) -> None:
    """
    Save orders to JSON file.
    
    Args:
        orders: Dictionary of all orders
    """
    orders_file = "data/orders.json"
    os.makedirs("data", exist_ok=True)
    
    with open(orders_file, 'w') as f:
        json.dump(orders, f, indent=2)


def create_order(order_id: str, cart_items: List[Dict], checkout_data: Dict, total: float) -> bool:
    """
    Create a new order for the current user.
    
    Args:
        order_id: Unique order identifier
        cart_items: List of items in the order
        checkout_data: Billing and shipping information
        total: Order total amount
    
    Returns:
        True if order created successfully
    """
    email = get_current_user_email()
    
    if not email:
        # Store order in session for guest users
        if "guest_orders" not in st.session_state:
            st.session_state["guest_orders"] = []
        
        order = {
            "order_id": order_id,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": cart_items,
            "checkout_data": checkout_data,
            "total": total,
            "status": "Processing"
        }
        st.session_state["guest_orders"].append(order)
        return True
    
    # Load existing orders
    orders = load_orders()
    
    # Initialize user's order list if needed
    if email not in orders:
        orders[email] = []
    
    # Create order object
    order = {
        "order_id": order_id,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": cart_items,
        "checkout_data": checkout_data,
        "total": total,
        "status": "Processing"
    }
    
    # Add order to user's order list
    orders[email].append(order)
    
    # Save to file
    save_orders(orders)
    
    return True


def get_user_orders() -> List[Dict]:
    """
    Get all orders for the current user.
    
    Returns:
        List of orders for the current user
    """
    email = get_current_user_email()
    
    if not email:
        # Return guest orders from session
        return st.session_state.get("guest_orders", [])
    
    orders = load_orders()
    return orders.get(email, [])


def get_order_by_id(order_id: str) -> Optional[Dict]:
    """
    Get a specific order by ID for the current user.
    
    Args:
        order_id: Order ID to retrieve
    
    Returns:
        Order dictionary or None if not found
    """
    user_orders = get_user_orders()
    
    for order in user_orders:
        if order["order_id"] == order_id:
            return order
    
    return None


def cancel_order(order_id: str) -> bool:
    """
    Cancel an order.
    
    Args:
        order_id: Order ID to cancel
    
    Returns:
        True if cancelled successfully
    """
    email = get_current_user_email()
    
    if not email:
        # Guest user - update session
        guest_orders = st.session_state.get("guest_orders", [])
        for order in guest_orders:
            if order["order_id"] == order_id:
                order["status"] = "Cancelled"
                return True
        return False
    
    # Logged in user - update file
    orders = load_orders()
    
    if email in orders:
        for order in orders[email]:
            if order["order_id"] == order_id:
                order["status"] = "Cancelled"
                save_orders(orders)
                return True
    
    return False


def get_order_count() -> int:
    """
    Get total number of orders for current user.
    
    Returns:
        Number of orders
    """
    return len(get_user_orders())
