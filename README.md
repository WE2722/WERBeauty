# 💄 WERBEAUTY - Luxury Cosmetics E-Commerce Platform

<div align="center">

![WERBEAUTY Logo](https://img.shields.io/badge/WERBEAUTY-Luxury_Cosmetics-B76E79?style=for-the-badge)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Botpress](https://img.shields.io/badge/Botpress-AI_Chatbot-6C63FF?style=for-the-badge)](https://botpress.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*An elegant, AI-powered beauty e-commerce application built with Streamlit and Botpress*

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

</div>

---

## 📖 About

**WERBEAUTY** is a sophisticated luxury cosmetics e-commerce platform that combines modern web technologies with artificial intelligence to deliver an exceptional shopping experience. Built as a school project to demonstrate mastery of **Streamlit** for web development and **Botpress** for conversational AI.

### 🎯 Project Goals

- Showcase advanced **Streamlit** capabilities for building data-driven web applications
- Demonstrate **Botpress** integration for intelligent customer support
- Create a production-ready e-commerce platform with real-world features
- Implement best practices in UI/UX design and code architecture

---

## ✨ Features

### 🛍️ E-Commerce Functionality

- **Smart Product Catalog**
  - Women's & Men's collections
  - Advanced filtering (category, price, rating)
  - Real-time search functionality
  - Detailed product pages with reviews

- **Shopping Cart Management**
  - Add/remove products with quantity control
  - Real-time price calculation
  - Persistent cart across sessions
  - Quick checkout process

- **Favorites/Wishlist System**
  - Save products for later
  - Quick access to saved items
  - Sync across browser sessions

### 🤖 AI-Powered Features

- **Botpress Chatbot Integration**
  - 24/7 customer support
  - Product recommendations
  - Order tracking assistance
  - Natural language understanding
  - Context-aware conversations

- **Recommendation Engine**
  - Personalized product suggestions
  - "Customers also bought" feature
  - Similar product recommendations
  - Trending products display

### 🎨 Premium UI/UX

- **Modern Design**
  - Glass morphism effects
  - Gradient backgrounds with animations
  - Smooth transitions and hover effects
  - Responsive layout (mobile-ready)

- **Interactive Elements**
  - Animated hero sections
  - Dynamic product cards
  - Loading states and skeleton loaders
  - Toast notifications

### 🔒 User Management

- Secure authentication system
- User profiles and preferences
- Order history tracking
- Address book management

---

## 🎥 Demo

### Screenshots

#### Home Page
*Elegant hero section with animated particles and featured collections*

#### Product Catalog
*Advanced filtering and search with beautiful product cards*

#### AI Chatbot
*Intelligent assistant providing instant support and recommendations*

#### Shopping Cart
*Clean, intuitive cart management with real-time updates*

### Live Demo
*[Coming Soon - Deploy link will be added here]*

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/WE2722/WERBeauty.git
cd WERBeauty
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv WERvenv
.\WERvenv\Scripts\activate

# macOS/Linux
python3 -m venv WERvenv
source WERvenv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment (Optional)

Create a `.env` file for custom configurations:

```env
# Botpress Configuration
BOTPRESS_BOT_ID=your_bot_id
BOTPRESS_CLIENT_ID=your_client_id

# App Configuration
APP_TITLE=WERBEAUTY
DEBUG_MODE=False
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📁 Project Structure

```
WERBEAUTY_app/
│
├── app.py                      # Main application entry point
├── router.py                   # Page routing logic
├── requirements.txt            # Python dependencies
│
├── components/                 # Reusable UI components
│   ├── navbar.py              # Navigation bar
│   ├── footer.py              # Footer with links
│   ├── product_card.py        # Product display cards
│   ├── animated_header.py     # Hero sections
│   └── ai_assistant_toggle.py # Chatbot toggle
│
├── pages/                      # Application pages
│   ├── home.py                # Landing page
│   ├── women.py               # Women's collection
│   ├── men.py                 # Men's collection
│   ├── cart.py                # Shopping cart
│   ├── favorites.py           # Wishlist
│   ├── recommended.py         # Recommendations
│   └── payment.py             # Checkout process
│
├── config/                     # Configuration files
│   ├── constants.py           # App constants
│   └── theme.py               # CSS styling
│
├── data/                       # Product data
│   ├── women_products.json    # Women's products
│   └── men_products.json      # Men's products
│
├── utils/                      # Utility functions
│   ├── cart_manager.py        # Cart operations
│   ├── favorites_manager.py   # Favorites management
│   ├── product_utils.py       # Product helpers
│   └── recommendation.py      # Recommendation engine
│
└── WERvenv/                    # Virtual environment (not in repo)
```

---

## 🛠️ Tech Stack

### Frontend Framework
- **[Streamlit 1.50.0](https://streamlit.io)** - Python web framework
  - Multi-page app architecture
  - Session state management
  - Custom CSS styling
  - Component-based design

### AI & Chatbot
- **[Botpress](https://botpress.com)** - Conversational AI platform
  - Natural Language Processing
  - Intent recognition
  - Conversation flow management
  - Multi-turn dialogue support

### Data Management
- **JSON** - Product database
- **Python dictionaries** - Session state
- **Caching** - Performance optimization

### Styling
- **Custom CSS** - Glass morphism, gradients, animations
- **Google Fonts** - Inter & Playfair Display
- **Responsive Design** - Mobile-first approach

---

## 💻 Usage

### Running the Application

```bash
# Standard mode
streamlit run app.py

# Development mode with auto-reload
streamlit run app.py --server.runOnSave=true

# Custom port
streamlit run app.py --server.port=8502
```

### Navigating the App

1. **Home Page**: Browse featured collections and bestsellers
2. **Women/Men Pages**: Explore category-specific products
3. **Search**: Use the search bar to find specific products
4. **Filter**: Apply filters for category, price, and rating
5. **Cart**: Add products and proceed to checkout
6. **Favorites**: Save products for later
7. **Chatbot**: Click the AI assistant for help

### Using the AI Chatbot

```
Example queries:
- "Show me products for dry skin"
- "What's on sale?"
- "Recommend a gift under $50"
- "Track my order #12345"
- "How do I return an item?"
```

---

## 🧪 Testing

### Manual Testing

```bash
# Run the app and test all features
streamlit run app.py
```

Test checklist:
- ✅ Product browsing and filtering
- ✅ Search functionality
- ✅ Add to cart operations
- ✅ Favorites management
- ✅ Chatbot interactions
- ✅ Navigation between pages
- ✅ Responsive design (resize browser)

---

## 🔧 Configuration

### Customizing the Theme

Edit `config/theme.py` to modify colors, fonts, and styles:

```python
# Color scheme
--primary-color: #0A1A3F;
--rose-gold: #B76E79;
--luxury-gold: #D4AF37;
```

### Adding Products

Edit `data/women_products.json` or `data/men_products.json`:

```json
{
  "id": "W001",
  "name": "Product Name",
  "category": "Skincare",
  "price": 49.99,
  "rating": 4.5,
  "image": "image_url",
  "description": "Product description"
}
```

### Botpress Configuration

1. Create a bot on [Botpress Cloud](https://botpress.com)
2. Configure intents and flows
3. Update bot credentials in `components/ai_assistant_toggle.py`

---

## 📊 Features in Detail

### Recommendation Engine

The recommendation system uses collaborative filtering based on:
- User browsing history
- Products in cart
- Favorite items
- Similar product attributes
- Customer purchase patterns

### Session Management

Streamlit session state stores:
- Shopping cart items
- Favorite products
- User preferences
- Current page navigation
- Filter selections

### Performance Optimization

- `@st.cache_data` for product loading
- Lazy loading for images
- Efficient state updates
- Minimized re-renders

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Bugs

1. Check if the bug is already reported in [Issues](https://github.com/WE2722/WERBeauty/issues)
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Provide examples or mockups

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Test thoroughly before submitting
- Update documentation if needed

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

**WERBEAUTY Development Team**

- **Wiame El Hafid** - Developer & Designer
  - GitHub: [@WE2722](https://github.com/WE2722)
  - Email: wiame.el.hafid27@gmail.com
  
- **Houssam Rjili** - Developer & AI Integration
  - GitHub: [@HxRjili](https://github.com/HxRjili)
  - Email: rjilihoussam55@gmail.com

### Acknowledgments

- Streamlit team for the amazing framework
- Botpress for conversational AI platform
- Unsplash for product images
- Google Fonts for typography

---

## 📧 Contact & Support

### Get Help

- **Issues**: [GitHub Issues](https://github.com/WE2722/WERBeauty/issues)
- **Discussions**: [GitHub Discussions](https://github.com/WE2722/WERBeauty/discussions)
- **Email**: support@werbeauty.com

### Social Media

- Instagram: [@werbeauty](https://instagram.com/werbeauty)
- Facebook: [WERBEAUTY](https://facebook.com/werbeauty)
- Twitter: [@werbeauty](https://twitter.com/werbeauty)

---

## 🎓 Educational Purpose

This project was developed as a school assignment to demonstrate proficiency in:

- **Streamlit**: Web application development with Python
- **Botpress**: AI chatbot creation and integration
- **Software Engineering**: Best practices in code organization
- **UI/UX Design**: Creating elegant, user-friendly interfaces
- **E-commerce Logic**: Implementing cart, checkout, and recommendations

### Learning Outcomes

✅ Multi-page Streamlit application architecture  
✅ Session state management for complex workflows  
✅ Custom CSS integration for brand identity  
✅ Botpress conversational AI implementation  
✅ RESTful API integration concepts  
✅ Responsive web design principles  
✅ Git version control and collaboration  

---

## 🚧 Roadmap

### Version 2.0 (Planned)

- [ ] Real payment integration (Stripe/PayPal)
- [ ] User authentication with database
- [ ] Email notifications
- [ ] Advanced analytics dashboard
- [ ] Product reviews system
- [ ] Live chat escalation to human agents
- [ ] Mobile app (React Native)
- [ ] AR try-on feature for makeup

### Future Enhancements

- [ ] Multi-language support
- [ ] Currency conversion
- [ ] Loyalty points system
- [ ] Subscription boxes
- [ ] Beauty quiz for personalization
- [ ] Social media integration
- [ ] Influencer partnership portal

---

## 📈 Project Stats

- **Lines of Code**: ~3,000+
- **Components**: 15+
- **Pages**: 6 main pages
- **Products**: 100+ items
- **Features**: 20+ core functionalities
- **Development Time**: [Your timeline]

---

## 🌟 Star Us!

If you find this project helpful or interesting, please consider giving it a ⭐ on GitHub!

---

<div align="center">

**Made with ❤️ by Wiame El Hafid & Houssam Rjili**

*Built with [Streamlit](https://streamlit.io) & [Botpress](https://botpress.com)*

© 2025 WERBEAUTY. All rights reserved.

[⬆ Back to Top](#-werbeauty---luxury-cosmetics-e-commerce-platform)

</div>
