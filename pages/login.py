"""
Login page for WERBEAUTY.
User authentication and login form.
"""

import streamlit as st
from config.theme import apply_theme
from utils.auth_manager import login_user, is_logged_in
from components.navbar import render_navbar


def render():
    """
    Render the login page.
    """
    apply_theme()
    render_navbar()
    
    # Redirect if already logged in
    if is_logged_in():
        st.session_state["current_page"] = "home"
        st.rerun()
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Login header
        st.markdown('<div style="text-align: center;"><h1 style="font-family: \'Playfair Display\', serif; font-size: 2.5rem; color: #B76E79; margin-bottom: 0.5rem;">Welcome Back</h1><p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 2rem;">Login to access your account</p></div>', unsafe_allow_html=True)
        
        # Login form container
        st.markdown('<div class="glass-card" style="padding: 2rem; border-radius: 24px; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);">', unsafe_allow_html=True)
        
        # Login form
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("📧 Email Address", placeholder="your.email@example.com", key="login_email")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password", key="login_password")
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            col_a, col_b = st.columns(2)
            with col_a:
                remember_me = st.checkbox("Remember me")
            with col_b:
                st.markdown('<div style="text-align: right; padding-top: 0.5rem;"><a href="#" style="color: #B76E79; text-decoration: none; font-size: 0.9rem;">Forgot password?</a></div>', unsafe_allow_html=True)
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            submit_button = st.form_submit_button("🚀 Login", use_container_width=True)
            
            if submit_button:
                if not email or not password:
                    st.error("⚠️ Please fill in all fields.")
                else:
                    success, message, user_data = login_user(email, password)
                    
                    if success:
                        st.session_state["user"] = user_data
                        st.session_state["user_email"] = email
                        st.success(f"✅ {message}")
                        st.balloons()
                        
                        # Redirect to home
                        st.session_state["current_page"] = "home"
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Sign up link
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; color: rgba(255,255,255,0.7);">Don\'t have an account? <a href="#" style="color: #B76E79; text-decoration: none; font-weight: 600;">Sign Up</a></div>', unsafe_allow_html=True)
        
        # Quick signup button
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        if st.button("Create New Account", use_container_width=True, key="go_to_signup"):
            st.session_state["current_page"] = "signup"
            st.rerun()
        
        # Social login (UI only)
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; color: rgba(255,255,255,0.5); margin-bottom: 1rem;">Or continue with</div>', unsafe_allow_html=True)
        
        col_x, col_y, col_z = st.columns(3)
        with col_x:
            st.button("🔵 Facebook", use_container_width=True, disabled=True)
        with col_y:
            st.button("🔴 Google", use_container_width=True, disabled=True)
        with col_z:
            st.button("⚫ Apple", use_container_width=True, disabled=True)
        
        st.markdown('<div style="text-align: center; color: rgba(255,255,255,0.4); font-size: 0.85rem; margin-top: 1rem;">Social login coming soon</div>', unsafe_allow_html=True)
