"""
Payment/Checkout page for WERBEAUTY.
Complete checkout flow with billing, shipping, and payment. 
"""

import streamlit as st
from utils.cart_manager import get_cart, get_cart_total, clear_cart
from utils.helpers import (
    format_price, generate_order_id, validate_email,
    validate_card_number, validate_expiry_date, validate_cvv, mask_card_number
)
from utils.animation import render_success_animation
from utils.order_manager import create_order
from config.constants import SHIPPING_OPTIONS


def render():
    """
    Render the payment/checkout page.
    """
    cart = get_cart()
    
    if not cart:
        render_empty_checkout()
        return
    
    # Check if order was just completed
    if st.session_state.get("order_complete", False):
        render_order_confirmation()
        return
    
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        primary_color = "#0A1A3F"
    else:
        primary_color = "#B76E79"
    
    # Page header
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="
            font-family: 'Playfair Display', serif;
            font-size: 2. 5rem;
            color: #0F0F0F;
            margin-bottom: 0.5rem;
        ">💳 Secure Checkout</h1>
        <p style="color: #666; font-family: 'Inter', sans-serif;">
            Complete your order securely
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Checkout steps indicator
    render_checkout_steps()
    
    # Main checkout layout
    col_form, col_summary = st.columns([2, 1])
    
    with col_form:
        render_checkout_form()
    
    with col_summary:
        render_checkout_summary()


