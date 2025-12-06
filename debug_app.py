"""
WERBEAUTY Application Debugging Script
======================================
This script performs comprehensive diagnostics to identify issues.
"""

import sys
import os
from pathlib import Path

print("=" * 80)
print("WERBEAUTY APPLICATION DEBUG REPORT")
print("=" * 80)
print()

# 1. ENVIRONMENT CHECK
print("1. ENVIRONMENT CHECK")
print("-" * 80)
print(f"Python Version: {sys.version}")
print(f"Python Executable: {sys.executable}")
print(f"Current Directory: {os.getcwd()}")
print(f"Script Location: {Path(__file__).parent}")
print()

# 2. REQUIRED PACKAGES CHECK
print("2. PACKAGE INSTALLATION CHECK")
print("-" * 80)
required_packages = [
    'streamlit',
    'pandas',
    'Pillow',
    'requests'
]

for package in required_packages:
    try:
        module = __import__(package)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {package}: {version}")
    except ImportError as e:
        print(f"✗ {package}: NOT INSTALLED - {e}")
print()

# 3. FILE STRUCTURE CHECK
print("3. FILE STRUCTURE CHECK")
print("-" * 80)
required_files = [
    'app.py',
    'router.py',
    'requirements.txt',
    'components/__init__.py',
    'components/navbar.py',
    'components/footer.py',
    'components/ai_assistant_toggle.py',
    'components/comments_section.py',
    'config/__init__.py',
    'config/constants.py',
    'config/theme.py',
    'data/women_products.json',
    'data/men_products.json',
    'pages/home.py',
    'pages/women.py',
    'pages/men.py',
    'pages/cart.py',
    'pages/favorites.py',
    'pages/payment.py',
    'pages/recommended.py',
    'utils/favorites_manager.py',
    'utils/cart_manager.py',
    'utils/helpers.py',
    'utils/product_loader.py',
    'utils/recommendation_engine.py'
]

for file_path in required_files:
    full_path = Path(file_path)
    if full_path.exists():
        size = full_path.stat().st_size
        print(f"✓ {file_path} ({size} bytes)")
    else:
        print(f"✗ {file_path} - MISSING!")
print()

# 4. IMPORT TESTS
print("4. MODULE IMPORT TESTS")
print("-" * 80)

test_imports = [
    ('app', 'Main App'),
    ('router', 'Router'),
    ('config.constants', 'Constants'),
    ('config.theme', 'Theme'),
    ('components', 'Components Package'),
    ('components.navbar', 'Navbar'),
    ('components.footer', 'Footer'),
    ('components.ai_assistant_toggle', 'AI Assistant'),
    ('components.comments_section', 'Comments Section'),
    ('pages.home', 'Home Page'),
    ('pages.women', 'Women Page'),
    ('pages.men', 'Men Page'),
    ('pages.cart', 'Cart Page'),
    ('pages.favorites', 'Favorites Page'),
    ('pages.payment', 'Payment Page'),
    ('pages.recommended', 'Recommended Page'),
    ('utils.favorites_manager', 'Favorites Manager'),
    ('utils.cart_manager', 'Cart Manager'),
    ('utils.helpers', 'Helpers'),
    ('utils.product_loader', 'Product Loader'),
    ('utils.recommendation_engine', 'Recommendation Engine')
]

import_errors = []
for module_name, display_name in test_imports:
    try:
        __import__(module_name)
        print(f"✓ {display_name} ({module_name})")
    except Exception as e:
        error_msg = str(e)
        print(f"✗ {display_name} ({module_name})")
        print(f"  Error: {error_msg}")
        import_errors.append((module_name, display_name, error_msg))
print()

# 5. COMPONENT RENDER FUNCTION CHECK
print("5. COMPONENT RENDER FUNCTION CHECK")
print("-" * 80)
components_to_check = [
    'components.navbar',
    'components.footer',
    'components.ai_assistant_toggle',
    'components.comments_section',
    'components.product_card',
    'components.filters_panel',
    'components.animated_header',
    'components.category_carousel',
    'components.testimonials_slider',
    'components.onboarding_gender_selector'
]

