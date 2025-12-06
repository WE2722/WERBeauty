"""
Category carousel component for WERBEAUTY. 
Horizontal scrolling category cards. 
"""

import streamlit as st
from config.constants import PLACEHOLDER_IMAGES


def render_category_carousel(gender: str = "women"):
    """
    Render a horizontal carousel of category cards.
    
    Args:
        gender: 'women' or 'men' to show relevant categories
    """
    if gender == "men":
        categories = [
            {"name": "Beard Care", "image": "https://images.unsplash. com/photo-1621605815971-fbc98d665033?w=400&h=300&fit=crop", "count": 24},
            {"name": "Perfumes", "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=400&h=300&fit=crop", "count": 18},
            {"name": "Hair Care", "image": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=400&h=300&fit=crop", "count": 32},
            {"name": "Self Care", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=300&fit=crop", "count": 28},
            {"name": "Grooming", "image": "https://images. unsplash.com/photo-1621607512214-68297480165e?w=400&h=300&fit=crop", "count": 15},
        ]
    else:
        categories = [
            {"name": "Makeup", "image": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796? w=400&h=300&fit=crop", "count": 45},
            {"name": "Perfumes", "image": "https://images. unsplash.com/photo-1541643600914-78b084683601?w=400&h=300&fit=crop", "count": 28},
            {"name": "Skincare", "image": "https://images.unsplash.com/photo-1570194065650-d99fb4b38b7e?w=400&h=300&fit=crop", "count": 52},
            {"name": "Hair Care", "image": "https://images. unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400&h=300&fit=crop", "count": 36},
            {"name": "Self Care", "image": "https://images. unsplash.com/photo-1596462502278-27bfdc403348?w=400&h=300&fit=crop", "count": 41},
        ]
    
    cols = st.columns(len(categories))
    
    for idx, (col, cat) in enumerate(zip(cols, categories)):
        with col:
            card_html = f"""
            <div class="category-card animate-fadeInUp" style="animation-delay: {idx * 0.1}s;">
                <img src="{cat['image']}" alt="{cat['name']}" class="category-card-image" 
                     onerror="this. src='https://via.placeholder.com/400x300?text={cat['name']}'">
                <div class="category-card-overlay">
                    <h3 class="category-card-title">{cat['name']}</h3>
                    <p class="category-card-count">{cat['count']} Products</p>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            if st.button(f"Shop {cat['name']}", key=f"cat_{gender}_{idx}", use_container_width=True):
                st.session_state["current_page"] = gender
                st.session_state["filters"]["category"] = cat["name"] if cat["name"] != "Self Care" else "Self-Care"
                st.rerun()