"""
Navigation bar component for WERBEAUTY. 
Fixed top navigation with transparent to solid scroll effect.
"""

import streamlit as st
from config.constants import NAV_ITEMS, BRAND_NAME
from utils.auth_manager import is_logged_in, get_current_user, logout_user


def render_navbar():
    """
    Render the main navigation bar with logo, links, and cart/favorites badges.
    """
    cart_count = len(st.session_state.get("cart", []))
    favorites_count = len(st.session_state.get("favorites", []))
    current_page = st.session_state.get("current_page", "home")
    logged_in = is_logged_in()
    user = get_current_user() if logged_in else None
    
    # Logo and title
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0 0.5rem 0;">
        <h1 style="font-family: 'Playfair Display', serif; font-size: 2.5rem; 
                   background: linear-gradient(135deg, #B76E79, #D8C18F); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                   margin: 0;">
            {BRAND_NAME}
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Create navigation buttons using Streamlit
    if logged_in:
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    else:
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state["current_page"] = "home"
            st.rerun()
    
    with col2:
        if st.button("👩 Women", key="nav_women", use_container_width=True):
            st.session_state["current_page"] = "women"
            st.rerun()
    
    with col3:
        if st.button("👨 Men", key="nav_men", use_container_width=True):
            st.session_state["current_page"] = "men"
            st.rerun()
    
    with col4:
        if st.button("🔮 For You", key="nav_recommended", use_container_width=True):
            st.session_state["current_page"] = "recommended"
            st.rerun()
    
    with col5:
        fav_label = f"❤️ ({favorites_count})" if favorites_count > 0 else "❤️ Favorites"
        if st.button(fav_label, key="nav_favorites", use_container_width=True):
            st.session_state["current_page"] = "favorites"
            st.rerun()
    
    with col6:
        cart_label = f"🛒 ({cart_count})" if cart_count > 0 else "🛒 Cart"
        if st.button(cart_label, key="nav_cart", use_container_width=True):
            st.session_state["current_page"] = "cart"
            st.rerun()
    
    with col7:
        if logged_in:
            # Show profile button with user name
            user_name = user.get("name", "User").split()[0] if user else "Profile"
            if st.button(f"👤 {user_name}", key="nav_profile", use_container_width=True):
                st.session_state["current_page"] = "profile"
                st.rerun()
        else:
            # Show login button
            if st.button("🔐 Login", key="nav_login", use_container_width=True):
                st.session_state["current_page"] = "login"
                st.rerun()
    
    st.markdown("---")