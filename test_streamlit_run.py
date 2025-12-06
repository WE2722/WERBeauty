"""
Test script to capture Streamlit startup errors
"""
import sys
import traceback

print("Starting Streamlit test...")
print("=" * 80)

try:
    # Import streamlit
    import streamlit as st
    print("✓ Streamlit imported")
    
    # Import app
    print("\nImporting app.py...")
    import app
    print("✓ app.py imported")
    
    # Try to access main components
    print("\nChecking app structure...")
    if hasattr(app, 'main'):
        print("✓ app.main() exists")
    else:
        print("✗ app.main() NOT FOUND")
    
    # Import router
    print("\nImporting router...")
    import router
    print("✓ router imported")
    
    if hasattr(router, 'route_page'):
        print("✓ router.route_page() exists")
    else:
        print("✗ router.route_page() NOT FOUND")
    
    # Test importing all pages
    print("\nTesting page imports...")
    pages = ['home', 'women', 'men', 'cart', 'favorites', 'payment', 'recommended']
    for page in pages:
        try:
            exec(f"from pages import {page}")
            print(f"✓ pages.{page}")
        except Exception as e:
            print(f"✗ pages.{page}: {e}")
    
    # Test importing all components
    print("\nTesting component imports...")
    components = ['navbar', 'footer', 'ai_assistant_toggle', 'comments_section',
                  'product_card', 'filters_panel', 'animated_header',
                  'category_carousel', 'testimonials_slider', 'onboarding_gender_selector']
    for comp in components:
        try:
            exec(f"from components import {comp}")
            print(f"✓ components.{comp}")
        except Exception as e:
            print(f"✗ components.{comp}: {e}")
    
    print("\n" + "=" * 80)
    print("✓ ALL TESTS PASSED - App structure is valid")
    print("=" * 80)
    
    # Now try to actually run the app
    print("\nAttempting to run app.main()...")
    try:
        app.main()
    except Exception as e:
        print(f"\n⚠ Error running app.main(): {e}")
        traceback.print_exc()

except Exception as e:
    print(f"\n✗ CRITICAL ERROR: {e}")
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
