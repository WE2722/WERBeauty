"""
Favorites/Wishlist page for WERBEAUTY.
Display and manage saved favorite products.
"""

import streamlit as st
from components.animated_header import render_animated_header
from components.product_card import render_product_grid
from utils.favorites_manager import get_favorites, clear_favorites
from utils.product_loader import get_product_by_id


def render():
    """
    Render the favorites page.
    """
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        primary_color = "#0A1A3F"
        subtitle = "Your saved grooming essentials"
    else:
        primary_color = "#B76E79"
        subtitle = "Your saved beauty treasures"
    
    # Page header
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            color: #0F0F0F;
            margin-bottom: 0.5rem;
        ">❤️ Your Favorites</h1>
        <p style="color: #666; font-family: 'Inter', sans-serif;">
            {subtitle}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    favorites = get_favorites()
    
    if not favorites:
        render_empty_favorites()
        return
    
    # Load full product details for favorites
    products = []
    for product_id in favorites:
        product = get_product_by_id(product_id)
        if product:
            products.append(product)
    
    # Favorites header with clear button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"""
        <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 1.5rem;">
            {len(products)} Saved Items
        </h3>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("🗑️ Clear All", key="clear_favorites_btn"):
            clear_favorites()
            st.rerun()
    
    # Product grid
    if products:
        render_product_grid(products, columns=3, key_prefix="favorites")


def render_empty_favorites():
    """
    Render empty favorites state.
    """
    st.markdown("""
    <div class="empty-state animate-fadeInUp" style="padding: 4rem 2rem;">
        <div class="empty-state-icon">💝</div>
        <h3 class="empty-state-title">No Favorites Yet</h3>
        <p class="empty-state-message">
            Start adding products to your wishlist by clicking the heart icon. <br>
            Save your favorite items and shop them later!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🛍️ Explore Products", key="empty_favorites_shop", use_container_width=True):
            gender = st.session_state.get("gender", "women")
            st.session_state["current_page"] = gender
            st.rerun()
