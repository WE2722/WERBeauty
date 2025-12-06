"""
Recommendation engine for WERBEAUTY.
Session-based product recommendations using similarity scoring.
"""

import streamlit as st
from typing import Dict, List
from utils.product_loader import load_women_products, load_men_products, get_product_by_id


def get_recommendations(limit: int = 8) -> List[Dict]:
    """
    Get personalized product recommendations based on user behavior.
    
    Args:
        limit: Maximum number of recommendations to return
    
    Returns:
        List of recommended products
    """
    gender = st.session_state.get("gender", "women")
    view_history = st.session_state.get("view_history", [])
    favorites = st.session_state.get("favorites", [])
    cart = st.session_state.get("cart", [])
    
    # Load products based on gender preference
    if gender == "men":
        products = load_men_products()
    else:
        products = load_women_products()
    
    # Get IDs of items already in cart or favorites
    exclude_ids = set()
    for item in cart:
        exclude_ids.add(item.get("id"))
    # Favorites are now stored as product IDs (strings)
    exclude_ids.update(favorites)
    
    # Calculate scores for each product
    scored_products = []
    
    # Get categories from user history
    history_categories = {}
    for item in view_history:
        cat = item.get("category", "")
        history_categories[cat] = history_categories.get(cat, 0) + 1
    
    # Load favorite products to get their categories
    for fav_id in favorites:
        fav_product = get_product_by_id(fav_id)
        if fav_product:
            cat = fav_product.get("category", "")
            history_categories[cat] = history_categories.get(cat, 0) + 2  # Weight favorites higher
    
    for item in cart:
        cat = item.get("category", "")
        history_categories[cat] = history_categories.get(cat, 0) + 3  # Weight cart items highest
    
    for product in products:
        if product.get("id") in exclude_ids:
            continue
        
        score = 0
        
        # Score based on category preference
        product_category = product.get("category", "")
        if product_category in history_categories:
            score += history_categories[product_category] * 10
        
        # Score based on rating
        score += product.get("rating", 0) * 5
        
        # Score based on popularity
        score += product.get("popularity", 0) * 0.5
        
        # Bonus for badges
        if product.get("badge"):
            score += 8
        
        scored_products.append((score, product))
    
    # Sort by score and return top results
    scored_products.sort(key=lambda x: x[0], reverse=True)
    
    return [product for score, product in scored_products[:limit]]


def get_trending(limit: int = 8) -> List[Dict]:
    """
    Get trending products based on popularity scores.
    
    Args:
        limit: Maximum number of products to return
    
    Returns:
        List of trending products
    """
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        products = load_men_products()
    else:
        products = load_women_products()
    
    # Sort by popularity
    trending = sorted(products, key=lambda x: x.get("popularity", 0), reverse=True)
    
    return trending[:limit]


def get_similar_products(product_id: str, limit: int = 4) -> List[Dict]:
    """
    Get products similar to a given product.
    
    Args:
        product_id: ID of the reference product
        limit: Maximum number of similar products to return
    
    Returns:
        List of similar products
    """
    # Load all products
    all_products = load_women_products() + load_men_products()
    
    # Find the reference product
    reference = None
    for product in all_products:
        if product. get("id") == product_id:
            reference = product
            break
    
    if not reference:
        return []
    
    ref_category = reference.get("category", "")
    ref_price = reference.get("price", 0)
    
    # Score similar products
    similar = []
    
    for product in all_products:
        if product.get("id") == product_id:
            continue
        
        score = 0
        
        # Same category = high similarity
        if product.get("category", "") == ref_category:
            score += 50
        
        # Similar price range
        price_diff = abs(product.get("price", 0) - ref_price)
        if price_diff < 20:
            score += 30
        elif price_diff < 50:
            score += 15
        
        # Similar rating
        rating_diff = abs(product.get("rating", 0) - reference.get("rating", 0))
        if rating_diff < 0.5:
            score += 10
        
        if score > 0:
            similar.append((score, product))
    
    similar.sort(key=lambda x: x[0], reverse=True)
    
    return [product for score, product in similar[:limit]]


def get_also_bought(product_id: str, limit: int = 4) -> List[Dict]:
    """
    Get products frequently bought together.
    
    Args:
        product_id: ID of the reference product
        limit: Maximum number of products to return
    
    Returns:
        List of complementary products
    """
    # Load all products
    all_products = load_women_products() + load_men_products()
    
    # Find the reference product
    reference = None
    for product in all_products:
        if product.get("id") == product_id:
            reference = product
            break
    
    if not reference:
        return []
    
    ref_category = reference.get("category", "")
    
    # Define complementary categories
    complements = {
        "Lips": ["Eyes", "Face"],
        "Eyes": ["Lips", "Face"],
        "Face": ["Lips", "Eyes", "Skincare"],
        "Skincare": ["Face", "Self-Care"],
        "Self-Care": ["Skincare", "Perfumes"],
        "Perfumes": ["Self-Care"],
        "Hair-Care": ["Self-Care"],
        "Makeup": ["Skincare", "Perfumes"],
        "Beard-Care": ["Grooming", "Perfumes"],
        "Grooming": ["Beard-Care", "Self-Care"],
    }
    
    complement_categories = complements.get(ref_category, [])
    
    # Filter products from complementary categories
    results = []
    for product in all_products:
        if product. get("id") == product_id:
            continue
        if product.get("category", "") in complement_categories:
            results.append(product)
    
    # Sort by rating and return
    results.sort(key=lambda x: x.get("rating", 0), reverse=True)
    
    return results[:limit]