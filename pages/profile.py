"""
Profile page for WERBEAUTY.
User profile management and settings.
"""

import streamlit as st
from config.theme import apply_theme
from utils.auth_manager import (
    is_logged_in, get_current_user, get_current_user_email,
    update_user_profile, update_user_preferences, change_password, logout_user
)
from components.navbar import render_navbar
from components.footer import render_footer


def render():
    """
    Render the profile page.
    """
    apply_theme()
    render_navbar()
    
    # Redirect if not logged in
    if not is_logged_in():
        st.warning("⚠️ Please login to access your profile.")
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        if st.button("Go to Login", use_container_width=True):
            st.session_state["current_page"] = "login"
            st.rerun()
        return
    
    user = get_current_user()
    email = get_current_user_email()
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Profile header
    st.markdown(f'<div style="text-align: center;"><h1 style="font-family: \'Playfair Display\', serif; font-size: 2.5rem; color: #B76E79; margin-bottom: 0.5rem;">My Profile</h1><p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 2rem;">Welcome back, {user["name"]}! 👋</p></div>', unsafe_allow_html=True)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Profile Info", "⚙️ Preferences", "🔒 Security", "📦 Orders"])
    
    # Tab 1: Profile Information
    with tab1:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Profile avatar
            st.markdown('<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #B76E79, #d4a5ad); border-radius: 24px;"><div style="font-size: 5rem; margin-bottom: 1rem;">👤</div><h3 style="color: white; margin: 0;">' + user["name"] + '</h3><p style="color: rgba(255,255,255,0.8); margin-top: 0.5rem;">' + email + '</p></div>', unsafe_allow_html=True)
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            # Account stats
            st.markdown('<div style="padding: 1.5rem; background: rgba(255, 255, 255, 0.05); border-radius: 18px; backdrop-filter: blur(10px);"><div style="text-align: center; color: rgba(255,255,255,0.7);"><div style="font-size: 1.8rem; font-weight: bold; color: #B76E79;">Member Since</div><div style="margin-top: 0.5rem;">' + user.get("created_at", "2025-01-01")[:10] + '</div></div></div>', unsafe_allow_html=True)
        
        with col2:
            # Edit profile form
            st.markdown("### Personal Information")
            
            with st.form("profile_form"):
                new_name = st.text_input("Full Name", value=user.get("name", ""))
                new_phone = st.text_input("Phone Number", value=user.get("profile", {}).get("phone", ""))
                new_address = st.text_input("Address", value=user.get("profile", {}).get("address", ""))
                
                col_a, col_b = st.columns(2)
                with col_a:
                    new_city = st.text_input("City", value=user.get("profile", {}).get("city", ""))
                with col_b:
                    new_country = st.text_input("Country", value=user.get("profile", {}).get("country", ""))
                
                new_birthday = st.date_input("Birthday", value=None)
                
                st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
                
                if st.form_submit_button("💾 Save Changes", use_container_width=True):
                    profile_data = {
                        "name": new_name,
                        "phone": new_phone,
                        "address": new_address,
                        "city": new_city,
                        "country": new_country,
                        "birthday": str(new_birthday) if new_birthday else ""
                    }
                    
                    success, message = update_user_profile(email, profile_data)
                    
                    if success:
                        st.success(f"✅ {message}")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
    
    # Tab 2: Preferences
    with tab2:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        st.markdown("### Beauty Preferences")
        
        with st.form("preferences_form"):
            skin_type = st.selectbox(
                "Skin Type",
                ["", "Oily", "Dry", "Combination", "Sensitive", "Normal"],
                index=0 if not user.get("preferences", {}).get("skin_type") else 
                      ["", "Oily", "Dry", "Combination", "Sensitive", "Normal"].index(user.get("preferences", {}).get("skin_type"))
            )
            
            st.markdown("### Communication Preferences")
            
            newsletter = st.checkbox(
                "📧 Receive newsletter with exclusive offers",
                value=user.get("preferences", {}).get("newsletter", True)
            )
            
            promotions = st.checkbox("🎁 Receive promotional emails", value=True)
            new_products = st.checkbox("✨ Get notified about new products", value=True)
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            if st.form_submit_button("💾 Update Preferences", use_container_width=True):
                preferences = {
                    "skin_type": skin_type,
                    "newsletter": newsletter
                }
                
                success, message = update_user_preferences(email, preferences)
                
                if success:
                    st.success(f"✅ {message}")
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
    
    # Tab 3: Security
    with tab3:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        st.markdown("### Change Password")
        
        with st.form("password_form"):
            old_password = st.text_input("Current Password", type="password")
            new_password = st.text_input("New Password", type="password")
            confirm_new_password = st.text_input("Confirm New Password", type="password")
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            if st.form_submit_button("🔒 Change Password", use_container_width=True):
                if not old_password or not new_password or not confirm_new_password:
                    st.error("⚠️ Please fill in all fields.")
                elif new_password != confirm_new_password:
                    st.error("❌ New passwords do not match.")
                else:
                    success, message = change_password(email, old_password, new_password)
                    
                    if success:
                        st.success(f"✅ {message}")
                    else:
                        st.error(f"❌ {message}")
        
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        st.markdown("### Account Actions")
        
        col_x, col_y = st.columns(2)
        
        with col_x:
            if st.button("🚪 Logout", use_container_width=True, type="secondary"):
                logout_user()
                st.success("✅ Logged out successfully!")
                st.session_state["current_page"] = "home"
                st.rerun()
        
        with col_y:
            if st.button("🗑️ Delete Account", use_container_width=True, type="secondary"):
                st.warning("⚠️ This feature is coming soon.")
    
    # Tab 4: Orders
    with tab4:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        st.markdown("### Order History")
        
        # Placeholder for orders
        st.info("📦 You haven't placed any orders yet. Start shopping to see your order history here!")
        
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        if st.button("🛍️ Start Shopping", use_container_width=True):
            st.session_state["current_page"] = "women"
            st.rerun()
    
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    render_footer()
