"""
Review and comment management for WERBEAUTY.
Handles product reviews and ratings.
"""

import streamlit as st
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from utils.auth_manager import get_current_user_email, get_current_user


def load_reviews() -> Dict:
    """
    Load all reviews from JSON file.
    
    Returns:
        Dictionary with product IDs as keys and their reviews as values
    """
    reviews_file = "data/reviews.json"
    
    if os.path.exists(reviews_file):
        with open(reviews_file, 'r') as f:
            return json.load(f)
    else:
        os.makedirs("data", exist_ok=True)
        with open(reviews_file, 'w') as f:
            json.dump({}, f)
        return {}


def save_reviews(reviews: Dict) -> None:
    """
    Save reviews to JSON file.
    
    Args:
        reviews: Dictionary of all reviews
    """
    reviews_file = "data/reviews.json"
    os.makedirs("data", exist_ok=True)
    
    with open(reviews_file, 'w') as f:
        json.dump(reviews, f, indent=2)


def add_review(product_id: str, rating: int, comment: str) -> bool:
    """
    Add a review for a product.
    
    Args:
        product_id: ID of the product
        rating: Rating from 1-5
        comment: Review comment
    
    Returns:
        True if review added successfully
    """
    email = get_current_user_email()
    user = get_current_user()
    
    if not email:
        return False
    
    reviews = load_reviews()
    
    # Initialize product reviews if needed
    if product_id not in reviews:
        reviews[product_id] = []
    
    # Check if user already reviewed this product
    for review in reviews[product_id]:
        if review["user_email"] == email:
            # Update existing review
            review["rating"] = rating
            review["comment"] = comment
            review["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_reviews(reviews)
            return True
    
    # Add new review
    review = {
        "user_email": email,
        "user_name": user.get("name", "Anonymous"),
        "rating": rating,
        "comment": comment,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    reviews[product_id].append(review)
    save_reviews(reviews)
    
    return True


def get_product_reviews(product_id: str) -> List[Dict]:
    """
    Get all reviews for a product.
    
    Args:
        product_id: ID of the product
    
    Returns:
        List of reviews for the product
    """
    reviews = load_reviews()
    return reviews.get(product_id, [])


def get_user_reviews() -> List[Dict]:
    """
    Get all reviews by the current user.
    
    Returns:
        List of reviews by the current user
    """
    email = get_current_user_email()
    
    if not email:
        return []
    
    reviews = load_reviews()
    user_reviews = []
    
    for product_id, product_reviews in reviews.items():
        for review in product_reviews:
            if review["user_email"] == email:
                review["product_id"] = product_id
                user_reviews.append(review)
    
    return user_reviews


def delete_review(product_id: str) -> bool:
    """
    Delete a user's review for a product.
    
    Args:
        product_id: ID of the product
    
    Returns:
        True if review deleted successfully
    """
    email = get_current_user_email()
    
    if not email:
        return False
    
    reviews = load_reviews()
    
    if product_id in reviews:
        reviews[product_id] = [r for r in reviews[product_id] if r["user_email"] != email]
        save_reviews(reviews)
        return True
    
    return False


def get_average_rating(product_id: str) -> float:
    """
    Calculate average rating for a product.
    
    Args:
        product_id: ID of the product
    
    Returns:
        Average rating (0-5)
    """
    reviews = get_product_reviews(product_id)
    
    if not reviews:
        return 0.0
    
    total_rating = sum(r["rating"] for r in reviews)
    return round(total_rating / len(reviews), 1)


def get_review_count(product_id: str) -> int:
    """
    Get number of reviews for a product.
    
    Args:
        product_id: ID of the product
    
    Returns:
        Number of reviews
    """
    reviews = get_product_reviews(product_id)
    return len(reviews)
