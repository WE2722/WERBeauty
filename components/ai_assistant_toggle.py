"""
AI Assistant toggle component for WERBEAUTY.
Floating button with Botpress chat integration.
"""

import streamlit as st

def render_ai_assistant():
    """
    Render the floating AI assistant button with Botpress chatbot integration.
    Uses CSS Checkbox Hack to avoid Streamlit JS blocking issues.
    """
    # The specific Botpress URL you requested
    botpress_url = "https://cdn.botpress.cloud/webchat/v3.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/10/13/15/20251013152509-KVW9QPHI.json"

    st.markdown(f"""
    <!-- Global CSS Styles -->
    <style>
        /* 1. Hide the actual checkbox input */
        #chat-toggle {{
            display: none;
        }}

        /* 2. Style the Floating Button (which is actually a Label) */
        .ai-float-btn {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: linear-gradient(135deg, #D4AF37, #f5d76e);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 10px 40px rgba(212, 175, 55, 0.5);
            z-index: 999999;
            font-size: 2.2rem;
            border: 3px solid white;
            transition: transform 0.3s ease;
            user-select: none;
            animation: ai-pulse 2s infinite;
        }}

        .ai-float-btn:hover {{
            transform: scale(1.1);
        }}

        @keyframes ai-pulse {{
            0% {{ box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.7); }}
            70% {{ box-shadow: 0 0 0 20px rgba(212, 175, 55, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(212, 175, 55, 0); }}
        }}

        /* 3. The Chat Container - Hidden by default */
        .ai-chat-container {{
            position: fixed;
            bottom: 110px;
            right: 30px;
            width: 380px;
            height: 600px;
            max-height: 80vh;
            background: white;
            border-radius: 20px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            z-index: 999998;
            overflow: hidden;
            
            /* Hidden State Properties */
            opacity: 0;
            visibility: hidden;
            transform: translateY(20px) scale(0.95);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            pointer-events: none; /* Prevents clicking when hidden */
        }}

        /* 4. THE MAGIC: When checkbox is checked, show the container */
        #chat-toggle:checked ~ .ai-chat-container {{
            opacity: 1;
            visibility: visible;
            transform: translateY(0) scale(1);
            pointer-events: auto;
        }}

        /* Rotate the button icon when open */
        #chat-toggle:checked ~ .ai-float-btn {{
            transform: rotate(45deg);
            background: #ff6b6b; /* Optional: Change color to 'close' red */
            border-color: #ff6b6b;
        }}
        
        /* Inner Chat Styling */
        .chat-header {{
            background: linear-gradient(135deg, #D4AF37, #f5d76e);
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
        }}
        
        .chat-header h3 {{
            margin: 0;
            font-size: 16px;
            font-family: sans-serif;
            font-weight: 600;
        }}

        .close-lbl {{
            cursor: pointer;
            font-size: 20px;
            background: rgba(255,255,255,0.2);
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .chat-body {{
            height: calc(100% - 60px);
            width: 100%;
            background: #f9f9f9;
        }}

        iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>

    <!-- The Toggle Logic (Order matters!) -->
    
    <!-- 1. The Hidden Checkbox Control -->
    <input type="checkbox" id="chat-toggle">
    
    <!-- 2. The Floating Button (Acting as a label for the checkbox) -->
    <label for="chat-toggle" class="ai-float-btn" title="Chat with WER AI">
        🤖
    </label>
    
    <!-- 3. The Chat Window -->
    <div class="ai-chat-container">
        <div class="chat-header">
            <h3>💬 WER AI Assistant</h3>
            <!-- This X also toggles the checkbox to close -->
            <label for="chat-toggle" class="close-lbl">✕</label>
        </div>
        <div class="chat-body">
            <iframe src="{botpress_url}" allow="microphone; clipboard-write"></iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Optional Sidebar Content
    with st.sidebar:
        st.markdown("---")
        st.info("💡 **Tip:** Click the 🤖 button in the bottom-right corner to start chatting!")