"""
Application constants and configuration values. 
"""

# Brand Information
BRAND_NAME = "WERBEAUTY"
BRAND_TAGLINE = "Discover Your Radiant Beauty"
BRAND_DESCRIPTION = "Luxury cosmetics crafted for those who appreciate elegance and quality."

# Color Palette - Women
COLORS_WOMEN = {
    "primary": "#B76E79",      # Rose Gold
    "secondary": "#F8E7EC",    # Soft Blush Pink
    "accent": "#D8C18F",       # Champagne Gold
}

# Color Palette - Men
COLORS_MEN = {
    "primary": "#0A1A3F",      # Midnight Navy
    "secondary": "#2F3542",    # Graphite Gray
    "accent": "#C0C3C8",       # Silver Metallic
}

# Global Colors
COLORS_GLOBAL = {
    "white": "#FFFFFF",
    "black": "#0F0F0F",
    "gold": "#D4AF37",
}

# Categories
WOMEN_CATEGORIES = [
    "All",
    "Makeup",
    "Perfumes",
    "Self-Care",
    "Hair-Care",
    "Skincare",
    "Lips",
    "Eyes",
    "Face"
]

MEN_CATEGORIES = [
    "All",
    "Beard-Care",
    "Perfumes",
    "Hair-Care",
    "Self-Care",
    "Grooming",
    "Skincare"
]

# Skin Types
SKIN_TYPES = [
    "All Skin Types",
    "Normal",
    "Oily",
    "Dry",
    "Combination",
    "Sensitive"
]

# Hair Types
HAIR_TYPES = [
    "All Hair Types",
    "Straight",
    "Wavy",
    "Curly",
    "Coily",
    "Fine",
    "Thick"
]

# Sort Options
SORT_OPTIONS = {
    "popularity": "Most Popular",
    "price_low": "Price: Low to High",
    "price_high": "Price: High to Low",
    "rating": "Highest Rated",
    "newest": "Newest First"
}

# Promo Codes
PROMO_CODES = {
    "WERBEAUTY10": {"discount": 0.10, "description": "10% off your order"},
    "LUXURY20": {"discount": 0.20, "description": "20% off luxury items"},
    "NEWUSER15": {"discount": 0.15, "description": "15% off for new customers"},
    "FREESHIP": {"discount": 0, "free_shipping": True, "description": "Free shipping"}
}

# Shipping Options
SHIPPING_OPTIONS = {
    "standard": {"name": "Standard Delivery", "price": 5.99, "days": "5-7 business days"},
    "express": {"name": "Express Delivery", "price": 12.99, "days": "2-3 business days"},
    "overnight": {"name": "Overnight Delivery", "price": 24.99, "days": "Next business day"},
    "free": {"name": "Free Shipping", "price": 0, "days": "7-10 business days"}
}

# Tax Rate
TAX_RATE = 0.08  # 8%

# Testimonials
TESTIMONIALS = [
    {
        "name": "Sophie Laurent",
        "text": "WERBEAUTY has completely transformed my skincare routine. The quality is unmatched! ",
        "rating": 5,
        "avatar": "https://randomuser.me/api/portraits/women/1.jpg"
    },
    {
        "name": "Emma Richardson",
        "text": "I've never felt more confident.  These products are worth every penny.",
        "rating": 5,
        "avatar": "https://randomuser.me/api/portraits/women/2.jpg"
    },
    {
        "name": "Michael Chen",
        "text": "Finally, a luxury brand that understands men's grooming.  Exceptional quality.",
        "rating": 5,
        "avatar": "https://randomuser.me/api/portraits/men/1.jpg"
    },
    {
        "name": "Isabella Martinez",
        "text": "The perfumes are divine. I receive compliments everywhere I go! ",
        "rating": 5,
        "avatar": "https://randomuser. me/api/portraits/women/3. jpg"
    },
    {
        "name": "James Wilson",
        "text": "Premium beard care that actually works. My beard has never looked better.",
        "rating": 5,
        "avatar": "https://randomuser.me/api/portraits/men/2.jpg"
    }
]

# Navigation Items
NAV_ITEMS = [
    {"name": "Home", "icon": "🏠", "page": "home"},
    {"name": "Women", "icon": "👩", "page": "women"},
    {"name": "Men", "icon": "👨", "page": "men"},
    {"name": "Recommended", "icon": "🔮", "page": "recommended"},
    {"name": "Favorites", "icon": "❤️", "page": "favorites"},
    {"name": "Cart", "icon": "🛒", "page": "cart"},
]

# Image placeholders (using placeholder services)
PLACEHOLDER_IMAGES = {
    "product": "https://images.unsplash. com/photo-1596462502278-27bfdc403348?w=400&h=400&fit=crop",
    "hero_women": "https://images.unsplash. com/photo-1522335789203-aabd1fc54bc9?w=1200&h=800&fit=crop",
    "hero_men": "https://images.unsplash.com/photo-1621607512214-68297480165e?w=1200&h=800&fit=crop",
    "category_makeup": "https://images.unsplash. com/photo-1512496015851-a90fb38ba796?w=400&h=300&fit=crop",
    "category_perfume": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400&h=300&fit=crop",
    "category_skincare": "https://images.unsplash.com/photo-1570194065650-d99fb4b38b7e?w=400&h=300&fit=crop",
    "category_haircare": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400&h=300&fit=crop",
}