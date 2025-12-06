"""
WERBEAUTY - Luxury E-Commerce Application
Main entry point for the Streamlit application. 
Author: WERBEAUTY Development Team
Version: 1.0.0
"""

import streamlit as st
from config.theme import apply_custom_theme, initialize_session_state
from components.navbar import render_navbar
from components.footer import render_footer
from components.ai_assistant_toggle import render_ai_assistant
from components.onboarding_gender_selector import render_onboarding
from router import route_to_page


def main():
    """
    Main application entry point. 
    Initializes the app, applies theme, and renders components.
    """
    # Page configuration
    st.set_page_config(
        page_title="WERBEAUTY | Luxury Cosmetics",
        page_icon="💎",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Apply custom theme and CSS
    apply_custom_theme()
    
    # Check if onboarding is needed
    if not st.session_state.get("onboarding_complete", False):
        render_onboarding()
        return
    
    # Render navigation bar
    render_navbar()
    
    # Route to appropriate page
    route_to_page()
    
    # Render AI assistant toggle
    render_ai_assistant()
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()