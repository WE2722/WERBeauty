"""
Utilities package for WERBEAUTY application. 
"""

from .cart_manager import add_to_cart, remove_from_cart, update_quantity, get_cart, clear_cart, is_in_cart, get_cart_total
from .favorites_manager import add_to_favorites, remove_from_favorites, get_favorites, is_favorite, clear_favorites
from .product_loader import load_women_products, load_men_products, get_product_by_id, filter_products, search_products
from .recommendation_engine import get_recommendations, get_trending, get_similar_products
from .helpers import format_price, generate_order_id, validate_email, validate_card_number
from .animation import get_animation_css, get_loading_skeleton