for comp in components_to_check:
    try:
        module = __import__(comp, fromlist=[''])
        if hasattr(module, 'render'):
            print(f"✓ {comp}.render() exists")
        else:
            print(f"✗ {comp} - NO render() FUNCTION!")
    except Exception as e:
        print(f"✗ {comp} - Import failed: {e}")
print()

# 6. PAGE RENDER FUNCTION CHECK
print("6. PAGE RENDER FUNCTION CHECK")
print("-" * 80)
pages_to_check = [
    'pages.home',
    'pages.women',
    'pages.men',
    'pages.cart',
    'pages.favorites',
    'pages.payment',
    'pages.recommended'
]

for page in pages_to_check:
    try:
        module = __import__(page, fromlist=[''])
        if hasattr(module, 'render'):
            print(f"✓ {page}.render() exists")
        else:
            print(f"✗ {page} - NO render() FUNCTION!")
    except Exception as e:
        print(f"✗ {page} - Import failed: {e}")
print()

# 7. DATA FILE VALIDATION
print("7. DATA FILE VALIDATION")
print("-" * 80)
import json

data_files = [
    'data/women_products.json',
    'data/men_products.json',
    'data/homepage_slides.json'
]

for data_file in data_files:
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                print(f"✓ {data_file} - Valid JSON ({len(data)} items)")
            elif isinstance(data, dict):
                print(f"✓ {data_file} - Valid JSON (dict with {len(data)} keys)")
            else:
                print(f"⚠ {data_file} - Valid JSON but unexpected type: {type(data)}")
    except FileNotFoundError:
        print(f"✗ {data_file} - FILE NOT FOUND!")
    except json.JSONDecodeError as e:
        print(f"✗ {data_file} - INVALID JSON: {e}")
    except Exception as e:
        print(f"✗ {data_file} - Error: {e}")
print()

# 8. STREAMLIT CONFIGURATION CHECK
print("8. STREAMLIT CONFIGURATION")
print("-" * 80)
streamlit_config_files = [
    '.streamlit/config.toml',
    '.streamlit/secrets.toml'
]

for config_file in streamlit_config_files:
    if Path(config_file).exists():
        print(f"✓ {config_file} exists")
    else:
        print(f"⚠ {config_file} not found (optional)")
print()

# 9. SESSION STATE INITIALIZATION CHECK
print("9. SESSION STATE INITIALIZATION")
print("-" * 80)
try:
    import streamlit as st
    print("✓ Streamlit imported successfully")
    print(f"  Streamlit version: {st.__version__}")
except Exception as e:
    print(f"✗ Streamlit import failed: {e}")
print()

# 10. SYNTAX CHECK ON KEY FILES
print("10. SYNTAX VALIDATION")
print("-" * 80)
import ast

files_to_check = [
    'app.py',
    'router.py',
    'components/ai_assistant_toggle.py',
    'components/footer.py',
    'pages/home.py'
]

for file_path in files_to_check:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            ast.parse(code)
            print(f"✓ {file_path} - Valid Python syntax")
    except SyntaxError as e:
        print(f"✗ {file_path} - SYNTAX ERROR at line {e.lineno}: {e.msg}")
    except FileNotFoundError:
        print(f"✗ {file_path} - FILE NOT FOUND!")
    except Exception as e:
        print(f"✗ {file_path} - Error: {e}")
print()

# 11. SUMMARY
print("=" * 80)
print("SUMMARY")
print("=" * 80)

if import_errors:
    print(f"\n⚠ FOUND {len(import_errors)} IMPORT ERRORS:")
    for module_name, display_name, error_msg in import_errors:
        print(f"\n  • {display_name} ({module_name})")
        print(f"    {error_msg}")
else:
    print("\n✓ All imports successful!")

print("\n" + "=" * 80)
print("DEBUG REPORT COMPLETE")
print("=" * 80)
