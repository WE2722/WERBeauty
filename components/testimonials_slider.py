"""
Testimonials slider component for WERBEAUTY.
Customer reviews with rating display.
"""

import streamlit as st
from config.constants import TESTIMONIALS


def render_testimonials_slider():
    """
    Render a slider/grid of customer testimonials.
    """
    st.markdown("""
    <div class="section-header animate-fadeInUp">
        <h2 class="section-title">What Our Customers Say</h2>
        <p class="section-subtitle">Real experiences from our valued customers</p>
        <div class="section-divider"></div>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    for idx, testimonial in enumerate(TESTIMONIALS[:3]):
        with cols[idx]:
            stars = "★" * testimonial["rating"]
            
            testimonial_html = f"""
            <div class="testimonial-card animate-fadeInUp" style="animation-delay: {idx * 0.15}s;">
                <img src="{testimonial['avatar']}" alt="{testimonial['name']}" class="testimonial-avatar"
                     onerror="this.src='https://via. placeholder.com/80x80?text=User'">
                <p class="testimonial-text">"{testimonial['text']}"</p>
                <p class="testimonial-author">{testimonial['name']}</p>
                <div class="testimonial-rating">{stars}</div>
            </div>
            """
            st.markdown(testimonial_html, unsafe_allow_html=True)