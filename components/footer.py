"""
Footer component for WERBEAUTY. 
Elegant footer with links, newsletter, and branding.
"""

import streamlit as st
from config.constants import BRAND_NAME
from utils.auth_manager import is_logged_in, get_current_user


def render_footer():
    """
    Render the application footer with links and newsletter signup.
    Uses gender-based colors for logged-in users.
    """
    # Get gender-based colors
    if is_logged_in():
        user = get_current_user()
        user_gender = user.get("gender", "Female") if user else "Female"
        if user_gender == "Male":
            gradient = "linear-gradient(135deg, #4A90E2, #7BB3E8)"  # Blue gradient
        else:
            gradient = "linear-gradient(135deg, #B76E79, #d4a5ad)"  # Rose gold gradient
    else:
        gradient = "linear-gradient(135deg, #B76E79, #d4a5ad)"  # Default rose gold
    
    footer_html = f'<div class="footer" style="background: {gradient};"><div class="footer-grid"><div class="footer-section"><h4 class="footer-section-title">About {BRAND_NAME}</h4><p style="color: rgba(255,255,255,0.7); line-height: 1.8;">Luxury cosmetics crafted for those who appreciate elegance and quality. Discover your radiant beauty with our premium collection.</p></div><div class="footer-section"><h4 class="footer-section-title">Shop</h4><a href="#" class="footer-link">Women\'s Collection</a><a href="#" class="footer-link">Men\'s Collection</a><a href="#" class="footer-link">New Arrivals</a><a href="#" class="footer-link">Best Sellers</a><a href="#" class="footer-link">Gift Sets</a></div><div class="footer-section"><h4 class="footer-section-title">Customer Care</h4><a href="#" class="footer-link">Contact Us</a><a href="#" class="footer-link">FAQs</a><a href="#" class="footer-link">Shipping Info</a><a href="#" class="footer-link">Returns &amp; Exchanges</a><a href="#" class="footer-link">Track Order</a></div><div class="footer-section"><h4 class="footer-section-title">Connect With Us</h4><a href="https://www.instagram.com/" target="_blank" rel="noopener" class="footer-link">📸 Instagram</a><a href="https://www.facebook.com/" target="_blank" rel="noopener" class="footer-link">📘 Facebook</a><a href="https://twitter.com/" target="_blank" rel="noopener" class="footer-link">🐦 Twitter</a><a href="https://www.youtube.com/" target="_blank" rel="noopener" class="footer-link">📺 YouTube</a><a href="https://www.linkedin.com/" target="_blank" rel="noopener" class="footer-link">💼 LinkedIn</a></div></div><div class="footer-bottom"><div class="footer-logo">{BRAND_NAME}</div><p style="color: rgba(255,255,255,0.5); margin-top: 1rem;">© 2025 {BRAND_NAME}<div><bold>"MADE BY: Wiame el hafid Et houssam Rjili".</bold></div> All rights reserved. | Privacy Policy | Terms of Service</p></div></div>'
    
    st.markdown(footer_html, unsafe_allow_html=True)