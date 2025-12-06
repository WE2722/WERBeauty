"""
Favorites management utilities for WERBEAUTY.
Handles wishlist operations. 
"""

import streamlit as st
from typing import Dict, List


def get_favorites() -> List[str]:
    """
    Get the current favorites from session state. 
    
    Returns:
        List of favorite product IDs
    """
    if "favorites" not in st.session_state:
        st.session_state["favorites"] = []
    return st.session_state["favorites"]


def add_to_favorites(product: Dict) -> bool:
    """
    Add a product to favorites.
    
    Args:
        product: Product dictionary to add
    
    Returns:
        True if added successfully
    """
    favorites = get_favorites()
    product_id = product.get("id")
    
    # Check if already in favorites
    if is_favorite(product_id):
        return False
    
    # Add product ID to favorites
    favorites.append(product_id)
    st.session_state["favorites"] = favorites
    return True
    
    return True


def remove_from_favorites(product_id: str) -> bool:
    """
    Remove a product from favorites. 
    
    Args:
        product_id: ID of product to remove
    
    Returns:
        True if removed successfully
    """
    favorites = get_favorites()
    st.session_state["favorites"] = [item for item in favorites if item.get("id") != product_id]
    return True


def is_favorite(product_id: str) -> bool:
    """
    Check if a product is in favorites.
    
    Args:
        product_id: ID of product to check
    
    Returns:
        True if product is in favorites
    """
    favorites = get_favorites()
    return product_id in favorites


def clear_favorites() -> bool:
    """
    Clear all favorites.
    
    Returns:
        True if cleared successfully
    """
    st.session_state["favorites"] = []
    return True


def move_to_cart(product_id: str) -> bool:
    """
    Move a favorite item to the cart. 
    
    Args:
        product_id: ID of product to move
    
    Returns:
        True if moved successfully
    """
    from utils.cart_manager import add_to_cart
    
    favorites = get_favorites()
    product = None
    
    for item in favorites:
        if item.get("id") == product_id:
            product = item
            break
    
    if product:
        add_to_cart(product)
        remove_from_favorites(product_id)
        return True
    
    return False