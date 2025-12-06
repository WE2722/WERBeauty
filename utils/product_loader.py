"""
Product loading utilities for WERBEAUTY.
Loads and filters product data.
"""

import streamlit as st
import json
import os
from typing import Dict, List, Optional


# Default product data (fallback if JSON files not found)
DEFAULT_WOMEN_PRODUCTS = [
    {
        "id": "w001",
        "name": "Velvet Rose Lipstick",
        "price": 42.00,
        "category": "Lips",
        "description": "Long-lasting velvet matte finish in a stunning rose shade.",
        "image": "https://images. unsplash.com/photo-1586495777744-4413f21062fa?w=400&h=400&fit=crop",
        "rating": 4.8,
        "badge": "Bestseller",
        "skin_type": "All Skin Types",
        "ingredients": ["Vitamin E", "Jojoba Oil", "Shea Butter"],
        "popularity": 98
    },
    {
        "id": "w002",
        "name": "Luminous Glow Foundation",
        "price": 68.00,
        "category": "Face",
        "description": "Buildable coverage with a natural luminous finish.",
        "image": "https://images.unsplash. com/photo-1631214503851-50b2c3f498b8?w=400&h=400&fit=crop",
        "rating": 4.9,
        "badge": "New",
        "skin_type": "All Skin Types",
        "ingredients": ["Hyaluronic Acid", "Vitamin C", "SPF 30"],
        "popularity": 95
    },
    {
        "id": "w003",
        "name": "Midnight Orchid Perfume",
        "price": 128.00,
        "category": "Perfumes",
        "description": "An enchanting floral fragrance with notes of orchid and vanilla.",
        "image": "https://images.unsplash. com/photo-1541643600914-78b084683601?w=400&h=400&fit=crop",
        "rating": 4.7,
        "badge": "Luxury",
        "skin_type": "All Skin Types",
        "ingredients": ["Orchid Extract", "Vanilla", "Musk"],
        "popularity": 92
    },
    {
        "id": "w004",
        "name": "Silk Repair Hair Serum",
        "price": 56.00,
        "category": "Hair-Care",
        "description": "Intensive repair serum for silky, frizz-free hair.",
        "image": "https://images.unsplash. com/photo-1527799820374-dcf8d9d4a388?w=400&h=400&fit=crop",
        "rating": 4.6,
        "badge": "",
        "hair_type": "All Hair Types",
        "ingredients": ["Argan Oil", "Keratin", "Silk Proteins"],
        "popularity": 88
    },
    {
        "id": "w005",
        "name": "Radiance Eye Cream",
        "price": 78.00,
        "category": "Skincare",
        "description": "Reduces dark circles and fine lines around the eyes.",
        "image": "https://images.unsplash.com/photo-1570194065650-d99fb4b38b7e?w=400&h=400&fit=crop",
        "rating": 4.8,
        "badge": "Bestseller",
        "skin_type": "All Skin Types",
        "ingredients": ["Retinol", "Caffeine", "Peptides"],
        "popularity": 94
    },
    {
        "id": "w006",
        "name": "Golden Shimmer Eyeshadow Palette",
        "price": 62.00,
        "category": "Eyes",
        "description": "12 stunning shades from matte to shimmer for endless looks.",
        "image": "https://images.unsplash. com/photo-1512496015851-a90fb38ba796?w=400&h=400&fit=crop",
        "rating": 4.9,
        "badge": "Popular",
        "skin_type": "All Skin Types",
        "ingredients": ["Mica", "Vitamin E", "Jojoba Oil"],
        "popularity": 96
    },
    {
        "id": "w007",
        "name": "Hydra Boost Moisturizer",
        "price": 54.00,
        "category": "Skincare",
        "description": "48-hour hydration with lightweight, non-greasy formula.",
        "image": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd?w=400&h=400&fit=crop",
        "rating": 4.7,
        "badge": "",
        "skin_type": "Dry",
        "ingredients": ["Hyaluronic Acid", "Ceramides", "Aloe Vera"],
        "popularity": 89
    },
    {
        "id": "w008",
        "name": "Cherry Blossom Body Lotion",
        "price": 38.00,
        "category": "Self-Care",
        "description": "Luxurious body lotion with delicate cherry blossom scent.",
        "image": "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400&h=400&fit=crop",
        "rating": 4.5,
        "badge": "",
        "skin_type": "All Skin Types",
        "ingredients": ["Cherry Blossom Extract", "Shea Butter", "Vitamin E"],
        "popularity": 85
    },
    {
        "id": "w009",
        "name": "Volume Boost Mascara",
        "price": 34.00,
        "category": "Eyes",
        "description": "Dramatic volume and length that lasts all day.",
        "image": "https://images.unsplash.com/photo-1631214540553-ff044a3ff1d4?w=400&h=400&fit=crop",
        "rating": 4.6,
        "badge": "New",
        "skin_type": "All Skin Types",
        "ingredients": ["Bamboo Extract", "Keratin", "Biotin"],
        "popularity": 91
    },
    {
        "id": "w010",
        "name": "Rose Petal Face Mist",
        "price": 28.00,
        "category": "Skincare",
        "description": "Refreshing facial mist with pure rose water.",
        "image": "https://images.unsplash. com/photo-1596462502278-27bfdc403348?w=400&h=400&fit=crop",
        "rating": 4.4,
        "badge": "",
        "skin_type": "All Skin Types",
        "ingredients": ["Rose Water", "Glycerin", "Aloe Vera"],
        "popularity": 82
    },
    {
        "id": "w011",
        "name": "Champagne Dreams Highlighter",
        "price": 44.00,
        "category": "Face",
        "description": "Stunning champagne glow for a radiant finish.",
        "image": "https://images.unsplash. com/photo-1599733589046-10c672de5c39?w=400&h=400&fit=crop",
        "rating": 4.8,
        "badge": "Trending",
        "skin_type": "All Skin Types",
        "ingredients": ["Mica", "Diamond Powder", "Vitamin E"],
        "popularity": 93
    },
    {
        "id": "w012",
        "name": "Sunset Blush Palette",
        "price": 48.00,
        "category": "Face",
        "description": "4 beautiful blush shades inspired by golden sunsets.",
        "image": "https://images.unsplash.com/photo-1503236823255-94609f598e71?w=400&h=400&fit=crop",
        "rating": 4.7,
        "badge": "",
        "skin_type": "All Skin Types",
        "ingredients": ["Silk Powder", "Rose Hip Oil", "Vitamin C"],
        "popularity": 87
    }
]

