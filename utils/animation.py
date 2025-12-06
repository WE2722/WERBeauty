"""
Animation utility for WERBEAUTY application.
Provides CSS animations and loading skeletons.
"""


def get_animation_css():
    """
    Get custom CSS for animations.
    
    Returns:
        str: CSS string with animation definitions
    """
    return """
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }
    
    .slide-in {
        animation: slideIn 0.5s ease-out;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    .shimmer {
        animation: shimmer 2s infinite;
        background: linear-gradient(to right, #f0f0f0 0%, #e0e0e0 50%, #f0f0f0 100%);
        background-size: 1000px 100%;
    }
    
    .card-hover {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card-hover:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    
    .btn-animation {
        transition: all 0.3s ease;
    }
    
    .btn-animation:hover {
        transform: scale(1.05);
    }
    
    .btn-animation:active {
        transform: scale(0.95);
    }
    </style>
    """


def get_loading_skeleton(width="100%", height="200px", count=1):
    """
    Generate a loading skeleton HTML.
    
    Args:
        width: Width of the skeleton (default: "100%")
        height: Height of the skeleton (default: "200px")
        count: Number of skeleton items (default: 1)
        
    Returns:
        str: HTML string with skeleton loaders
    """
    skeleton_html = get_animation_css()
    
    for i in range(count):
        skeleton_html += f"""
        <div style="width: {width}; height: {height}; margin-bottom: 20px;" 
             class="shimmer" 
             role="status" 
             aria-label="Loading...">
        </div>
        """
    
    return skeleton_html


def get_fade_in_animation(delay=0):
    """
    Get fade-in animation style.
    
    Args:
        delay: Animation delay in seconds (default: 0)
        
    Returns:
        str: CSS style string
    """
    return f"animation: fadeIn 0.5s ease-in {delay}s; animation-fill-mode: both;"


def get_slide_in_animation(delay=0):
    """
    Get slide-in animation style.
    
    Args:
        delay: Animation delay in seconds (default: 0)
        
    Returns:
        str: CSS style string
    """
    return f"animation: slideIn 0.5s ease-out {delay}s; animation-fill-mode: both;"


def render_success_animation():
    """
    Render a success animation with checkmark.
    Used for order confirmations and successful actions.
    
    Returns:
        str: HTML string with success animation
    """
    return """
    <style>
    @keyframes checkmark {
        0% {
            stroke-dashoffset: 100;
        }
        100% {
            stroke-dashoffset: 0;
        }
    }
    
    @keyframes scaleIn {
        0% {
            transform: scale(0);
            opacity: 0;
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    .success-animation {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    
    .success-checkmark {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: block;
        stroke-width: 3;
        stroke: #4CAF50;
        stroke-miterlimit: 10;
        box-shadow: inset 0px 0px 0px #4CAF50;
        animation: scaleIn 0.5s ease-out;
    }
    
    .success-checkmark__circle {
        stroke-dasharray: 166;
        stroke-dashoffset: 166;
        stroke-width: 3;
        stroke-miterlimit: 10;
        stroke: #4CAF50;
        fill: #f0f9f0;
        animation: checkmark 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
        animation-delay: 0.2s;
    }
    
    .success-checkmark__check {
        transform-origin: 50% 50%;
        stroke-dasharray: 48;
        stroke-dashoffset: 48;
        animation: checkmark 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards;
    }
    </style>
    
    <div class="success-animation">
        <svg class="success-checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
            <circle class="success-checkmark__circle" cx="26" cy="26" r="25" fill="none"/>
            <path class="success-checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/>
        </svg>
    </div>
    """
