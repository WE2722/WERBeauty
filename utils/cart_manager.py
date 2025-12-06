"""
Cart Manager utility for WERBEAUTY application.
Handles cart operations using session state.
"""

import streamlit as st


def get_cart():
    """Get the current cart from session state."""
    if "cart" not in st.session_state:
        st.session_state.cart = []
    return st.session_state.cart


def add_to_cart(product, quantity=1):
    """
    Add a product to the cart.
    
    Args:
        product: Product dictionary containing product details
        quantity: Quantity to add (default: 1)
    """
    cart = get_cart()
    
    # Check if product already exists in cart
    for item in cart:
        if item["id"] == product["id"]:
            item["quantity"] += quantity
            st.session_state.cart = cart
            return
    
    # Add new product to cart
    cart_item = {
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "image": product.get("image", ""),
        "brand": product.get("brand", ""),
        "quantity": quantity
    }
    cart.append(cart_item)
    st.session_state.cart = cart


def remove_from_cart(product_id):
    """
    Remove a product from the cart.
    
    Args:
        product_id: ID of the product to remove
    """
    cart = get_cart()
    st.session_state.cart = [item for item in cart if item["id"] != product_id]


def update_quantity(product_id, quantity):
    """
    Update the quantity of a product in the cart.
    
    Args:
        product_id: ID of the product
        quantity: New quantity
    """
    cart = get_cart()
    for item in cart:
        if item["id"] == product_id:
            if quantity <= 0:
                remove_from_cart(product_id)
            else:
                item["quantity"] = quantity
            break
    st.session_state.cart = cart


def clear_cart():
    """Clear all items from the cart."""
    st.session_state.cart = []


def is_in_cart(product_id):
    """
    Check if a product is in the cart.
    
    Args:
        product_id: ID of the product to check
        
    Returns:
        bool: True if product is in cart, False otherwise
    """
    cart = get_cart()
    return any(item["id"] == product_id for item in cart)


def get_cart_total():
    """
    Calculate the total price and breakdown of items in the cart.
    
    Returns:
        dict: Dictionary with subtotal, shipping, tax, discount, total, and item_count
    """
    cart = get_cart()
    
    # Calculate subtotal
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    item_count = sum(item["quantity"] for item in cart)
    
    # Calculate shipping (free over $100)
    shipping = 0 if subtotal >= 100 else 10.00
    
    # Calculate discount (example: 10% off over $200)
    discount = subtotal * 0.1 if subtotal >= 200 else 0
    
    # Calculate tax (8%)
    tax = (subtotal - discount) * 0.08
    
    # Calculate total
    total = subtotal - discount + shipping + tax
    
    return {
        'subtotal': subtotal,
        'shipping': shipping,
        'tax': tax,
        'discount': discount,
        'total': total,
        'item_count': item_count
    }


def get_cart_count():
    """
    Get the total number of items in the cart.
    
    Returns:
        int: Total item count
    """
    cart = get_cart()
    return sum(item["quantity"] for item in cart)
