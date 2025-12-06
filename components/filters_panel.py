"""
Filters panel component for WERBEAUTY.
Advanced filtering options for product listings.
"""

import streamlit as st
from config.constants import WOMEN_CATEGORIES, MEN_CATEGORIES, SKIN_TYPES, HAIR_TYPES, SORT_OPTIONS


def render_filters_panel(gender: str = "women"):
    """
    Render the filters panel with all filtering options.
    
    Args:
        gender: 'women' or 'men' to determine categories
    
    Returns:
        Dictionary containing all filter values
    """
    categories = WOMEN_CATEGORIES if gender == "women" else MEN_CATEGORIES
    
    st.markdown("""
    <div class="filters-panel">
        <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 1. 5rem;">
            🔍 Filter Products
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize filter state
    if "filters" not in st. session_state:
        st.session_state["filters"] = {
            "price_range": (0, 500),
            "category": "All",
            "skin_type": "All Skin Types",
            "hair_type": "All Hair Types",
            "sort_by": "popularity"
        }
    
    filters = st.session_state["filters"]
    
    # Search
    search_query = st.text_input(
        "🔎 Search Products",
        value=st.session_state.get("search_query", ""),
        placeholder="Search by name or description..."
    )
    st.session_state["search_query"] = search_query
    
    st.markdown("---")
    
    # Category filter
    st.markdown("**Category**")
    selected_category = st.selectbox(
        "Select Category",
        categories,
        index=categories.index(filters.get("category", "All")) if filters.get("category", "All") in categories else 0,
        label_visibility="collapsed"
    )
    filters["category"] = selected_category
    
    st.markdown("---")
    
    # Price range
    st.markdown("**Price Range**")
    price_range = st.slider(
        "Price Range",
        min_value=0,
        max_value=500,
        value=filters.get("price_range", (0, 500)),
        step=10,
        format="$%d",
        label_visibility="collapsed"
    )
    filters["price_range"] = price_range
    
    st.markdown(f"${price_range[0]} - ${price_range[1]}")
    
    st.markdown("---")
    
    # Skin type filter
    st.markdown("**Skin Type**")
    selected_skin_type = st.selectbox(
        "Select Skin Type",
        SKIN_TYPES,
        index=SKIN_TYPES. index(filters.get("skin_type", "All Skin Types")) if filters.get("skin_type", "All Skin Types") in SKIN_TYPES else 0,
        label_visibility="collapsed"
    )
    filters["skin_type"] = selected_skin_type
    
    st.markdown("---")
    
    # Hair type filter
    st.markdown("**Hair Type**")
    selected_hair_type = st.selectbox(
        "Select Hair Type",
        HAIR_TYPES,
        index=HAIR_TYPES.index(filters.get("hair_type", "All Hair Types")) if filters.get("hair_type", "All Hair Types") in HAIR_TYPES else 0,
        label_visibility="collapsed"
    )
    filters["hair_type"] = selected_hair_type
    
    st.markdown("---")
    
    # Sort by
    st.markdown("**Sort By**")
    sort_options_list = list(SORT_OPTIONS.keys())
    sort_options_display = list(SORT_OPTIONS.values())
    current_sort_index = sort_options_list.index(filters.get("sort_by", "popularity")) if filters.get("sort_by", "popularity") in sort_options_list else 0
    
    selected_sort = st.selectbox(
        "Sort By",
        sort_options_display,
        index=current_sort_index,
        label_visibility="collapsed"
    )
    filters["sort_by"] = sort_options_list[sort_options_display.index(selected_sort)]
    
    st.markdown("---")
    
    # Reset filters button
    if st.button("🔄 Reset Filters", use_container_width=True):
        st.session_state["filters"] = {
            "price_range": (0, 500),
            "category": "All",
            "skin_type": "All Skin Types",
            "hair_type": "All Hair Types",
            "sort_by": "popularity"
        }
        st.session_state["search_query"] = ""
        st.rerun()
    
    st.session_state["filters"] = filters
    
    return filters