# Contributing to WERBEAUTY

First off, thank you for considering contributing to WERBEAUTY! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## 📜 Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

### Our Standards

- Be respectful and considerate
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what's best for the project
- Show empathy towards other community members

## 🤝 How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear title**: Summarize the problem
2. **Description**: Detailed explanation of the issue
3. **Steps to reproduce**: How to trigger the bug
4. **Expected behavior**: What should happen
5. **Actual behavior**: What actually happens
6. **Screenshots**: If applicable
7. **Environment**: OS, Python version, browser

**Example:**

```
Title: Cart quantity doesn't update after adding product

Description: When clicking "Add to Cart" button, the quantity counter 
doesn't increment.

Steps to Reproduce:
1. Go to Women's page
2. Click "Add to Cart" on any product
3. Check cart icon counter

Expected: Counter should show 1
Actual: Counter remains at 0

Environment: Windows 11, Python 3.10, Chrome 120
```

### Suggesting Features

We love new ideas! Create an enhancement issue with:

1. **Problem**: What problem does this solve?
2. **Solution**: Your proposed feature
3. **Alternatives**: Other solutions you considered
4. **Benefits**: How does this improve WERBEAUTY?
5. **Mockups**: Visual examples (if applicable)

### Improving Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add missing information
- Improve code examples
- Translate documentation
- Create tutorials or guides

## 🛠️ Development Setup

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/WERBeauty.git
cd WERBeauty
```

### 2. Create Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Set Up Environment

```bash
# Create virtual environment
python -m venv WERvenv

# Activate it
# Windows:
.\WERvenv\Scripts\activate
# macOS/Linux:
source WERvenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

## 📝 Coding Guidelines

### Python Style

Follow [PEP 8](https://pep8.org/) style guide:

```python
# Good
def calculate_total_price(items: list, tax_rate: float = 0.08) -> float:
    """
    Calculate total price including tax.
    
    Args:
        items: List of product dictionaries
        tax_rate: Tax percentage as decimal
    
    Returns:
        Total price with tax
    """
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    return subtotal * (1 + tax_rate)

# Bad
def calc(i,t=0.08):
    s=sum(x['price']*x['quantity'] for x in i)
    return s*(1+t)
```

### Naming Conventions

- **Functions**: `snake_case` - `def get_product_by_id()`
- **Classes**: `PascalCase` - `class ProductManager`
- **Constants**: `UPPER_SNAKE_CASE` - `MAX_CART_ITEMS = 50`
- **Variables**: `snake_case` - `user_cart = []`

### Docstrings

Use Google-style docstrings:

```python
def filter_products(products: list, category: str = None, 
                   min_price: float = 0, max_price: float = float('inf')) -> list:
    """
    Filter products based on category and price range.
    
    Args:
        products: List of product dictionaries to filter
        category: Product category (e.g., 'Skincare', 'Makeup')
        min_price: Minimum price threshold
        max_price: Maximum price threshold
    
    Returns:
        Filtered list of products matching criteria
    
    Example:
        >>> products = get_all_products()
        >>> skincare = filter_products(products, category='Skincare', max_price=50)
        >>> print(len(skincare))
        12
    """
    filtered = products
    
    if category:
        filtered = [p for p in filtered if p['category'] == category]
    
    filtered = [p for p in filtered if min_price <= p['price'] <= max_price]
    
    return filtered
```

### Component Structure

Keep components focused and reusable:

```python
# components/custom_button.py
import streamlit as st

def render_custom_button(
    label: str,
    icon: str = "",
    variant: str = "primary",
    on_click = None,
    key: str = None
) -> bool:
    """
    Render a styled custom button.
    
    Args:
        label: Button text
        icon: Emoji or icon to display
        variant: Style variant ('primary', 'secondary', 'danger')
        on_click: Callback function
        key: Unique key for Streamlit
    
    Returns:
        True if button was clicked
    """
    button_html = f"""
        <button class="custom-btn custom-btn-{variant}">
            {icon} {label}
        </button>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button(label, on_click=on_click, key=key, type="primary")
```

## 💬 Commit Messages

Write clear, descriptive commit messages:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style (formatting, no logic change)
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good commits
git commit -m "feat(cart): add quantity update functionality"
git commit -m "fix(navbar): resolve mobile menu overlap issue"
git commit -m "docs(readme): add installation instructions"
git commit -m "style(components): format product card code"
git commit -m "refactor(utils): optimize recommendation algorithm"

# Bad commits
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "WIP"
```

### Detailed Commit

```bash
git commit -m "feat(recommendations): implement collaborative filtering

- Add similarity calculation based on user preferences
- Include product category matching
- Optimize performance with caching
- Add unit tests for recommendation engine

Closes #42"
```

## 🔄 Pull Request Process

### Before Submitting

1. **Test thoroughly**: Ensure your changes work
2. **Update docs**: Modify README/docs if needed
3. **Check style**: Run linter if available
4. **Sync with main**: Rebase on latest main branch

```bash
git fetch origin
git rebase origin/main
```

### Creating PR

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open PR on GitHub**

3. **Fill PR template**:
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [x] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Testing
   Describe how you tested this
   
   ## Screenshots (if applicable)
   Add screenshots
   
   ## Checklist
   - [x] Code follows style guidelines
   - [x] Self-review completed
   - [x] Comments added for complex code
   - [x] Documentation updated
   - [x] No new warnings generated
   - [x] Tests added/updated
   ```

### PR Review Process

1. **Automated checks**: Wait for CI/CD (if configured)
2. **Code review**: Maintainers will review your code
3. **Address feedback**: Make requested changes
4. **Approval**: Once approved, PR will be merged
5. **Celebration**: 🎉 Your contribution is now part of WERBEAUTY!

### After Merge

```bash
# Update your local repo
git checkout main
git pull origin main

# Delete feature branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

## 🧪 Testing

### Manual Testing Checklist

Before submitting PR, test:

- [ ] All pages load correctly
- [ ] Navigation works between pages
- [ ] Add to cart functionality
- [ ] Cart quantity updates
- [ ] Favorites add/remove
- [ ] Search returns results
- [ ] Filters work correctly
- [ ] Responsive design (mobile/tablet)
- [ ] No console errors
- [ ] Chatbot responds (if modified)

### Testing Your Changes

```bash
# Run the app
streamlit run app.py

# Test in different browsers
# - Chrome
# - Firefox
# - Safari
# - Edge

# Test responsive design
# - Resize browser window
# - Use Chrome DevTools mobile view
```

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Botpress Documentation](https://botpress.com/docs)
- [Python PEP 8 Style Guide](https://pep8.org)
- [Git Best Practices](https://git-scm.com/book/en/v2)

## 🎓 Learning & Mentorship

New to open source? We're here to help!

- Ask questions in Issues or Discussions
- Request guidance on implementation
- Pair programming sessions available
- Code review learning opportunities

## 🙏 Thank You!

Every contribution, no matter how small, makes WERBEAUTY better. We appreciate:

- Bug reports 🐛
- Feature suggestions 💡
- Documentation improvements 📝
- Code contributions 💻
- Spreading the word 📢

**Happy Contributing!** 🚀

---

*Questions? Open an issue or discussion, and we'll help you get started!*
