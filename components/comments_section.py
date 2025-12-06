"""
Comments/Reviews section component for WERBEAUTY.
Customer reviews and ratings display.
"""

import streamlit as st
from datetime import datetime


def render_comments_section(product_id: str = None):
    """
    Render customer reviews and comments section.
    
    Args:
        product_id: Optional product ID to filter reviews
    """
    # Sample reviews data
    reviews = [
        {
            "author": "Sarah M.",
            "rating": 5,
            "date": "2024-11-15",
            "comment": "Absolutely love this product! The quality is outstanding and it arrived quickly.",
            "verified": True
        },
        {
            "author": "Michael T.",
            "rating": 5,
            "date": "2024-11-10",
            "comment": "Best purchase I've made this year. Highly recommend to anyone looking for premium quality.",
            "verified": True
        },
        {
            "author": "Emily R.",
            "rating": 4,
            "date": "2024-11-05",
            "comment": "Great product overall. Packaging was beautiful and the product works as described.",
            "verified": True
        },
        {
            "author": "James K.",
            "rating": 5,
            "date": "2024-10-28",
            "comment": "Exceeded my expectations! Will definitely be ordering again.",
            "verified": True
        }
    ]
    
    st.markdown("""
    <div style="margin-top: 3rem; margin-bottom: 2rem;">
        <h2 style="
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: var(--luxury-gold);
            margin-bottom: 1rem;
        ">Customer Reviews</h2>
        <div style="
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, var(--luxury-gold), transparent);
            margin-bottom: 2rem;
        "></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Overall rating
    avg_rating = sum(r["rating"] for r in reviews) / len(reviews)
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(183, 110, 121, 0.1));
        padding: 2rem;
        border-radius: 18px;
        margin-bottom: 2rem;
        text-align: center;
    ">
        <h3 style="
            font-size: 3rem;
            color: var(--luxury-gold);
            margin: 0;
        ">{avg_rating:.1f}</h3>
        <div style="font-size: 1.5rem; color: var(--luxury-gold); margin: 0.5rem 0;">
            {'⭐' * int(avg_rating)}
        </div>
        <p style="color: #666; margin: 0;">Based on {len(reviews)} reviews</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Individual reviews
    for review in reviews:
        stars = '⭐' * review["rating"]
        verified_badge = '✓ Verified Purchase' if review["verified"] else ''
        
        st.markdown(f"""
        <div style="
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border-left: 4px solid var(--luxury-gold);
            box-shadow: 0 4px 16px rgba(0,0,0,0.05);
        ">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <strong style="color: #0F0F0F; font-size: 1.1rem;">{review["author"]}</strong>
                <span style="color: #999; font-size: 0.9rem;">{review["date"]}</span>
            </div>
            <div style="margin-bottom: 0.5rem;">
                <span style="font-size: 1.2rem;">{stars}</span>
                {f'<span style="color: #4caf50; font-size: 0.85rem; margin-left: 1rem;">{verified_badge}</span>' if verified_badge else ''}
            </div>
            <p style="color: #333; line-height: 1.6; margin: 0;">
                {review["comment"]}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Write a review button
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📝 Write a Review", use_container_width=True, type="primary"):
            st.session_state["show_review_form"] = True
    
    # Review form
    if st.session_state.get("show_review_form", False):
        st.markdown("---")
        st.markdown("### Write Your Review")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name")
        with col2:
            rating = st.selectbox("Rating", [5, 4, 3, 2, 1], format_func=lambda x: "⭐" * x)
        
        comment = st.text_area("Your Review", height=150)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Submit Review", use_container_width=True):
                if name and comment:
                    st.success("Thank you for your review! It has been submitted.")
                    st.session_state["show_review_form"] = False
                    st.rerun()
                else:
                    st.error("Please fill in all fields.")
        with col2:
            if st.button("Cancel", use_container_width=True):
                st.session_state["show_review_form"] = False
                st.rerun()
