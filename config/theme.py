"""
Theme configuration and CSS injection for WERBEAUTY. 
Defines all styling, animations, and visual elements. 
"""

import streamlit as st


def initialize_session_state():
    """
    Initialize all session state variables with default values.
    """
    defaults = {
        "gender": None,
        "cart": [],
        "favorites": [],
        "ai_open": False,
        "view_history": [],
        "current_page": "home",
        "onboarding_complete": False,
        "search_query": "",
        "filters": {
            "price_range": (0, 500),
            "category": "All",
            "sort_by": "popularity"
        },
        "promo_code": "",
        "promo_applied": False,
        "checkout_data": {}
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def apply_custom_theme():
    """
    Apply custom CSS theme to the application. 
    Includes all animations, glassmorphism effects, and responsive styles.
    """
    
    # Determine color scheme based on gender preference
    gender = st.session_state.get("gender", "women")
    
    if gender == "men":
        primary_color = "#0A1A3F"  # Midnight Navy
        secondary_color = "#2F3542"  # Graphite Gray
        accent_color = "#C0C3C8"  # Silver Metallic
        gradient_start = "#0A1A3F"
        gradient_end = "#1a2a4f"
    else:
        primary_color = "#B76E79"  # Rose Gold
        secondary_color = "#F8E7EC"  # Soft Blush Pink
        accent_color = "#D8C18F"  # Champagne Gold
        gradient_start = "#B76E79"
        gradient_end = "#d4a5ad"
    
    css = f"""
    <style>
        /* ==================== IMPORTS ==================== */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* ==================== ROOT VARIABLES ==================== */
        :root {{
            --primary-color: {primary_color};
            --secondary-color: {secondary_color};
            --accent-color: {accent_color};
            --gradient-start: {gradient_start};
            --gradient-end: {gradient_end};
            --luxury-gold: #D4AF37;
            --pure-white: #FFFFFF;
            --onyx-black: #0F0F0F;
            --rose-gold: #B76E79;
            --midnight-navy: #0A1A3F;
            --glass-bg: rgba(255, 255, 255, 0.15);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-light: 0 8px 32px rgba(0, 0, 0, 0.1);
            --shadow-medium: 0 16px 48px rgba(0, 0, 0, 0.15);
            --shadow-heavy: 0 24px 64px rgba(0, 0, 0, 0.2);
            --border-radius-sm: 12px;
            --border-radius-md: 18px;
            --border-radius-lg: 24px;
            --transition-fast: 0.2s ease;
            --transition-medium: 0.3s ease;
            --transition-slow: 0.5s ease;
        }}
        
        /* ==================== GLOBAL STYLES ==================== */
        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            scroll-behavior: smooth;
        }}
        
        . stApp {{
            background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Playfair Display', serif ! important;
            font-weight: 600;
        }}
        
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* ==================== GLASSMORPHISM COMPONENTS ==================== */
        .glass-panel {{
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius-lg);
            box-shadow: var(--shadow-light);
            padding: 2rem;
            transition: all var(--transition-medium);
        }}
        
        .glass-panel:hover {{
            box-shadow: var(--shadow-medium);
            transform: translateY(-2px);
        }}
        
        /* ==================== NAVIGATION BAR ==================== */
        .navbar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
            transition: all var(--transition-medium);
        }}
        
        .navbar.scrolled {{
            background: rgba(255, 255, 255, 0.98);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.12);
        }}
        
        .nav-logo {{
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }}
        
        .nav-links {{
            display: flex;
            gap: 2rem;
            align-items: center;
        }}
        
        .nav-link {{
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--onyx-black);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: var(--border-radius-sm);
            transition: all var(--transition-fast);
            position: relative;
        }}
        
        .nav-link:hover {{
            color: var(--primary-color);
            background: rgba(183, 110, 121, 0.1);
        }}
        
        .nav-link::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 2px;
            background: var(--primary-color);
            transition: all var(--transition-medium);
            transform: translateX(-50%);
        }}
        
        .nav-link:hover::after {{
            width: 80%;
        }}
        
        .nav-badge {{
            position: absolute;
            top: -5px;
            right: -5px;
            background: var(--luxury-gold);
            color: white;
            font-size: 0.7rem;
            font-weight: 600;
            padding: 2px 6px;
            border-radius: 50%;
            min-width: 18px;
            text-align: center;
        }}
        
        /* ==================== BUTTONS ==================== */
        .stButton > button {{
            font-family: 'Inter', sans-serif ! important;
            font-weight: 500;
            border-radius: var(--border-radius-md) !important;
            padding: 0.75rem 2rem !important;
            transition: all var(--transition-medium) !important;
            border: none ! important;
            box-shadow: var(--shadow-light);
        }}
        
        .btn-primary {{
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end)) !important;
            color: white !important;
        }}
        
        .btn-primary:hover {{
            transform: translateY(-3px) !important;
            box-shadow: var(--shadow-medium) !important;
        }}
        
        .btn-secondary {{
            background: transparent !important;
            border: 2px solid var(--primary-color) !important;
            color: var(--primary-color) !important;
        }}
        
        .btn-secondary:hover {{
            background: var(--primary-color) !important;
            color: white !important;
        }}
        
        .btn-luxury {{
            background: linear-gradient(135deg, #D4AF37, #f5d76e) !important;
            color: var(--onyx-black) ! important;
            font-weight: 600 !important;
        }}
        
        .btn-luxury:hover {{
            background: linear-gradient(135deg, #c9a430, #e8ca5c) !important;
            transform: scale(1.02) translateY(-2px) !important;
        }}
        
        /* ==================== PRODUCT CARDS ==================== */
        .product-card {{
            background: white;
            border-radius: var(--border-radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-light);
            transition: all var(--transition-medium);
            cursor: pointer;
            position: relative;
        }}
        
        .product-card:hover {{
            transform: translateY(-10px);
            box-shadow: var(--shadow-heavy);
        }}
        
        .product-card-image {{
            width: 100%;
            height: 280px;
            object-fit: cover;
            transition: transform var(--transition-slow);
        }}
        
        .product-card:hover . product-card-image {{
            transform: scale(1.08);
        }}
        
        .product-card-content {{
            padding: 1.5rem;
        }}
        
        .product-card-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--onyx-black);
            margin-bottom: 0.5rem;
        }}
        
        .product-card-price {{
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--primary-color);
        }}
        
        .product-card-badge {{
            position: absolute;
            top: 1rem;
            left: 1rem;
            background: var(--luxury-gold);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: var(--border-radius-sm);
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }}
        
        . product-card-favorite {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-light);
            cursor: pointer;
            transition: all var(--transition-fast);
        }}
        
        .product-card-favorite:hover {{
            transform: scale(1. 1);
            background: #ffe4e8;
        }}
        
        .product-card-actions {{
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
        }}
        
        /* ==================== HERO SECTION ==================== */
        .hero-section {{
            position: relative;
            min-height: 85vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
            margin: -1rem -1rem 2rem -1rem;
            padding: 4rem 2rem;
        }}
        
        .hero-content {{
            text-align: center;
            z-index: 10;
            animation: fadeInUp 1s ease-out;
        }}
        
        .hero-title {{
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            font-weight: 700;
            color: white;
            margin-bottom: 1. 5rem;
            text-shadow: 2px 4px 20px rgba(0, 0, 0, 0.2);
        }}
        
        .hero-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 2rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .hero-particles {{
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }}
        
        .particle {{
            position: absolute;
            width: 10px;
            height: 10px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            animation: float 15s infinite;
        }}
        
        /* ==================== ANIMATIONS ==================== */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(40px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-40px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes fadeInLeft {{
            from {{
                opacity: 0;
                transform: translateX(-40px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}
        
        @keyframes fadeInRight {{
            from {{
                opacity: 0;
                transform: translateX(40px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}
        
        @keyframes scaleIn {{
            from {{
                opacity: 0;
                transform: scale(0.9);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        @keyframes float {{
            0%, 100% {{
                transform: translateY(0) rotate(0deg);
                opacity: 0;
            }}
            10% {{
                opacity: 1;
            }}
            90% {{
                opacity: 1;
            }}
            100% {{
                transform: translateY(-100vh) rotate(720deg);
                opacity: 0;
            }}
        }}
        
        @keyframes shimmer {{
            0% {{
                background-position: -200% 0;
            }}
            100% {{
                background-position: 200% 0;
            }}
        }}
        
        @keyframes pulse {{
            0%, 100% {{
                transform: scale(1);
            }}
            50% {{
                transform: scale(1.05);
            }}
        }}
        
        @keyframes glow {{
            0%, 100% {{
                box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
            }}
            50% {{
                box-shadow: 0 0 40px rgba(212, 175, 55, 0.8);
            }}
        }}
        
        @keyframes typewriter {{
            from {{ width: 0; }}
            to {{ width: 100%; }}
        }}
        
        @keyframes blink {{
            0%, 50% {{ border-color: transparent; }}
            51%, 100% {{ border-color: var(--luxury-gold); }}
        }}
        
        @keyframes slideInFromLeft {{
            from {{
                transform: translateX(-100%);
                opacity: 0;
            }}
            to {{
                transform: translateX(0);
                opacity: 1;
            }}
        }}
        
        @keyframes slideInFromRight {{
            from {{
                transform: translateX(100%);
                opacity: 0;
            }}
            to {{
                transform: translateX(0);
                opacity: 1;
            }}
        }}
        
        @keyframes bounceIn {{
            0% {{
                opacity: 0;
                transform: scale(0.3);
            }}
            50% {{
                transform: scale(1. 05);
            }}
            70% {{
                transform: scale(0.9);
            }}
            100% {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        @keyframes flipIn {{
            from {{
                transform: perspective(400px) rotateY(90deg);
                opacity: 0;
            }}
            to {{
                transform: perspective(400px) rotateY(0);
                opacity: 1;
            }}
        }}
        
        /* Animation Classes */
        .animate-fadeInUp {{
            animation: fadeInUp 0.6s ease-out forwards;
        }}
        
        .animate-fadeInDown {{
            animation: fadeInDown 0.6s ease-out forwards;
        }}
        
        .animate-fadeInLeft {{
            animation: fadeInLeft 0.6s ease-out forwards;
        }}
        
        .animate-fadeInRight {{
            animation: fadeInRight 0.6s ease-out forwards;
        }}
        
        .animate-scaleIn {{
            animation: scaleIn 0.5s ease-out forwards;
        }}
        
        .animate-bounceIn {{
            animation: bounceIn 0.8s ease-out forwards;
        }}
        
        .animate-pulse {{
            animation: pulse 2s ease-in-out infinite;
        }}
        
        .animate-glow {{
            animation: glow 2s ease-in-out infinite;
        }}
        
        .delay-1 {{ animation-delay: 0.1s; }}
        .delay-2 {{ animation-delay: 0.2s; }}
        .delay-3 {{ animation-delay: 0.3s; }}
        .delay-4 {{ animation-delay: 0.4s; }}
        .delay-5 {{ animation-delay: 0.5s; }}
        
        /* ==================== LOADING SKELETON ==================== */
        .skeleton {{
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
            border-radius: var(--border-radius-md);
        }}
        
        .skeleton-card {{
            height: 350px;
            margin-bottom: 1rem;
        }}
        
        .skeleton-text {{
            height: 20px;
            margin-bottom: 0.5rem;
        }}
        
        .skeleton-title {{
            height: 30px;
            width: 70%;
            margin-bottom: 1rem;
        }}
        
        /* ==================== FILTERS PANEL ==================== */
        .filters-panel {{
            background: white;
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            box-shadow: var(--shadow-light);
            position: sticky;
            top: 100px;
        }}
        
        .filter-section {{
            margin-bottom: 1.5rem;
            padding-bottom: 1. 5rem;
            border-bottom: 1px solid #eee;
        }}
        
        . filter-section:last-child {{
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }}
        
        . filter-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1rem;
            font-weight: 600;
            color: var(--onyx-black);
            margin-bottom: 1rem;
        }}
        
        /* ==================== CAROUSEL ==================== */
        .carousel-container {{
            position: relative;
            overflow: hidden;
            padding: 2rem 0;
        }}
        
        . carousel-track {{
            display: flex;
            gap: 1. 5rem;
            transition: transform var(--transition-slow);
        }}
        
        .carousel-item {{
            flex: 0 0 auto;
            width: 280px;
        }}
        
        .carousel-nav {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-medium);
            cursor: pointer;
            transition: all var(--transition-fast);
            z-index: 10;
        }}
        
        . carousel-nav:hover {{
            transform: translateY(-50%) scale(1. 1);
            box-shadow: var(--shadow-heavy);
        }}
        
        .carousel-nav-prev {{ left: 1rem; }}
        .carousel-nav-next {{ right: 1rem; }}
        
        /* ==================== TESTIMONIALS ==================== */
        .testimonial-card {{
            background: white;
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            box-shadow: var(--shadow-light);
            text-align: center;
            transition: all var(--transition-medium);
        }}
        
        . testimonial-card:hover {{
            transform: translateY(-5px);
            box-shadow: var(--shadow-medium);
        }}
        
        .testimonial-avatar {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 1rem;
            border: 3px solid var(--luxury-gold);
        }}
        
        .testimonial-text {{
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #555;
            font-style: italic;
            line-height: 1.8;
            margin-bottom: 1rem;
        }}
        
        . testimonial-author {{
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--onyx-black);
        }}
        
        . testimonial-rating {{
            color: var(--luxury-gold);
            font-size: 1.2rem;
            margin-top: 0.5rem;
        }}
        
        /* ==================== CART STYLES ==================== */
        .cart-item {{
            display: flex;
            gap: 1. 5rem;
            padding: 1. 5rem;
            background: white;
            border-radius: var(--border-radius-lg);
            box-shadow: var(--shadow-light);
            margin-bottom: 1rem;
            transition: all var(--transition-medium);
        }}
        
        .cart-item:hover {{
            box-shadow: var(--shadow-medium);
        }}
        
        .cart-item-image {{
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: var(--border-radius-md);
        }}
        
        .cart-item-details {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        
        . cart-item-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            font-weight: 600;
        }}
        
        .cart-item-price {{
            font-family: 'Inter', sans-serif;
            font-size: 1. 3rem;
            font-weight: 700;
            color: var(--primary-color);
        }}
        
        .quantity-selector {{
            display: flex;
            align-items: center;
            gap: 1rem;
            background: #f5f5f5;
            padding: 0.5rem 1rem;
            border-radius: var(--border-radius-md);
        }}
        
        .quantity-btn {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            border: none;
            background: var(--primary-color);
            color: white;
            cursor: pointer;
            transition: all var(--transition-fast);
        }}
        
        .quantity-btn:hover {{
            transform: scale(1. 1);
        }}
        
        /* ==================== PAYMENT FORM ==================== */
        .payment-form {{
            background: white;
            border-radius: var(--border-radius-lg);
            padding: 2. 5rem;
            box-shadow: var(--shadow-medium);
        }}
        
        .credit-card {{
            width: 100%;
            max-width: 400px;
            aspect-ratio: 1. 586;
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            color: white;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-heavy);
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }}
        
        .credit-card. flipped {{
            transform: rotateY(180deg);
        }}
        
        .credit-card-front,
        .credit-card-back {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            padding: 2rem;
            backface-visibility: hidden;
        }}
        
        .credit-card-back {{
            transform: rotateY(180deg);
            background: linear-gradient(135deg, var(--gradient-end), var(--gradient-start));
        }}
        
        .card-chip {{
            width: 50px;
            height: 40px;
            background: linear-gradient(135deg, #d4af37, #f5d76e);
            border-radius: 8px;
            margin-bottom: 1. 5rem;
        }}
        
        .card-number {{
            font-family: 'Inter', monospace;
            font-size: 1.4rem;
            letter-spacing: 4px;
            margin-bottom: 1. 5rem;
        }}
        
        .card-info {{
            display: flex;
            justify-content: space-between;
        }}
        
        .card-label {{
            font-size: 0.7rem;
            text-transform: uppercase;
            opacity: 0.8;
            margin-bottom: 0.3rem;
        }}
        
        . card-value {{
            font-size: 1rem;
            font-weight: 500;
        }}
        
        /* ==================== ONBOARDING ==================== */
        .onboarding-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.9);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
        }}
        
        .onboarding-content {{
            text-align: center;
            padding: 3rem;
            animation: scaleIn 0.5s ease-out;
        }}
        
        .onboarding-title {{
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            color: white;
            margin-bottom: 1rem;
        }}
        
        .onboarding-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 3rem;
        }}
        
        .gender-options {{
            display: flex;
            gap: 3rem;
            justify-content: center;
        }}
        
        .gender-option {{
            padding: 2rem 4rem;
            border-radius: var(--border-radius-lg);
            cursor: pointer;
            transition: all var(--transition-medium);
            text-align: center;
        }}
        
        .gender-option-women {{
            background: linear-gradient(135deg, #B76E79, #d4a5ad);
        }}
        
        .gender-option-men {{
            background: linear-gradient(135deg, #0A1A3F, #1a2a4f);
        }}
        
        .gender-option:hover {{
            transform: scale(1.05) translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }}
        
        .gender-icon {{
            font-size: 4rem;
            margin-bottom: 1rem;
        }}
        
        . gender-label {{
            font-family: 'Playfair Display', serif;
            font-size: 1. 5rem;
            color: white;
            font-weight: 600;
        }}
        
        /* ==================== AI ASSISTANT ==================== */
        .ai-toggle {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 9998;
        }}
        
        .ai-toggle-btn {{
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--luxury-gold), #f5d76e);
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-heavy);
            transition: all var(--transition-medium);
            animation: pulse 2s infinite;
        }}
        
        .ai-toggle-btn:hover {{
            transform: scale(1. 1);
        }}
        
        .ai-chat-window {{
            position: fixed;
            bottom: 6rem;
            right: 2rem;
            width: 380px;
            height: 500px;
            background: white;
            border-radius: var(--border-radius-lg);
            box-shadow: var(--shadow-heavy);
            overflow: hidden;
            z-index: 9997;
            animation: slideInFromRight 0.3s ease-out;
        }}
        
        .ai-chat-header {{
            background: linear-gradient(135deg, var(--luxury-gold), #f5d76e);
            padding: 1rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .ai-chat-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--onyx-black);
        }}
        
        .ai-chat-body {{
            height: calc(100% - 60px);
            overflow: hidden;
        }}
        
        /* ==================== FOOTER ==================== */
        .footer {{
            background: linear-gradient(135deg, #B76E79, #d4a5ad);
            color: white;
            padding: 4rem 2rem 2rem;
            margin-top: 4rem;
        }}
        
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 3rem;
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .footer-section-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            color: white;
            font-weight: 700;
        }}
        
        .footer-link {{
            display: block;
            color: white;
            text-decoration: none;
            margin-bottom: 0.8rem;
            transition: all var(--transition-fast);
            opacity: 0.9;
        }}
        
        .footer-link:hover {{
            color: #2C1810;
            transform: translateX(5px);
            opacity: 1;
        }}
        
        .footer-bottom {{
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.3);
            color: white;
        }}
        
        .footer-logo {{
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            font-weight: 700;
            color: white;
            margin-bottom: 1rem;
        }}
        
        /* ==================== RESPONSIVE DESIGN ==================== */
        @media (max-width: 1200px) {{
            .footer-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        
        @media (max-width: 768px) {{
            .hero-title {{
                font-size: 2.5rem;
            }}
            
            .hero-subtitle {{
                font-size: 1rem;
            }}
            
            .gender-options {{
                flex-direction: column;
                gap: 1.5rem;
            }}
            
            .gender-option {{
                padding: 1.5rem 3rem;
            }}
            
            .footer-grid {{
                grid-template-columns: 1fr;
            }}
            
            .ai-chat-window {{
                width: calc(100% - 2rem);
                right: 1rem;
                left: 1rem;
            }}
            
            .cart-item {{
                flex-direction: column;
            }}
            
            .cart-item-image {{
                width: 100%;
                height: 200px;
            }}
        }}
        
        @media (max-width: 480px) {{
            .hero-title {{
                font-size: 2rem;
            }}
            
            . nav-links {{
                gap: 1rem;
            }}
            
            .nav-link {{
                font-size: 0.85rem;
                padding: 0.4rem 0.8rem;
            }}
        }}
        
        /* ==================== SECTION STYLES ==================== */
        .section {{
            padding: 4rem 0;
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .section-header {{
            text-align: center;
            margin-bottom: 3rem;
        }}
        
        .section-title {{
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            font-weight: 600;
            color: var(--onyx-black);
            margin-bottom: 1rem;
        }}
        
        .section-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            color: #666;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .section-divider {{
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            margin: 1.5rem auto 0;
            border-radius: 2px;
        }}
        
        /* ==================== NEWSLETTER ==================== */
        .newsletter-section {{
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
            padding: 4rem 2rem;
            border-radius: var(--border-radius-lg);
            text-align: center;
            margin: 4rem 0;
        }}
        
        .newsletter-title {{
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: white;
            margin-bottom: 1rem;
        }}
        
        .newsletter-subtitle {{
            font-family: 'Inter', sans-serif;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 2rem;
        }}
        
        .newsletter-form {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            max-width: 500px;
            margin: 0 auto;
        }}
        
        .newsletter-input {{
            flex: 1;
            padding: 1rem 1.5rem;
            border: none;
            border-radius: var(--border-radius-md);
            font-size: 1rem;
            outline: none;
        }}
        
        .newsletter-btn {{
            padding: 1rem 2rem;
            background: var(--luxury-gold);
            color: var(--onyx-black);
            border: none;
            border-radius: var(--border-radius-md);
            font-weight: 600;
            cursor: pointer;
            transition: all var(--transition-medium);
        }}
        
        .newsletter-btn:hover {{
            transform: scale(1.05);
        }}
        
        /* ==================== STAR RATING ==================== */
        .star-rating {{
            color: var(--luxury-gold);
            font-size: 1rem;
        }}
        
        .star-rating . star-empty {{
            color: #ddd;
        }}
        
        /* ==================== PROMO CODE ==================== */
        .promo-section {{
            background: linear-gradient(135deg, #f8f8f8, #fff);
            padding: 1.5rem;
            border-radius: var(--border-radius-md);
            border: 2px dashed var(--luxury-gold);
            margin-bottom: 2rem;
        }}
        
        .promo-applied {{
            background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
            border-color: #4caf50;
        }}
        
        /* ==================== ORDER SUMMARY ==================== */
        .order-summary {{
            background: white;
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            box-shadow: var(--shadow-medium);
            position: sticky;
            top: 100px;
        }}
        
        .order-summary-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #eee;
        }}
        
        .order-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            font-size: 1rem;
        }}
        
        .order-row.total {{
            font-weight: 700;
            font-size: 1.3rem;
            padding-top: 1rem;
            border-top: 2px solid #eee;
            margin-top: 1rem;
        }}
        
        /* ==================== QUICK VIEW MODAL ==================== */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            animation: fadeIn 0.3s ease-out;
        }}
        
        .modal-content {{
            background: white;
            border-radius: var(--border-radius-lg);
            max-width: 900px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            animation: scaleIn 0.3s ease-out;
        }}
        
        .modal-close {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: white;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            box-shadow: var(--shadow-light);
            transition: all var(--transition-fast);
        }}
        
        .modal-close:hover {{
            transform: scale(1.1);
            background: #f5f5f5;
        }}
        
        /* ==================== SUCCESS ANIMATION ==================== */
        .success-animation {{
            text-align: center;
            padding: 4rem 2rem;
        }}
        
        .success-checkmark {{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: linear-gradient(135deg, #4caf50, #8bc34a);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 2rem;
            animation: bounceIn 0.8s ease-out;
        }}
        
        .success-checkmark svg {{
            width: 50px;
            height: 50px;
            stroke: white;
            stroke-width: 3;
        }}
        
        .success-title {{
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: var(--onyx-black);
            margin-bottom: 1rem;
        }}
        
        .success-message {{
            font-family: 'Inter', sans-serif;
            color: #666;
            font-size: 1. 1rem;
        }}
        
        /* ==================== CATEGORY CARDS ==================== */
        .category-card {{
            position: relative;
            height: 300px;
            border-radius: var(--border-radius-lg);
            overflow: hidden;
            cursor: pointer;
            transition: all var(--transition-medium);
        }}
        
        .category-card:hover {{
            transform: scale(1.02);
        }}
        
        .category-card-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform var(--transition-slow);
        }}
        
        .category-card:hover .category-card-image {{
            transform: scale(1.1);
        }}
        
        .category-card-overlay {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 2rem;
            background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
        }}
        
        .category-card-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            color: white;
            font-weight: 600;
        }}
        
        .category-card-count {{
            font-family: 'Inter', sans-serif;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.9rem;
        }}
        
        /* ==================== SEARCH HIGHLIGHT ==================== */
        .search-highlight {{
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.3), rgba(212, 175, 55, 0.1));
            padding: 0 4px;
            border-radius: 4px;
        }}
        
        /* ==================== EMPTY STATE ==================== */
        .empty-state {{
            text-align: center;
            padding: 4rem 2rem;
        }}
        
        .empty-state-icon {{
            font-size: 5rem;
            margin-bottom: 1.5rem;
            opacity: 0.5;
        }}
        
        .empty-state-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            color: var(--onyx-black);
            margin-bottom: 0.5rem;
        }}
        
        .empty-state-message {{
            font-family: 'Inter', sans-serif;
            color: #666;
            margin-bottom: 2rem;
        }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)