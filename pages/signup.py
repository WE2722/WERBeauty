"""
Signup page for WERBEAUTY.
User registration form.
"""

import streamlit as st
from utils.auth_manager import signup_user, is_logged_in


def render():
    """
    Render the signup page.
    """
    # Redirect if already logged in
    if is_logged_in():
        st.session_state["current_page"] = "home"
        st.rerun()
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Center the signup form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Signup header
        st.markdown('<div style="text-align: center;"><h1 style="font-family: \'Playfair Display\', serif; font-size: 2.5rem; color: #B76E79; margin-bottom: 0.5rem;">Create Account</h1><p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 2rem;">Join WERBEAUTY and discover luxury beauty</p></div>', unsafe_allow_html=True)
        
        # Signup form container
        st.markdown('<div class="glass-card" style="padding: 2rem; border-radius: 24px; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);">', unsafe_allow_html=True)
        
        # Signup form
        with st.form("signup_form", clear_on_submit=False):
            name = st.text_input("👤 Full Name", placeholder="John Doe", key="signup_name")
            email = st.text_input("📧 Email Address", placeholder="your.email@example.com", key="signup_email")
            
            # Gender selection
            gender = st.selectbox(
                "⚥ Gender",
                ["Female", "Male"],
                index=0,
                help="This will personalize your shopping experience"
            )
            
            password = st.text_input("🔒 Password", type="password", placeholder="At least 6 characters", key="signup_password")
            confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Re-enter password", key="signup_confirm")
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            agree_terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")
            newsletter = st.checkbox("Subscribe to newsletter for exclusive offers", value=True)
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            submit_button = st.form_submit_button("🎉 Create Account", use_container_width=True)
            
            if submit_button:
                if not name or not email or not password or not confirm_password:
                    st.error("⚠️ Please fill in all fields.")
                elif password != confirm_password:
                    st.error("❌ Passwords do not match.")
                elif not agree_terms:
                    st.error("⚠️ Please agree to the Terms of Service to continue.")
                else:
                    success, message = signup_user(email, password, name, gender)
                    
                    if success:
                        st.success(f"✅ {message}")
                        st.balloons()
                        st.session_state["signup_success"] = True
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
        
        # Show login button after successful signup (outside form)
        if st.session_state.get("signup_success"):
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            if st.button("Go to Login", use_container_width=True, key="go_to_login_after_signup"):
                st.session_state["signup_success"] = False
                st.session_state["current_page"] = "login"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Login link
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; color: rgba(255,255,255,0.7);">Already have an account? <a href="#" style="color: #B76E79; text-decoration: none; font-weight: 600;">Login</a></div>', unsafe_allow_html=True)
        
        # Quick login button
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        if st.button("Login to Existing Account", use_container_width=True, key="go_to_login"):
            st.session_state["current_page"] = "login"
            st.rerun()
        
        # Benefits section
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; color: rgba(255,255,255,0.7); margin-bottom: 1rem;"><strong>Why Join WERBEAUTY?</strong></div>', unsafe_allow_html=True)
        
        benefits_html = '<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; text-align: center; color: rgba(255,255,255,0.6); font-size: 0.9rem;"><div>🎁 Exclusive Offers</div><div>💎 VIP Rewards</div><div>📦 Order Tracking</div><div>❤️ Save Favorites</div></div>'
        st.markdown(benefits_html, unsafe_allow_html=True)
