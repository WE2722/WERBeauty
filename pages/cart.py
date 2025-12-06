"""
Shopping cart page for WERBEAUTY. 
Full cart management with promo codes and checkout.
"""

import streamlit as st
from utils.cart_manager import get_cart, remove_from_cart, update_quantity, get_cart_total, clear_cart
from utils.helpers import format_price
from config.constants import PROMO_CODES, SHIPPING_OPTIONS


def render():
    """
    Render the shopping cart page.
    """
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
            font-size: 2.5rem;
            color: #0F0F0F;
            margin-bottom: 0. 5rem;
        ">🛒 Your Shopping Cart</h1>
        <p style="color: #666; font-family: 'Inter', sans-serif;">
            Review your items and proceed to checkout
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    cart = get_cart()
    
    if not cart:
        render_empty_cart()
        return
    
    # Cart layout
    col_items, col_summary = st.columns([2, 1])
    
    with col_items:
        render_cart_items(cart)
    
    with col_summary:
        render_order_summary()


def render_empty_cart():
    """
    Render empty cart state.
    """
    st.markdown("""
    <div class="empty-state animate-fadeInUp" style="padding: 4rem 2rem;">
        <div class="empty-state-icon">🛒</div>
        <h3 class="empty-state-title">Your Cart is Empty</h3>
        <p class="empty-state-message">
            Looks like you haven't added anything to your cart yet. <br>
            Discover our luxury collection and find your perfect products.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🛍️ Start Shopping", key="empty_cart_shop", use_container_width=True):
            gender = st.session_state.get("gender", "women")
            st.session_state["current_page"] = gender
            st.rerun()


def render_cart_items(cart: list):
    """
    Render all cart items with quantity controls.
    """
    st.markdown("""
    <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 1. 5rem;">
        Cart Items
    </h3>
    """, unsafe_allow_html=True)
    
    for idx, item in enumerate(cart):
        render_cart_item(item, idx)
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Clear cart button
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🗑️ Clear Cart", key="clear_cart_btn"):
            clear_cart()
            st.rerun()
    with col2:
        gender = st.session_state.get("gender", "women")
        if st.button("🛍️ Continue Shopping", key="continue_shopping"):
            st.session_state["current_page"] = gender
            st.rerun()


def render_cart_item(item: dict, index: int):
    """
    Render a single cart item with controls.
    """
    product_id = item.get("id", "")
    name = item.get("name", "Product")
    price = item.get("price", 0)
    quantity = item.get("quantity", 1)
    image = item.get("image", "https://via.placeholder. com/120x120? text=Product")
    category = item.get("category", "")
    
    st.markdown(f"""
    <div class="cart-item animate-fadeInUp" style="animation-delay: {index * 0.1}s;">
        <img src="{image}" alt="{name}" class="cart-item-image" 
             onerror="this. src='https://via.placeholder.com/120x120?text=WERBEAUTY'">
        <div class="cart-item-details">
            <div>
                <p style="color: #888; font-size: 0.85rem; margin-bottom: 0.3rem;">{category}</p>
                <h4 class="cart-item-title">{name}</h4>
            </div>
            <p class="cart-item-price">${price:.2f}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quantity controls
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        if st.button("➖", key=f"dec_{product_id}_{index}"):
            new_qty = max(0, quantity - 1)
            if new_qty == 0:
                remove_from_cart(product_id)
            else:
                update_quantity(product_id, new_qty)
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 0.5rem;
            background: #f5f5f5;
            border-radius: 8px;
            font-weight: 600;
        ">{quantity}</div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("➕", key=f"inc_{product_id}_{index}"):
            update_quantity(product_id, quantity + 1)
            st.rerun()
    
    with col4:
        if st.button("🗑️", key=f"remove_{product_id}_{index}"):
            remove_from_cart(product_id)
            st.rerun()
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)


def render_order_summary():
    """
    Render the order summary sidebar.
    """
    totals = get_cart_total()
    
    st.markdown("""
    <div class="order-summary">
        <h3 class="order-summary-title">Order Summary</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Promo code section
    render_promo_section()
    
    st.markdown("---")
    
    # Shipping selection
    st.markdown("**Shipping Method**")
    shipping_options = list(SHIPPING_OPTIONS.keys())
    shipping_labels = [f"{SHIPPING_OPTIONS[k]['name']} - ${SHIPPING_OPTIONS[k]['price']:.2f}" 
                       if SHIPPING_OPTIONS[k]['price'] > 0 else f"{SHIPPING_OPTIONS[k]['name']} - FREE"
                       for k in shipping_options]
    
    selected_shipping = st.selectbox(
        "Shipping",
        shipping_options,
        format_func=lambda x: f"{SHIPPING_OPTIONS[x]['name']} - ${SHIPPING_OPTIONS[x]['price']:.2f}" 
                              if SHIPPING_OPTIONS[x]['price'] > 0 else f"{SHIPPING_OPTIONS[x]['name']} - FREE",
        label_visibility="collapsed",
        key="shipping_select"
    )
    st.session_state["shipping_method"] = selected_shipping
    
    # Recalculate totals with new shipping
    totals = get_cart_total()
    
    st.markdown(f"""
    <p style="color: #666; font-size: 0.85rem; margin-top: 0.5rem;">
        📦 {SHIPPING_OPTIONS[selected_shipping]['days']}
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Order breakdown
    st.markdown(f"""
    <div class="order-row">
        <span>Subtotal ({totals['item_count']} items)</span>
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
        <span>Tax (8%)</span>
        <span>${totals['tax']:.2f}</span>
    </div>
    <div class="order-row total">
        <span>Total</span>
        <span>${totals['total']:.2f}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Free shipping notice
    if totals['subtotal'] < 100:
        remaining = 100 - totals['subtotal']
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #fff3cd, #ffeeba);
            padding: 1rem;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 1rem;
        ">
            <p style="margin: 0; font-size: 0.9rem;">
                🚚 Add <strong>${remaining:.2f}</strong> more for FREE shipping!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Checkout button
    if st.button("💳 Proceed to Checkout", key="checkout_btn", use_container_width=True):
        st.session_state["current_page"] = "payment"
        st. rerun()


def render_promo_section():
    """
    Render the promo code input section.
    """
    st.markdown("**Promo Code**")
    
    promo_applied = st.session_state.get("promo_applied", False)
    current_promo = st.session_state.get("promo_code", "")
    
    if promo_applied and current_promo:
        promo_info = PROMO_CODES.get(current_promo.upper(), {'description': 'Special discount applied!'})
        st.markdown(f"""
        <div class="promo-section promo-applied">
            <p style="margin: 0; color: #2e7d32;">
                ✅ <strong>{current_promo.upper()}</strong> applied! <br>
                <span style="font-size: 0.85rem;">{promo_info.get('description', 'Special discount applied!')}</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Remove Code", key="remove_promo"):
            st.session_state["promo_code"] = ""
            st.session_state["promo_applied"] = False
            st.rerun()
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            promo_input = st.text_input(
                "Promo Code",
                placeholder="Enter code",
                label_visibility="collapsed",
                key="promo_input"
            )
        
        with col2:
            if st.button("Apply", key="apply_promo"):
                # Accept all promo codes
                st.session_state["promo_code"] = promo_input.upper()
                st.session_state["promo_applied"] = True
                st.rerun()