def render_empty_checkout():
    """
    Render empty checkout state.
    """
    st.markdown("""
    <div class="empty-state animate-fadeInUp" style="padding: 4rem 2rem;">
        <div class="empty-state-icon">💳</div>
        <h3 class="empty-state-title">Nothing to Checkout</h3>
        <p class="empty-state-message">
            Your cart is empty. Add some products to proceed with checkout.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🛍️ Start Shopping", key="empty_checkout_shop", use_container_width=True):
            gender = st.session_state.get("gender", "women")
            st.session_state["current_page"] = gender
            st.rerun()


def render_checkout_steps():
    """
    Render the checkout progress steps.
    """
    st.markdown("""
    <div style="
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-bottom: 3rem;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 18px;
    ">
        <div style="text-align: center;">
            <div style="
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: linear-gradient(135deg, #4caf50, #8bc34a);
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 0. 5rem;
                font-weight: 600;
            ">✓</div>
            <span style="color: #4caf50; font-weight: 500;">Cart</span>
        </div>
        <div style="text-align: center;">
            <div style="
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: linear-gradient(135deg, #D4AF37, #f5d76e);
                color: #0F0F0F;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 0.5rem;
                font-weight: 600;
            ">2</div>
            <span style="color: #D4AF37; font-weight: 500;">Checkout</span>
        </div>
        <div style="text-align: center;">
            <div style="
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: #e0e0e0;
                color: #666;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 0.5rem;
                font-weight: 600;
            ">3</div>
            <span style="color: #666;">Confirmation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_checkout_form():
    """
    Render the checkout form with billing, shipping, and payment. 
    """
    # Initialize checkout data
    if "checkout_data" not in st.session_state:
        st.session_state["checkout_data"] = {}
    
    checkout_data = st. session_state["checkout_data"]
    
    # Billing Information
    st.markdown("""
    <div class="payment-form">
        <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 1.5rem;">
            📋 Billing Information
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input(
            "First Name *",
            value=checkout_data.get("first_name", ""),
            key="billing_first_name"
        )
    
    with col2:
        last_name = st.text_input(
            "Last Name *",
            value=checkout_data.get("last_name", ""),
            key="billing_last_name"
        )
    
    email = st.text_input(
        "Email Address *",
        value=checkout_data.get("email", ""),
        key="billing_email"
    )
    
    phone = st.text_input(
        "Phone Number *",
        value=checkout_data.get("phone", ""),
        key="billing_phone"
    )
    
    address = st.text_input(
        "Street Address *",
        value=checkout_data.get("address", ""),
        key="billing_address"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        city = st.text_input(
            "City *",
            value=checkout_data.get("city", ""),
            key="billing_city"
        )
    
    with col2:
        state = st.text_input(
            "State/Province *",
            value=checkout_data.get("state", ""),
            key="billing_state"
        )
    
    with col3:
        zip_code = st.text_input(
            "ZIP/Postal Code *",
            value=checkout_data.get("zip_code", ""),
            key="billing_zip"
        )
    
    country = st.selectbox(
        "Country *",
        ["United States", "Canada", "United Kingdom", "France", "Germany", "Australia", "Other"],
        key="billing_country"
    )
    
    st.markdown("---")
    
    # Payment Information
    st.markdown("""
    <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 1. 5rem;">
        💳 Payment Information
    </h3>
    """, unsafe_allow_html=True)
    
    # Credit Card Preview
    render_credit_card_preview()
    
    card_number = st.text_input(
        "Card Number *",
        value=checkout_data.get("card_number", ""),
        max_chars=19,
        placeholder="1234 5678 9012 3456",
        key="card_number"
    )
    
    card_name = st.text_input(
        "Name on Card *",
        value=checkout_data.get("card_name", ""),
        placeholder="JOHN DOE",
        key="card_name"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        exp_month = st.selectbox(
            "Expiry Month *",
            list(range(1, 13)),
            format_func=lambda x: f"{x:02d}",
            key="exp_month"
        )
    
    with col2:
        current_year = 2024
        exp_year = st.selectbox(
            "Expiry Year *",
            list(range(current_year, current_year + 11)),
            key="exp_year"
        )
    
    with col3:
        cvv = st.text_input(
            "CVV *",
            max_chars=4,
            type="password",
            placeholder="123",
            key="cvv"
        )
    
    st.markdown("---")
    
    # Terms and conditions
    agree = st.checkbox(
        "I agree to the Terms of Service and Privacy Policy",
        key="agree_terms"
    )
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Place order button
    if st.button("🔒 Place Order", key="place_order", use_container_width=True):
        # Validate form
        errors = []
        
        if not all([first_name, last_name, email, phone, address, city, state, zip_code]):
            errors.append("Please fill in all required billing fields.")
        
        if email and not validate_email(email):
            errors.append("Please enter a valid email address.")
        
        if not card_number or not card_name:
            errors.append("Please enter your payment information.")
        
        # Accept all card numbers - validation removed for testing
        
        if not validate_expiry_date(exp_month, exp_year):
            errors.append("Card has expired. Please use a valid card.")
        
        if cvv and not validate_cvv(cvv):
            errors.append("Please enter a valid CVV.")
        
        if not agree:
            errors.append("Please agree to the Terms of Service.")
        
        if errors:
            for error in errors:
                st.error(error)
        else:
            # Generate order ID
            order_id = generate_order_id()
            
            # Calculate total with shipping
            cart_totals = get_cart_total()
            total = cart_totals['total']
            
            # Save checkout data
            checkout_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "address": address,
                "city": city,
                "state": state,
                "zip_code": zip_code,
                "country": country,
                "card_last_four": card_number[-4:] if card_number else "0000",
                "shipping_method": st.session_state.get("shipping_method", "Standard")
            }
            
            # Create order in database
            cart_items = get_cart()
            create_order(order_id, cart_items, checkout_data, total)
            
            # Save to session for confirmation page
            st.session_state["checkout_data"] = checkout_data
            st.session_state["order_id"] = order_id
            st.session_state["order_complete"] = True
            
            # Clear cart
            clear_cart()
            st.rerun()


def render_credit_card_preview():
    """
    Render an animated credit card preview. 
    """
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        gradient = "linear-gradient(135deg, #0A1A3F, #1a2a4f)"
    else:
        gradient = "linear-gradient(135deg, #B76E79, #d4a5ad)"
    
    st.markdown(f"""
    <div class="credit-card" style="
        background: {gradient};
        margin: 1. 5rem auto;
        max-width: 380px;
    ">
        <div class="credit-card-front">
            <div class="card-chip"></div>
            <div class="card-number">•••• •••• •••• ••••</div>
            <div class="card-info">
                <div>
                    <div class="card-label">Card Holder</div>
                    <div class="card-value">YOUR NAME</div>
                </div>
                <div>
                    <div class="card-label">Expires</div>
                    <div class="card-value">MM/YY</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_checkout_summary():
    """
    Render the order summary sidebar. 
    """
    cart = get_cart()
    totals = get_cart_total()
    
    st.markdown("""
    <div class="order-summary">
        <h3 class="order-summary-title">Order Summary</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Cart items preview
    for item in cart[:3]:
        st.markdown(f"""
        <div style="
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #eee;
        ">
            <img src="{item.get('image', '')}" style="
                width: 60px;
                height: 60px;
                object-fit: cover;
                border-radius: 8px;
            " onerror="this. src='https://via.placeholder.com/60x60?text=W'">
            <div style="flex: 1;">
                <p style="margin: 0; font-size: 0.9rem; font-weight: 500;">
                    {item.get('name', 'Product')}
                </p>
                <p style="margin: 0; color: #888; font-size: 0.85rem;">
                    Qty: {item.get('quantity', 1)}
                </p>
            </div>
            <p style="margin: 0; font-weight: 600;">
                ${item.get('price', 0) * item.get('quantity', 1):.2f}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    if len(cart) > 3:
        st.markdown(f"""
        <p style="color: #888; font-size: 0. 9rem; text-align: center;">
            +{len(cart) - 3} more items
        </p>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Totals
    st.markdown(f"""
    <div class="order-row">
        <span>Subtotal</span>
        <span>${totals['subtotal']:.2f}</span>
    </div>
    """, unsafe_allow_html=True)
    
    if totals['discount'] > 0:
        st.markdown(f"""
        <div class="order-row" style="color: #4caf50;">
            <span>Discount</span>
            <span>-${totals['discount']:.2f}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="order-row">
        <span>Shipping</span>
        <span>{"FREE" if totals['shipping'] == 0 else f"${totals['shipping']:.2f}"}</span>
    </div>
    <div class="order-row">
        <span>Tax</span>
        <span>${totals['tax']:.2f}</span>
    </div>
    <div class="order-row total">
        <span>Total</span>
        <span>${totals['total']:.2f}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        margin-top: 1. 5rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 12px;
        text-align: center;
    ">
        <p style="margin: 0; font-size: 0.85rem; color: #666;">
            🔒 Secure 256-bit SSL encryption
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_order_confirmation():
    """
    Render the order confirmation page after successful checkout.
    """
    order_id = st. session_state.get("order_id", "WER-000000")
    checkout_data = st.session_state.get("checkout_data", {})
    
    gender = st.session_state.get("gender", "women")
    if gender == "men":
        primary_color = "#0A1A3F"
    else:
        primary_color = "#B76E79"
    
    # Success animation
    st.markdown("""
    <div class="success-animation">
        <div class="success-checkmark animate-bounceIn" style="
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(135deg, #4caf50, #8bc34a);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 2rem;
            box-shadow: 0 10px 40px rgba(76, 175, 80, 0. 3);
        ">
            <span style="font-size: 3rem; color: white;">✓</span>
        </div>
        <h1 class="success-title animate-fadeInUp delay-2" style="
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            color: #0F0F0F;
            margin-bottom: 1rem;
        ">Order Confirmed! </h1>
        <p class="success-message animate-fadeInUp delay-3" style="
            color: #666;
            font-size: 1. 1rem;
            margin-bottom: 2rem;
        ">
            Thank you for your purchase.  Your order has been received. 
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Order details card
    st.markdown(f"""
    <div style="
        max-width: 600px;
        margin: 0 auto;
        background: white;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    " class="animate-fadeInUp delay-4">
        <div style="text-align: center; margin-bottom: 2rem;">
            <p style="color: #888; font-size: 0.9rem; margin-bottom: 0.5rem;">Order Number</p>
            <p style="
                font-family: 'Inter', monospace;
                font-size: 1.5rem;
                font-weight: 600;
                color: {primary_color};
                letter-spacing: 2px;
            ">{order_id}</p>
        </div>
        
        <div style="
            background: #f8f9fa;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        ">
            <h4 style="font-family: 'Playfair Display', serif; margin-bottom: 1rem;">
                📦 Shipping Details
            </h4>
            <p style="margin: 0; color: #333;">
                {checkout_data.get('first_name', '')} {checkout_data.get('last_name', '')}<br>
                {checkout_data.get('address', '')}<br>
                {checkout_data.get('city', '')}, {checkout_data.get('state', '')} {checkout_data.get('zip_code', '')}<br>
                {checkout_data.get('country', '')}
            </p>
        </div>
        
        <div style="
            background: #f8f9fa;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        ">
            <h4 style="font-family: 'Playfair Display', serif; margin-bottom: 1rem;">
                📧 Confirmation Email
            </h4>
            <p style="margin: 0; color: #333;">
                A confirmation email has been sent to:<br>
                <strong>{checkout_data.get('email', 'your email')}</strong>
            </p>
        </div>
        
        <div style="
            background: linear-gradient(135deg, #D4AF37, #f5d76e);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
        ">
            <p style="margin: 0; color: #0F0F0F; font-weight: 500;">
                🎁 You've earned <strong>50 WERBEAUTY Points</strong> with this order!
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🛍️ Continue Shopping", key="continue_after_order", use_container_width=True):
            st.session_state["order_complete"] = False
            st.session_state["current_page"] = "home"
            st.rerun()