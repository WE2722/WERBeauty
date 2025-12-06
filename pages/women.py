"""
Women's collection page for WERBEAUTY.
Product listing with filters and search for women's products.
"""

import streamlit as st
from components.animated_header import render_animated_header, render_section_header
from components.filters_panel import render_filters_panel
from components.product_card import render_product_grid
from utils.product_loader import load_women_products, filter_products, search_products
from utils.helpers import highlight_text


def render():
    """
    Render the women's collection page.
    """
    # Set gender preference
    st.session_state["gender"] = "women"
    
    # Hero Header
    render_animated_header(
        title="Women's Collection",
        subtitle="Luxury beauty essentials for the elegant woman",
        gender="women"
    )
    
    # Main content layout
    col_filters, col_products = st.columns([1, 3])
    
    with col_filters:
        filters = render_filters_panel(gender="women")
    
    with col_products:
        # Search bar
        render_search_section()
        
        # Load and filter products
        products = load_women_products()
        
        # Apply search
        search_query = st.session_state.get("search_query", "")
        if search_query:
            products = search_products(products, search_query)
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, rgba(192, 195, 200, 0.1), rgba(10, 26, 63, 0.1));
                padding: 1rem 1.5rem;
                border-radius: 12px;
                margin-bottom: 1.5rem;
                border-left: 4px solid #C0C3C8;
            ">
                <p style="margin: 0; color: #666;">
                    Showing results for "<strong>{search_query}</strong>" ({len(products)} products found)
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Apply filters
        products = filter_products(products, filters)
        
        # Results header
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
            <p style="color: #666; margin: 0;">{len(products)} products</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Product grid
        if products:
            render_product_grid(products, columns=3, key_prefix="women")
        else:
            render_empty_results()


def render_search_section():
    """
    Render the search bar with highlighting support.
    """
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 0.5rem;">
            🔍 Search Products
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    search = st.text_input(
        "Search",
        value=st.session_state.get("search_query", ""),
        placeholder="Search skincare, makeup, fragrances...",
        label_visibility="collapsed",
        key="women_search"
    )
    
    if search != st.session_state.get("search_query", ""):
        st.session_state["search_query"] = search
        st.rerun()


def render_empty_results():
    """
    Render empty results state.
    """
    st.markdown("""
    <div class="empty-state animate-fadeInUp">
        <div class="empty-state-icon">💄</div>
        <h3 class="empty-state-title">No Products Found</h3>
        <p class="empty-state-message">
            Try adjusting your filters or search for something else.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Reset All Filters", key="reset_women_filters", use_container_width=True):
        st.session_state["filters"] = {
            "price_range": (0, 500),
            "category": "All",
            "skin_type": "All Skin Types",
            "hair_type": "All Hair Types",
            "sort_by": "popularity"
        }
        st.session_state["search_query"] = ""
        st.rerun()
