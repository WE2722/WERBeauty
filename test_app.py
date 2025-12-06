"""
Test script for WERBEAUTY application
Verifies all key functionality and modules
"""

import sys

def test_imports():
    """Test all module imports"""
    print("\n=== Testing Imports ===")
    try:
        from utils.cart_manager import get_cart, add_to_cart, remove_from_cart, update_quantity, get_cart_total, is_in_cart
        print("✓ cart_manager: All functions imported")
        
        from utils.animation import render_success_animation, get_animation_css, get_loading_skeleton
        print("✓ animation: All functions imported")
        
        from utils.favorites_manager import get_favorites, add_to_favorites, remove_from_favorites, is_favorite
        print("✓ favorites_manager: All functions imported")
        
        from utils.product_loader import load_women_products, load_men_products, get_product_by_id, filter_products
        print("✓ product_loader: All functions imported")
        
        from utils.helpers import format_price, generate_order_id, validate_email, validate_card_number
        print("✓ helpers: All functions imported")
        
        from utils.recommendation_engine import get_recommendations, get_trending, get_similar_products
        print("✓ recommendation_engine: All functions imported")
        
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False


def test_pages():
    """Test all page imports"""
    print("\n=== Testing Pages ===")
    try:
        from pages import home, women, men, cart, favorites, payment, recommended
        print("✓ All pages imported successfully")
        
        # Verify each page has render function
        for page_name, page_module in [("home", home), ("women", women), ("men", men), 
                                       ("cart", cart), ("favorites", favorites), 
                                       ("payment", payment), ("recommended", recommended)]:
            if hasattr(page_module, 'render'):
                print(f"  ✓ {page_name}.render() exists")
            else:
                print(f"  ✗ {page_name}.render() missing!")
                return False
        
        return True
    except Exception as e:
        print(f"✗ Page import error: {e}")
        return False


def test_components():
    """Test all component imports"""
    print("\n=== Testing Components ===")
    try:
        from components.navbar import render_navbar
        print("✓ navbar imported")
        
        from components.footer import render_footer
        print("✓ footer imported")
        
        from components.product_card import render_product_card, render_product_grid
        print("✓ product_card imported")
        
        from components.filters_panel import render_filters_panel
        print("✓ filters_panel imported")
        
        from components.ai_assistant_toggle import render_ai_assistant
        print("✓ ai_assistant_toggle imported")
        
        from components.onboarding_gender_selector import render_onboarding
        print("✓ onboarding_gender_selector imported")
        
        return True
    except Exception as e:
        print(f"✗ Component import error: {e}")
        return False


def test_utility_functions():
    """Test utility functions work correctly"""
    print("\n=== Testing Utility Functions ===")
    try:
        from utils.helpers import format_price, generate_order_id, validate_email, validate_card_number
        
        # Test format_price
        price = format_price(99.99)
        assert price == "$99.99", f"Expected $99.99, got {price}"
        print("✓ format_price() works correctly")
        
        # Test generate_order_id
        order_id = generate_order_id()
        assert order_id.startswith("WER-"), f"Order ID should start with WER-, got {order_id}"
        print(f"✓ generate_order_id() works: {order_id}")
        
        # Test validate_email
        assert validate_email("test@example.com") == True
        assert validate_email("invalid-email") == False
        print("✓ validate_email() works correctly")
        
        # Test validate_card_number
        assert validate_card_number("4532015112830366") == True  # Valid test card
        assert validate_card_number("1234567890123456") == False  # Invalid
        print("✓ validate_card_number() works correctly")
        
        return True
    except Exception as e:
        print(f"✗ Utility function error: {e}")
        return False


def test_product_loading():
    """Test product loading functions"""
    print("\n=== Testing Product Loading ===")
    try:
        from utils.product_loader import load_women_products, load_men_products
        
        women_products = load_women_products()
        print(f"✓ Loaded {len(women_products)} women's products")
        
        men_products = load_men_products()
        print(f"✓ Loaded {len(men_products)} men's products")
        
        # Verify product structure
        if women_products:
            sample = women_products[0]
            required_keys = ['id', 'name', 'price', 'category']
            for key in required_keys:
                if key not in sample:
                    print(f"  ✗ Missing key '{key}' in product")
                    return False
            print("✓ Product structure is valid")
        
        return True
    except Exception as e:
        print(f"✗ Product loading error: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("WERBEAUTY Application Test Suite")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Pages", test_pages()))
    results.append(("Components", test_components()))
    results.append(("Utility Functions", test_utility_functions()))
    results.append(("Product Loading", test_product_loading()))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All tests passed! Application is ready.")
        print("=" * 60)
        print("\n🚀 Start the app with: streamlit run app.py")
        print("📱 Then open: http://localhost:8501")
        return 0
    else:
        print("❌ Some tests failed. Please review errors above.")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
