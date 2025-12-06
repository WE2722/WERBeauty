"""
Home page for WERBEAUTY. 
Main landing page with hero, categories, bestsellers, and more.
"""

import streamlit as st
from components.animated_header import render_animated_header, render_section_header
from components.category_carousel import render_category_carousel
from components.testimonials_slider import render_testimonials_slider
from components.comments_section import render_comments_section
from components.product_card import render_product_grid
from utils.product_loader import load_women_products, load_men_products
from utils.recommendation_engine import get_trending, get_recommendations
from config.constants import BRAND_NAME, BRAND_TAGLINE


def render():
    """
    Render the home page with all sections.
    """
    gender = st.session_state.get("gender", "women")
    
    # Hero Section
    render_hero_section(gender)
    
    # Gender Quick Access
    render_gender_quick_access()
    
    # Featured Categories
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    render_section_header(
        "Shop by Category",
        "Explore our curated collections"
    )
    render_category_carousel(gender)
    
    # Best Sellers
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_bestsellers_section(gender)
    
    # New Arrivals
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_new_arrivals_section(gender)
    
    # AI Recommendations Preview
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_recommendations_preview()
    
    # Testimonials
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_testimonials_slider()
    
    # Customer Reviews
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_comments_section()
    
    # Newsletter
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_newsletter_section()


def render_hero_section(gender: str):
    """
    Render the hero banner section with parallax effect.
    """
    if gender == "men":
        gradient_start = "#0A1A3F"
        gradient_end = "#1a2a4f"
        hero_image = "https://images.unsplash. com/photo-1621607512214-68297480165e?w=1200&h=800&fit=crop"
        tagline = "Refined Grooming for the Modern Gentleman"
    else:
        gradient_start = "#B76E79"
        gradient_end = "#d4a5ad"
        hero_image = "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=1200&h=800&fit=crop"
        tagline = "Discover Your Radiant Beauty"
    
    hero_html = f"""
    <div class="hero-section" style="
        background: linear-gradient(135deg, {gradient_start}dd, {gradient_end}dd),
                    url('{hero_image}') center/cover;
        min-height: 80vh;
    ">
        <div class="hero-particles">
            <div class="particle" style="left: 10%; animation-delay: 0s; width: 8px; height: 8px;"></div>
            <div class="particle" style="left: 20%; animation-delay: 2s; width: 12px; height: 12px;"></div>
            <div class="particle" style="left: 35%; animation-delay: 4s; width: 6px; height: 6px;"></div>
            <div class="particle" style="left: 50%; animation-delay: 1s; width: 10px; height: 10px;"></div>
            <div class="particle" style="left: 65%; animation-delay: 3s; width: 8px; height: 8px;"></div>
            <div class="particle" style="left: 80%; animation-delay: 5s; width: 14px; height: 14px;"></div>
            <div class="particle" style="left: 90%; animation-delay: 2. 5s; width: 6px; height: 6px;"></div>
        </div>
        <div class="hero-content">
            <h1 class="hero-title animate-fadeInUp" style="
                font-size: 4. 5rem;
                text-shadow: 2px 4px 30px rgba(0,0,0,0.3);
            ">{BRAND_NAME}</h1>
            <p class="hero-subtitle animate-fadeInUp delay-2" style="
                font-size: 1.4rem;
                max-width: 600px;
                margin: 0 auto 2rem;
            ">{tagline}</p>
            <div class="animate-fadeInUp delay-3">
                <span style="
                    display: inline-block;
                    padding: 1rem 3rem;
                    background: linear-gradient(135deg, #D4AF37, #f5d76e);
                    color: #0F0F0F;
                    border-radius: 50px;
                    font-family: 'Inter', sans-serif;
                    font-weight: 600;
                    font-size: 1.1rem;
                    box-shadow: 0 10px 40px rgba(212, 175, 55, 0.4);
                    cursor: pointer;
                    transition: all 0.3s ease;
                ">Shop Now ✨</span>
            </div>
        </div>
    </div>
    """
    
    st.markdown(hero_html, unsafe_allow_html=True)
    
    # Invisible button for navigation
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🛍️ Start Shopping", key="hero_shop_btn", use_container_width=True):
            st.session_state["current_page"] = gender
            st.rerun()


