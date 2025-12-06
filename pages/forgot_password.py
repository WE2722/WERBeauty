"""
Forgot Password page for WERBEAUTY.
Password reset request form.
"""

import streamlit as st
from utils.auth_manager import initiate_password_reset, is_logged_in


def render():
    """
    Render the forgot password page.
    """
    # Redirect if already logged in
    if is_logged_in():
        st.session_state["current_page"] = "home"
        st.rerun()
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Center the form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Header
        st.markdown('''
        <div style="text-align: center;">
            <h1 style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #B76E79; margin-bottom: 0.5rem;">
                Forgot Password?
            </h1>
            <p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 2rem;">
                No worries, we'll send you reset instructions 🔒
            </p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Form container
        st.markdown('''
        <div class="glass-card" style="
            padding: 2rem; 
            border-radius: 24px; 
            background: rgba(255, 255, 255, 0.05); 
            backdrop-filter: blur(10px); 
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        ">
        ''', unsafe_allow_html=True)
        
        # Information box
        st.markdown('''
        <div style="
            background: rgba(183, 110, 121, 0.1); 
            border-left: 4px solid #B76E79; 
            padding: 1rem; 
            border-radius: 8px; 
            margin-bottom: 1.5rem;
        ">
            <p style="color: rgba(255,255,255,0.8); margin: 0; line-height: 1.6;">
                💡 <strong>How it works:</strong><br>
                Enter your email address and we'll send you a temporary password. 
                Use it to log in, then change it immediately in your profile settings.
            </p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Reset form
        with st.form("forgot_password_form", clear_on_submit=False):
            email = st.text_input(
                "📧 Email Address", 
                placeholder="your.email@example.com",
                key="forgot_password_email",
                help="Enter the email address associated with your account"
            )
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            submit_button = st.form_submit_button("🚀 Send Reset Email", use_container_width=True)
            
            if submit_button:
                if not email:
                    st.error("⚠️ Please enter your email address.")
                elif '@' not in email or '.' not in email:
                    st.error("⚠️ Please enter a valid email address.")
                else:
                    success, message = initiate_password_reset(email)
                    
                    if success:
                        st.success(f"✅ {message}")
                        
                        # Show additional instructions
                        st.markdown('''
                        <div style="
                            background: rgba(76, 175, 80, 0.1); 
                            border: 1px solid rgba(76, 175, 80, 0.3); 
                            padding: 1.5rem; 
                            border-radius: 12px; 
                            margin-top: 1.5rem;
                        ">
                            <p style="color: rgba(255,255,255,0.9); margin: 0 0 1rem; font-weight: 600;">
                                📬 Check your email!
                            </p>
                            <p style="color: rgba(255,255,255,0.8); margin: 0 0 0.5rem; line-height: 1.6; font-size: 0.95rem;">
                                ✉️ We've sent a temporary password to your email<br>
                                ⏱️ The temporary password expires in 1 hour<br>
                                🔑 Use it to log in, then change your password<br>
                                📧 Check your spam folder if you don't see it
                            </p>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
                        
                        # Go to login button
                        if st.button("Go to Login Page", use_container_width=True, type="primary"):
                            st.session_state["current_page"] = "login"
                            st.rerun()
                    else:
                        st.error(f"❌ {message}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Back to login link
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('''
        <div style="text-align: center; color: rgba(255,255,255,0.7);">
            Remember your password? 
            <a href="#" style="color: #B76E79; text-decoration: none; font-weight: 600;">Back to Login</a>
        </div>
        ''', unsafe_allow_html=True)
        
        # Back to login button
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if st.button("← Back to Login", use_container_width=True, key="back_to_login"):
                st.session_state["current_page"] = "login"
                st.rerun()
        
        # Support info
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        st.markdown('''
        <div style="
            text-align: center; 
            color: rgba(255,255,255,0.5); 
            font-size: 0.9rem; 
            padding: 1.5rem; 
            background: rgba(255, 255, 255, 0.02); 
            border-radius: 12px;
        ">
            <p style="margin: 0 0 0.5rem;">
                💬 <strong>Need Help?</strong>
            </p>
            <p style="margin: 0;">
                Contact our support team at <span style="color: #B76E79;">support@werbeauty.com</span>
            </p>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
