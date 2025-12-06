"""
Profile page for WERBEAUTY.
User profile management and settings.
"""

import streamlit as st
from utils.auth_manager import (
    is_logged_in, get_current_user, get_current_user_email,
    update_user_profile, update_user_preferences, change_password, logout_user
)
from utils.order_manager import get_user_orders, cancel_order
from utils.review_manager import get_user_reviews, delete_review
from utils.helpers import format_price
from datetime import date


def render():
    """
    Render the profile page.
    """
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
    
    # Get gender-based colors
    user_gender = user.get("gender", "Female")
    if user_gender == "Male":
        primary_color = "#4A90E2"  # Blue
        secondary_color = "#7BB3E8"  # Light blue
        gradient = "linear-gradient(135deg, #4A90E2, #7BB3E8)"
    else:
        primary_color = "#B76E79"  # Rose gold
        secondary_color = "#d4a5ad"  # Light rose
        gradient = "linear-gradient(135deg, #B76E79, #d4a5ad)"
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Profile header
    st.markdown(f'<div style="text-align: center;"><h1 style="font-family: \'Playfair Display\', serif; font-size: 2.5rem; color: {primary_color}; margin-bottom: 0.5rem;">My Profile</h1><p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 2rem;">Welcome back, {user["name"]}! 👋</p></div>', unsafe_allow_html=True)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Profile Info", "⚙️ Preferences", "🔒 Security", "📦 Orders", "⭐ My Reviews"])
    
    # Tab 1: Profile Information
    with tab1:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Profile avatar
            st.markdown(f'<div style="text-align: center; padding: 2rem; background: {gradient}; border-radius: 24px;"><div style="font-size: 5rem; margin-bottom: 1rem;">👤</div><h3 style="color: white; margin: 0;">' + user["name"] + '</h3><p style="color: rgba(255,255,255,0.8); margin-top: 0.5rem;">' + email + '</p></div>', unsafe_allow_html=True)
            
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            # Account stats
            st.markdown(f'<div style="padding: 1.5rem; background: rgba(255, 255, 255, 0.05); border-radius: 18px; backdrop-filter: blur(10px);"><div style="text-align: center; color: rgba(255,255,255,0.7);"><div style="font-size: 1.8rem; font-weight: bold; color: {primary_color};">Member Since</div><div style="margin-top: 0.5rem;">' + user.get("created_at", "2025-01-01")[:10] + '</div></div></div>', unsafe_allow_html=True)
        
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
                
                # Parse existing birthday if available
                existing_birthday = user.get("profile", {}).get("birthday", "")
                birthday_value = None
                if existing_birthday:
                    try:
                        from datetime import datetime
                        birthday_value = datetime.strptime(existing_birthday, "%Y-%m-%d").date()
                    except:
                        birthday_value = None
                
                new_birthday = st.date_input("Birthday", value=birthday_value, min_value=date(1900, 1, 1), max_value=date(2025, 12, 31))
                
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
        
        # Get user orders
        orders = get_user_orders()
        
        if not orders:
            st.info("📦 You haven't placed any orders yet. Start shopping to see your order history here!")
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            if st.button("🛍️ Start Shopping", use_container_width=True):
                st.session_state["current_page"] = "women"
                st.rerun()
        else:
            # Display orders (newest first)
            for order in reversed(orders):
                order_id = order.get("order_id", "N/A")
                order_date = order.get("date", "N/A")
                order_status = order.get("status", "Processing")
                order_total = order.get("total", 0)
                order_items = order.get("items", [])
                
                # Status color
                status_colors = {
                    "Processing": "#FFA500",
                    "Shipped": "#2196F3",
                    "Delivered": "#4CAF50",
                    "Cancelled": "#F44336"
                }
                status_color = status_colors.get(order_status, "#666")
                
                # Order card
                st.markdown(f"""
                <div style="
                    background: rgba(255, 255, 255, 0.05);
                    backdrop-filter: blur(10px);
                    padding: 1.5rem;
                    border-radius: 16px;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    margin-bottom: 1rem;
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <div>
                            <h3 style="margin: 0; color: #B76E79; font-size: 1.1rem;">Order #{order_id}</h3>
                            <p style="margin: 0.25rem 0 0 0; color: #999; font-size: 0.9rem;">{order_date}</p>
                        </div>
                        <div style="
                            padding: 0.5rem 1rem;
                            border-radius: 20px;
                            background: {status_color}20;
                            color: {status_color};
                            font-weight: 600;
                            font-size: 0.9rem;
                        ">{order_status}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Order items
                with st.expander(f"📦 View {len(order_items)} item(s) - Total: {format_price(order_total)}"):
                    for item in order_items:
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.markdown(f"**{item.get('name', 'Unknown')}**")
                            st.caption(f"Brand: {item.get('brand', 'N/A')}")
                        with col2:
                            st.markdown(f"Qty: {item.get('quantity', 1)}")
                        with col3:
                            st.markdown(f"{format_price(item.get('price', 0))}")
                    
                    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
                    
                    # Order actions
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        if order_status == "Processing":
                            if st.button(f"❌ Cancel Order", key=f"cancel_{order_id}", use_container_width=True):
                                if cancel_order(order_id):
                                    st.success("✅ Order cancelled successfully!")
                                    st.rerun()
                                else:
                                    st.error("Failed to cancel order.")
                    
                    with col_b:
                        if st.button(f"📧 Contact Support", key=f"support_{order_id}", use_container_width=True):
                            st.info("💬 Please email support@werbeauty.com for assistance.")
                
                st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
    
    # Tab 5: My Reviews
    with tab5:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        st.markdown("### My Reviews & Comments")
        
        # Get user reviews
        user_reviews = get_user_reviews()
        
        if not user_reviews:
            st.info("⭐ You haven't written any reviews yet. Share your experience with products you've tried!")
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            if st.button("🛍️ Browse Products", use_container_width=True):
                st.session_state["current_page"] = "women"
                st.rerun()
        else:
            st.markdown(f"<p style='color: rgba(255,255,255,0.7);'>You have written {len(user_reviews)} review(s)</p>", unsafe_allow_html=True)
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
            
            # Display reviews (newest first)
            for review in reversed(user_reviews):
                product_id = review.get("product_id", "N/A")
                rating = review.get("rating", 0)
                comment = review.get("comment", "")
                review_date = review.get("date", "N/A")
                
                # Rating stars
                stars = "⭐" * rating + "☆" * (5 - rating)
                
                # Review card
                st.markdown(f"""
                <div style="
                    background: rgba(255, 255, 255, 0.05);
                    backdrop-filter: blur(10px);
                    padding: 1.5rem;
                    border-radius: 16px;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    margin-bottom: 1rem;
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <div style="font-size: 1.3rem;">{stars}</div>
                        <div style="color: #999; font-size: 0.9rem;">{review_date}</div>
                    </div>
                    <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0; line-height: 1.6;">{comment}</p>
                    <p style="color: #B76E79; font-size: 0.9rem; margin-top: 0.5rem;">Product ID: {product_id}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Review actions
                col_del, col_edit = st.columns([1, 3])
                
                with col_del:
                    if st.button(f"🗑️ Delete", key=f"delete_review_{product_id}", use_container_width=True):
                        if delete_review(product_id):
                            st.success("✅ Review deleted successfully!")
                            st.rerun()
                        else:
                            st.error("Failed to delete review.")
                
                st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
    
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)

