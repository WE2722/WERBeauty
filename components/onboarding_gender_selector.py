"""
Onboarding gender selector component for WERBEAUTY.
Full-screen modal for initial gender preference selection.
"""

import streamlit as st
from config.constants import BRAND_NAME


def render_onboarding():
    """
    Render the onboarding gender selection screen.
    """
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Center content
    st.markdown("<div style='height: 10vh;'></div>", unsafe_allow_html=True)
    
    # Logo and welcome message
    st.markdown(f"""
    <div style="text-align: center; animation: fadeInUp 0.8s ease-out;">
        <h1 style="
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            font-weight: 700;
            background: linear-gradient(135deg, #D4AF37, #f5d76e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        ">{BRAND_NAME}</h1>
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 3rem;
        ">Discover Your Radiant Beauty</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: white;
            margin-bottom: 0.5rem;
        ">Welcome to WERBEAUTY</h2>
        <p style="
            font-family: 'Inter', sans-serif;
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.1rem;
        ">Choose your preferred collection to personalize your experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Gender selection buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        subcol1, subcol2 = st.columns(2)
        
        with subcol1:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #B76E79, #d4a5ad);
                border-radius: 24px;
                padding: 2rem;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 10px 40px rgba(183, 110, 121, 0.3);
            " onmouseover="this.style.transform='scale(1.05) translateY(-10px)'" 
               onmouseout="this.style.transform='scale(1)'">
                <div style="font-size: 4rem; margin-bottom: 1rem;">👩</div>
                <h3 style="
                    font-family: 'Playfair Display', serif;
                    font-size: 1.5rem;
                    color: white;
                    margin-bottom: 0.5rem;
                ">Women</h3>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">
                    Makeup, Skincare, Perfumes & More
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Shop Women's Collection", key="onboard_women", use_container_width=True):
                st. session_state["gender"] = "women"
                st.session_state["onboarding_complete"] = True
                st.session_state["current_page"] = "home"
                st.rerun()
        
        with subcol2:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #0A1A3F, #1a2a4f);
                border-radius: 24px;
                padding: 2rem;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 10px 40px rgba(10, 26, 63, 0.3);
            " onmouseover="this.style.transform='scale(1.05) translateY(-10px)'" 
               onmouseout="this.style. transform='scale(1)'">
                <div style="font-size: 4rem; margin-bottom: 1rem;">👨</div>
                <h3 style="
                    font-family: 'Playfair Display', serif;
                    font-size: 1.5rem;
                    color: white;
                    margin-bottom: 0.5rem;
                ">Men</h3>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">
                    Beard Care, Grooming, Perfumes & More
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Shop Men's Collection", key="onboard_men", use_container_width=True):
                st.session_state["gender"] = "men"
                st.session_state["onboarding_complete"] = True
                st.session_state["current_page"] = "home"
                st.rerun()