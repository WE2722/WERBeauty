"""
Router module for handling page navigation. 
"""

import streamlit as st


def route_to_page():
    """
    Routes to the appropriate page based on session state.
    """
    current_page = st.session_state.get("current_page", "home")
    
    if current_page == "home":
        from pages import home
        home.render()
    elif current_page == "women":
        from pages import women
        women.render()
    elif current_page == "men":
        from pages import men
        men.render()
    elif current_page == "cart":
        from pages import cart
        cart.render()
    elif current_page == "favorites":
        from pages import favorites
        favorites.render()
    elif current_page == "recommended":
        from pages import recommended
        recommended.render()
    elif current_page == "payment":
        from pages import payment
        payment.render()
    elif current_page == "login":
        from pages import login
        login.render()
    elif current_page == "signup":
        from pages import signup
        signup.render()
    elif current_page == "forgot_password":
        from pages import forgot_password
        forgot_password.render()
    elif current_page == "profile":
        from pages import profile
        profile.render()
    else:
        from pages import home
        home.render()