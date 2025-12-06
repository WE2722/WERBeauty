"""
Animated header component for WERBEAUTY.
Hero sections with parallax and typewriter effects.
"""

import streamlit as st


def render_animated_header(
    title: str,
    subtitle: str = "",
    show_particles: bool = True,
    gender: str = "women"
):
    """
    Render an animated hero header section.
    
    Args:
        title: Main heading text
        subtitle: Subheading text
        show_particles: Whether to show floating particles
        gender: 'women' or 'men' for color scheme
    """
    if gender == "men":
        gradient_start = "#0A1A3F"
        gradient_end = "#1a2a4f"
    else:
        gradient_start = "#B76E79"
        gradient_end = "#d4a5ad"
    
    particles_html = ""
    if show_particles:
        particles_html = """
        <div class="hero-particles">
            <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
            <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
            <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
            <div class="particle" style="left: 40%; animation-delay: 1s;"></div>
            <div class="particle" style="left: 50%; animation-delay: 3s;"></div>
            <div class="particle" style="left: 60%; animation-delay: 5s;"></div>
            <div class="particle" style="left: 70%; animation-delay: 2.5s;"></div>
            <div class="particle" style="left: 80%; animation-delay: 1.5s;"></div>
            <div class="particle" style="left: 90%; animation-delay: 3.5s;"></div>
        </div>
        """
    
    header_html = f'''
    <div class="hero-section" style="background: linear-gradient(135deg, {gradient_start}, {gradient_end});">
        <div class="hero-content">
            <h1 class="hero-title animate-fadeInUp">{title}</h1>
            <p class="hero-subtitle animate-fadeInUp delay-2">{subtitle}</p>
        </div>
    </div>
    '''
    
    st.markdown(header_html, unsafe_allow_html=True)


def render_section_header(title: str, subtitle: str = ""):
    """
    Render a section header with title and optional subtitle.
    
    Args:
        title: Section title
        subtitle: Optional description
    """
    header_html = f"""
    <div class="section-header animate-fadeInUp">
        <h2 class="section-title">{title}</h2>
        {'<p class="section-subtitle">' + subtitle + '</p>' if subtitle else ''}
        <div class="section-divider"></div>
    </div>
    """
    
    st.markdown(header_html, unsafe_allow_html=True)