DEFAULT_MEN_PRODUCTS = [
    {
        "id": "m001",
        "name": "Gentleman's Beard Oil",
        "price": 48.00,
        "category": "Beard-Care",
        "description": "Premium beard oil for a soft, healthy, and styled beard.",
        "image": "https://images.unsplash.com/photo-1621605815971-fbc98d665033?w=400&h=400&fit=crop",
        "rating": 4.9,
        "badge": "Bestseller",
        "skin_type": "All Skin Types",
        "ingredients": ["Argan Oil", "Jojoba Oil", "Vitamin E"],
        "popularity": 97
    },
    {
        "id": "m002",
        "name": "Noir Intense Cologne",
        "price": 145.00,
        "category": "Perfumes",
        "description": "Bold and sophisticated fragrance with woody notes.",
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=400&h=400&fit=crop",
        "rating": 4.8,
        "badge": "Luxury",
        "skin_type": "All Skin Types",
        "ingredients": ["Bergamot", "Cedar", "Leather"],
        "popularity": 95
    },
    {
        "id": "m003",
        "name": "Precision Beard Trimmer Set",
        "price": 89.00,
        "category": "Grooming",
        "description": "Professional-grade trimmer with multiple attachments.",
        "image": "https://images.unsplash.com/photo-1621607512214-68297480165e?w=400&h=400&fit=crop",
        "rating": 4.7,
        "badge": "Popular",
        "skin_type": "All Skin Types",
        "ingredients": [],
        "popularity": 92
    },
    {
        "id": "m004",
        "name": "Charcoal Deep Cleanse Face Wash",
        "price": 32.00,
        "category": "Skincare",
        "description": "Deep cleansing formula with activated charcoal.",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop",
        "rating": 4.6,
        "badge": "",
        "skin_type": "Oily",
        "ingredients": ["Activated Charcoal", "Tea Tree Oil", "Salicylic Acid"],
        "popularity": 88
    },
    {
        "id": "m005",
        "name": "Sculpting Hair Pomade",
        "price": 28.00,
        "category": "Hair-Care",
        "description": "Strong hold pomade with natural matte finish.",
        "image": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=400&h=400&fit=crop",
        "rating": 4.5,
        "badge": "",
        "hair_type": "All Hair Types",
        "ingredients": ["Beeswax", "Coconut Oil", "Kaolin Clay"],
        "popularity": 86
    },
    {
        "id": "m006",
        "name": "Beard Balm Supreme",
        "price": 38.00,
        "category": "Beard-Care",
        "description": "Nourishing balm for beard styling and conditioning.",
        "image": "https://images.unsplash. com/photo-1621605815971-fbc98d665033?w=400&h=400&fit=crop",
        "rating": 4.7,
        "badge": "New",
        "skin_type": "All Skin Types",
        "ingredients": ["Shea Butter", "Beeswax", "Tea Tree Oil"],
        "popularity": 90
    },
    {
        "id": "m007",
        "name": "Ocean Breeze Body Wash",
        "price": 24.00,
        "category": "Self-Care",
        "description": "Refreshing body wash with ocean mineral complex.",
        "image": "https://images.unsplash. com/photo-1608248597279-f99d160bfcbc?w=400&h=400&fit=crop",
        "rating": 4.4,
        "badge": "",
        "skin_type": "All Skin Types",
        "ingredients": ["Sea Salt", "Algae Extract", "Menthol"],
        "popularity": 83
    },
    {
        "id": "m008",
        "name": "Anti-Aging Eye Gel",
        "price": 58.00,
        "category": "Skincare",
        "description": "Targeted treatment for dark circles and puffiness.",
        "image": "https://images.unsplash.com/photo-1570194065650-d99fb4b38b7e?w=400&h=400&fit=crop",
        "rating": 4.6,
        "badge": "",
        "skin_type": "All Skin Types",
        "ingredients": ["Caffeine", "Peptides", "Vitamin K"],
        "popularity": 85
    },
    {
        "id": "m009",
        "name": "Cedar & Sage Deodorant",
        "price": 22.00,
        "category": "Self-Care",
        "description": "Natural aluminum-free deodorant with 48-hour protection.",
        "image": "https://images.unsplash. com/photo-1596462502278-27bfdc403348?w=400&h=400&fit=crop",
        "rating": 4.5,
        "badge": "",
        "skin_type": "Sensitive",
        "ingredients": ["Baking Soda", "Cedar Oil", "Sage Extract"],
        "popularity": 84
    },
    {
        "id": "m010",
        "name": "Thickening Hair Shampoo",
        "price": 36.00,
        "category": "Hair-Care",
        "description": "Volumizing shampoo for thicker, fuller-looking hair.",
        "image": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400&h=400&fit=crop",
        "rating": 4.7,
        "badge": "Trending",
        "skin_type": "All Skin Types",
        "hair_type": "Fine",
        "ingredients": ["Biotin", "Caffeine", "Saw Palmetto"],
        "popularity": 91
    },
    {
        "id": "m011",
        "name": "Executive Shave Cream",
        "price": 34.00,
        "category": "Grooming",
        "description": "Rich lathering cream for the smoothest shave.",
        "image": "https://images.unsplash.com/photo-1621607512214-68297480165e?w=400&h=400&fit=crop",
        "rating": 4.8,
        "badge": "",
        "skin_type": "Sensitive",
        "ingredients": ["Aloe Vera", "Coconut Oil", "Vitamin E"],
        "popularity": 89
    },
    {
        "id": "m012",
        "name": "Midnight Oud Parfum",
        "price": 175.00,
        "category": "Perfumes",
        "description": "Exclusive oud-based fragrance for the distinguished gentleman.",
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=400&h=400&fit=crop",
        "rating": 4.9,
        "badge": "Exclusive",
        "skin_type": "All Skin Types",
        "ingredients": ["Oud", "Amber", "Sandalwood"],
        "popularity": 94
    }
]


