"""
Recommendations page for WERBEAUTY.
AI-powered personalized product suggestions.
"""

import streamlit as st
from components.animated_header import render_section_header
from components.product_card import render_product_grid
from utils.recommendation_engine import get_recommendations, get_trending, get_similar_products, get_also_bought
from utils.product_loader import load_women_products, load_men_products


def render():
    """
    Render the recommendations page.
    """
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        primary_color = "#0A1A3F"
        gradient = "linear-gradient(135deg, #0A1A3F, #1a2a4f)"
    else:
        primary_color = "#B76E79"
        gradient = "linear-gradient(135deg, #B76E79, #d4a5ad)"
    
    # Page header
    st.markdown(f"""
    <div style="
        background: {gradient};
        padding: 4rem 2rem;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 3rem;
    ">
        <h1 style="
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            color: white;
            margin-bottom: 1rem;
        ">🔮 Recommended For You</h1>
        <p style="
            color: rgba(255,255,255,0.9);
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto;
        ">
            Personalized suggestions based on your preferences and browsing history
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Personalized Recommendations
    render_personalized_section()
    
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    
    # Trending Now
    render_trending_section()
    
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    
    # Based on Your Favorites
    render_favorites_based_section()
    
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    
    # Complete Your Routine
    render_routine_section()


def render_personalized_section():
    """
    Render personalized recommendations section. 
    """
    render_section_header(
        "✨ Curated Just For You",
        "Products we think you'll love based on your taste"
    )
    
    recommendations = get_recommendations(limit=8)
    
    if recommendations:
        render_product_grid(recommendations, columns=4, key_prefix="recommended")
    else:
        st.markdown("""
        <div style="
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 18px;
            text-align: center;
        ">
            <p style="color: #666; margin: 0;">
                🔍 Browse some products to get personalized recommendations! 
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        gender = st.session_state.get("gender", "women")
        if st.button("🛍️ Start Browsing", key="rec_browse", use_container_width=False):
            st. session_state["current_page"] = gender
            st.rerun()


def render_trending_section():
    """
    Render trending products section.
    """
    render_section_header(
        "🔥 Trending Now",
        "Most popular products loved by our community"
    )
    
    trending = get_trending(limit=4)
    
    if trending:
        render_product_grid(trending, columns=4, key_prefix="trending")


def render_favorites_based_section():
    """
    Render recommendations based on favorites. 
    """
    favorites = st.session_state.get("favorites", [])
    
    if not favorites:
        return
    
    render_section_header(
        "❤️ Because You Saved",
        "Similar products to your favorites"
    )
    
    # Get similar products based on first favorite (favorites are product IDs)
    first_fav_id = favorites[0] if isinstance(favorites[0], str) else favorites[0].get("id", "")
    similar = get_similar_products(first_fav_id, limit=4)
    
    if similar:
        render_product_grid(similar, columns=4, key_prefix="similar")


def render_routine_section():
    """
    Render complete your routine section.
    """
    cart = st.session_state.get("cart", [])
    
    if not cart:
        return
    
    render_section_header(
        "💫 Complete Your Routine",
        "Products that pair perfectly with your cart items"
    )
    
    # Get complementary products based on first cart item
    first_cart = cart[0]
    complementary = get_also_bought(first_cart.get("id", ""), limit=4)
    
    if complementary:
        render_product_grid(complementary, columns=4, key_prefix="complementary")