def render_gender_quick_access():
    """
    Render quick access buttons for gender sections.
    """
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #B76E79, #d4a5ad);
            border-radius: 24px;
            padding: 3rem 2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 10px 40px rgba(183, 110, 121, 0.2);
        ">
            <div style="font-size: 3rem; margin-bottom: 1rem;">👩</div>
            <h3 style="
                font-family: 'Playfair Display', serif;
                font-size: 1.8rem;
                color: white;
                margin-bottom: 0.5rem;
            ">Women's Collection</h3>
            <p style="color: rgba(255,255,255,0.9); font-size: 1rem;">
                Makeup • Skincare • Perfumes • Hair Care
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Explore Women's →", key="quick_women", use_container_width=True):
            st.session_state["current_page"] = "women"
            st.session_state["gender"] = "women"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #0A1A3F, #1a2a4f);
            border-radius: 24px;
            padding: 3rem 2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 10px 40px rgba(10, 26, 63, 0.2);
        ">
            <div style="font-size: 3rem; margin-bottom: 1rem;">👨</div>
            <h3 style="
                font-family: 'Playfair Display', serif;
                font-size: 1. 8rem;
                color: white;
                margin-bottom: 0.5rem;
            ">Men's Collection</h3>
            <p style="color: rgba(255,255,255,0. 9); font-size: 1rem;">
                Beard Care • Grooming • Perfumes • Hair Care
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Explore Men's →", key="quick_men", use_container_width=True):
            st.session_state["current_page"] = "men"
            st. session_state["gender"] = "men"
            st.rerun()


def render_bestsellers_section(gender: str):
    """
    Render the bestsellers product section.
    """
    render_section_header(
        "Best Sellers",
        "Our most loved products by customers worldwide"
    )
    
    # Load products
    if gender == "men":
        products = load_men_products()
    else:
        products = load_women_products()
    
    # Filter bestsellers (products with high popularity or "Bestseller" badge)
    bestsellers = [p for p in products if p.get("badge") == "Bestseller" or p.get("popularity", 0) >= 90]
    
    # If not enough bestsellers, get top by popularity
    if len(bestsellers) < 4:
        bestsellers = sorted(products, key=lambda x: x.get("popularity", 0), reverse=True)[:8]
    
    render_product_grid(bestsellers[:8], columns=4, key_prefix="bestsellers")


def render_new_arrivals_section(gender: str):
    """
    Render the new arrivals product section.
    """
    render_section_header(
        "New Arrivals",
        "Fresh additions to our luxury collection"
    )
    
    # Load products
    if gender == "men":
        products = load_men_products()
    else:
        products = load_women_products()
    
    # Filter new arrivals (products with "New" badge)
    new_arrivals = [p for p in products if p.get("badge") == "New"]
    
    # If not enough new products, get latest by ID
    if len(new_arrivals) < 4:
        new_arrivals = sorted(products, key=lambda x: x.get("id", ""), reverse=True)[:4]
    
    render_product_grid(new_arrivals[:4], columns=4, key_prefix="new_arrivals")


def render_recommendations_preview():
    """
    Render a preview of AI-powered recommendations.
    """
    recommendations = get_recommendations(limit=4)
    
    if not recommendations:
        return
    
    st.markdown("""
    <div class="section-header animate-fadeInUp">
        <h2 class="section-title">🔮 Recommended For You</h2>
        <p class="section-subtitle">Personalized picks based on your preferences</p>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    render_product_grid(recommendations, columns=4, key_prefix="home_recommendations")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("View All Recommendations →", key="view_all_recs", use_container_width=True):
            st.session_state["current_page"] = "recommended"
            st.rerun()


def render_newsletter_section():
    """
    Render the newsletter subscription section. 
    """
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        gradient_start = "#0A1A3F"
        gradient_end = "#1a2a4f"
    else:
        gradient_start = "#B76E79"
        gradient_end = "#d4a5ad"
    
    st.markdown(f"""
    <div class="newsletter-section" style="background: linear-gradient(135deg, {gradient_start}, {gradient_end});">
        <h2 class="newsletter-title">Join the WERBEAUTY Family</h2>
        <p class="newsletter-subtitle">Subscribe for exclusive offers, new arrivals, and beauty tips</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address",
            label_visibility="collapsed",
            key="newsletter_email"
        )
        
        if st.button("Subscribe ✨", key="newsletter_subscribe", use_container_width=True):
            if email and "@" in email:
                st.success("🎉 Thank you for subscribing!  Check your inbox for a special welcome offer.")
            else:
                st.error("Please enter a valid email address.")