@st.cache_data(ttl=3600)
def load_women_products() -> List[Dict]:
    """
    Load women's products from JSON file or return defaults. 
    
    Returns:
        List of women's product dictionaries
    """
    try:
        json_path = os.path.join(os.path.dirname(__file__), "..", "data", "women_products.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading women's products: {e}")
    
    return DEFAULT_WOMEN_PRODUCTS


@st.cache_data(ttl=3600)
def load_men_products() -> List[Dict]:
    """
    Load men's products from JSON file or return defaults.
    
    Returns:
        List of men's product dictionaries
    """
    try:
        json_path = os.path.join(os.path.dirname(__file__), "..", "data", "men_products.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading men's products: {e}")
    
    return DEFAULT_MEN_PRODUCTS


def get_product_by_id(product_id: str) -> Optional[Dict]:
    """
    Get a product by its ID. 
    
    Args:
        product_id: The product ID to find
    
    Returns:
        Product dictionary or None if not found
    """
    all_products = load_women_products() + load_men_products()
    
    for product in all_products:
        if product.get("id") == product_id:
            return product
    
    return None


def filter_products(products: List[Dict], filters: Dict) -> List[Dict]:
    """
    Filter products based on given criteria.
    
    Args:
        products: List of products to filter
        filters: Filter criteria dictionary
    
    Returns:
        Filtered list of products
    """
    filtered = products.copy()
    
    # Filter by category
    category = filters.get("category", "All")
    if category and category != "All":
        filtered = [p for p in filtered if p.get("category", ""). lower() == category. lower() or 
                   category. lower() in p.get("category", "").lower()]
    
    # Filter by price range
    price_range = filters.get("price_range", (0, 500))
    if price_range:
        min_price, max_price = price_range
        filtered = [p for p in filtered if min_price <= p.get("price", 0) <= max_price]
    
    # Filter by skin type
    skin_type = filters.get("skin_type", "All Skin Types")
    if skin_type and skin_type != "All Skin Types":
        filtered = [p for p in filtered if 
                   p.get("skin_type", "All Skin Types") == skin_type or 
                   p.get("skin_type", "All Skin Types") == "All Skin Types"]
    
    # Filter by hair type
    hair_type = filters.get("hair_type", "All Hair Types")
    if hair_type and hair_type != "All Hair Types":
        filtered = [p for p in filtered if 
                   p.get("hair_type", "All Hair Types") == hair_type or 
                   p.get("hair_type", "All Hair Types") == "All Hair Types"]
    
    # Sort products
    sort_by = filters.get("sort_by", "popularity")
    if sort_by == "price_low":
        filtered.sort(key=lambda x: x.get("price", 0))
    elif sort_by == "price_high":
        filtered.sort(key=lambda x: x.get("price", 0), reverse=True)
    elif sort_by == "rating":
        filtered. sort(key=lambda x: x.get("rating", 0), reverse=True)
    elif sort_by == "popularity":
        filtered.sort(key=lambda x: x.get("popularity", 0), reverse=True)
    elif sort_by == "newest":
        filtered. sort(key=lambda x: x.get("id", ""), reverse=True)
    
    return filtered


def search_products(products: List[Dict], query: str) -> List[Dict]:
    """
    Search products by name, description, or category.
    
    Args:
        products: List of products to search
        query: Search query string
    
    Returns:
        List of matching products with highlighted matches
    """
    if not query or not query.strip():
        return products
    
    query = query.lower(). strip()
    results = []
    
    for product in products:
        name = product.get("name", ""). lower()
        description = product.get("description", "").lower()
        category = product.get("category", "").lower()
        
        if query in name or query in description or query in category:
            # Create a copy with match info
            result = product.copy()
            result["_match_in_name"] = query in name
            result["_match_in_description"] = query in description
            result["_match_in_category"] = query in category
            results.append(result)
    
    return results