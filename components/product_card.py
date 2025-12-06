"""
Product card component for WERBEAUTY. 
Displays individual products with animations and interactions.
"""

import streamlit as st
from utils.cart_manager import add_to_cart, remove_from_cart, is_in_cart
from utils.favorites_manager import add_to_favorites, remove_from_favorites, is_favorite


def render_star_rating(rating: float) -> str:
    """
    Generate HTML for star rating display.
    
    Args:
        rating: Product rating (0-5)
    
    Returns:
        HTML string for star rating
    """
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    
    stars_html = "★" * full_stars
    if half_star:
        stars_html += "☆"
    stars_html += '<span class="star-empty">' + "★" * empty_stars + '</span>'
    
    return f'<div class="star-rating">{stars_html}</div>'


def render_product_card(product: dict, index: int, show_actions: bool = True, key_prefix: str = ""):
    """
    Render a single product card with image, details, and actions.
    
    Args:
        product: Product dictionary with details
        index: Unique index for the product
        show_actions: Whether to show add to cart/favorites buttons
        key_prefix: Prefix for unique keys to avoid duplicates
    """
    product_id = product.get("id", index)
    name = product.get("name", "Product Name")
    price = product.get("price", 0)
    image = product.get("image", "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400&h=400&fit=crop")
    rating = product.get("rating", 4.5)
    badge = product.get("badge", "")
    category = product.get("category", "")
    
    # Generate unique key
    unique_key = f"{key_prefix}_{product_id}_{index}" if key_prefix else f"{product_id}_{index}"
    
    in_cart = is_in_cart(product_id)
    in_favorites = is_favorite(product_id)
    
    # Badge HTML
    badge_html = f'<div class="product-card-badge">{badge}</div>' if badge else ""
    
    # Favorite icon
    fav_icon = "❤️" if in_favorites else "🤍"
    
    # Favorite title
    fav_title = 'Remove from' if in_favorites else 'Add to'
    
    # Build card HTML as single line
    card_html = f'<div class="product-card animate-fadeInUp delay-{(index % 5) + 1}" style="animation-delay: {index * 0.1}s;">{badge_html}<div class="product-card-favorite" title="{fav_title} favorites">{fav_icon}</div><img src="{image}" alt="{name}" class="product-card-image" onerror="this.src=\'https://via.placeholder.com/400x400?text=WERBEAUTY\'"><div class="product-card-content"><p style="color: #888; font-size: 0.85rem; margin-bottom: 0.3rem;">{category}</p><h3 class="product-card-title">{name}</h3>{render_star_rating(rating)}<p class="product-card-price">${price:.2f}</p></div></div>'
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    if show_actions:
        col1, col2 = st.columns(2)
        
        with col1:
            if in_cart:
                if st.button("✓ In Cart", key=f"cart_{unique_key}", use_container_width=True):
                    remove_from_cart(product_id)
                    st.rerun()
            else:
                if st.button("🛒 Add", key=f"cart_{unique_key}", use_container_width=True):
                    add_to_cart(product)
                    st.rerun()
        
        with col2:
            if in_favorites:
                if st.button("❤️ Saved", key=f"fav_{unique_key}", use_container_width=True):
                    remove_from_favorites(product_id)
                    st.rerun()
            else:
                if st.button("🤍 Save", key=f"fav_{unique_key}", use_container_width=True):
                    add_to_favorites(product)
                    st.rerun()


def render_product_grid(products: list, columns: int = 4, key_prefix: str = ""):
    """
    Render a grid of product cards. 
    
    Args:
        products: List of product dictionaries
        columns: Number of columns in the grid
        key_prefix: Prefix for unique keys to avoid duplicates
    """
    if not products:
        st.markdown('<div class="empty-state"><div class="empty-state-icon">🔍</div><h3 class="empty-state-title">No Products Found</h3><p class="empty-state-message">Try adjusting your filters or search query.</p></div>', unsafe_allow_html=True)
        return
    
    # Create grid
    cols = st.columns(columns)
    
    for idx, product in enumerate(products):
        with cols[idx % columns]:
            render_product_card(product, idx, key_prefix=key_prefix)
            st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)