#!/usr/bin/env python3
"""
WCAG Color Contrast Ratio Checker
==================================

Calculate and verify WCAG 2.1 contrast ratios for text/background color combinations.

Usage:
    python contrast_checker.py

WCAG Standards:
    - AA Normal Text: 4.5:1 minimum
    - AA Large Text: 3.0:1 minimum (18pt+ or 14pt+ bold)
    - AAA Normal Text: 7.0:1 minimum
    - AAA Large Text: 4.5:1 minimum

Author: Generated for douglascuthbertson.com accessibility improvements
Date: 2025-11-25
"""

import sys


def hex_to_rgb(hex_color):
    """
    Convert hex color to RGB tuple (0-255 range).

    Args:
        hex_color: String like "#ffffff" or "ffffff"

    Returns:
        Tuple of (r, g, b) values in 0-255 range
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_luminance(r, g, b):
    """
    Calculate relative luminance from RGB values.

    Uses WCAG 2.1 formula for relative luminance calculation.

    Args:
        r, g, b: RGB values in 0-255 range

    Returns:
        Float: Relative luminance (0.0 to 1.0)
    """
    # Convert to 0-1 range
    r, g, b = r / 255, g / 255, b / 255

    # Linearize each channel
    def linearize(val):
        if val <= 0.03928:
            return val / 12.92
        else:
            return ((val + 0.055) / 1.055) ** 2.4

    r = linearize(r)
    g = linearize(g)
    b = linearize(b)

    # Calculate luminance using WCAG formula
    # These coefficients account for human perception of different colors
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1, color2):
    """
    Calculate WCAG contrast ratio between two hex colors.

    Args:
        color1, color2: Hex color strings (e.g., "#ffffff" or "ffffff")

    Returns:
        Float: Contrast ratio (1.0 to 21.0)
    """
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)

    l1 = rgb_to_luminance(r1, g1, b1)
    l2 = rgb_to_luminance(r2, g2, b2)

    # Ensure l1 is the lighter color
    if l1 < l2:
        l1, l2 = l2, l1

    # Calculate contrast ratio using WCAG formula
    ratio = (l1 + 0.05) / (l2 + 0.05)
    return ratio


def check_wcag_compliance(ratio):
    """
    Check WCAG compliance levels for a given contrast ratio.

    Args:
        ratio: Float contrast ratio

    Returns:
        Dict with compliance information
    """
    return {
        'aa_normal': ratio >= 4.5,
        'aa_large': ratio >= 3.0,
        'aaa_normal': ratio >= 7.0,
        'aaa_large': ratio >= 4.5,
    }


def format_compliance(ratio):
    """
    Format compliance status as a readable string.

    Args:
        ratio: Float contrast ratio

    Returns:
        String describing compliance levels
    """
    compliance = check_wcag_compliance(ratio)

    if compliance['aaa_normal']:
        return "AAA-normal, AAA-large (Excellent!)"
    elif compliance['aa_normal']:
        return "AA-normal, AAA-large (Good)"
    elif compliance['aaa_large']:
        return "AAA-large only (Marginal)"
    elif compliance['aa_large']:
        return "AA-large only (Fails normal text)"
    else:
        return "FAILS ALL WCAG STANDARDS"


def suggest_improvements(fg_color, bg_color, current_ratio):
    """
    Suggest color adjustments to improve contrast.

    Args:
        fg_color, bg_color: Hex color strings
        current_ratio: Current contrast ratio

    Returns:
        String with suggestions
    """
    compliance = check_wcag_compliance(current_ratio)

    if compliance['aaa_normal']:
        return "No improvements needed - excellent contrast!"

    suggestions = []

    if not compliance['aa_normal']:
        suggestions.append(f"CRITICAL: Fails WCAG AA for normal text (need 4.5:1, have {current_ratio:.2f}:1)")
        suggestions.append("  - Consider darkening foreground or lightening background")
        suggestions.append("  - Or use these colors only for large text (18pt+/14pt+ bold)")
    elif not compliance['aaa_normal']:
        suggestions.append(f"Good for AA, but short of AAA (need 7.0:1, have {current_ratio:.2f}:1)")
        suggestions.append("  - Optional: Darken foreground or lighten background for AAA")

    return "\n".join(suggestions) if suggestions else "No suggestions"


def print_separator(char="=", length=90):
    """Print a separator line."""
    print(char * length)


def analyze_color_pair(fg_name, fg_color, bg_name, bg_color, show_suggestions=True):
    """
    Analyze and print detailed information about a color pair.

    Args:
        fg_name: Name/description of foreground color
        fg_color: Foreground hex color
        bg_name: Name/description of background color
        bg_color: Background hex color
        show_suggestions: Whether to show improvement suggestions
    """
    ratio = contrast_ratio(fg_color, bg_color)
    compliance_str = format_compliance(ratio)

    print(f"\n{fg_name} ({fg_color}) on {bg_name} ({bg_color})")
    print(f"  Contrast Ratio: {ratio:.2f}:1")
    print(f"  Compliance: {compliance_str}")

    if show_suggestions:
        suggestions = suggest_improvements(fg_color, bg_color, ratio)
        if suggestions and "No improvements needed" not in suggestions:
            print(f"  Suggestions: {suggestions}")


def test_victorian_blog_colors():
    """
    Test the current Victorian Newspaper blog color combinations.
    """
    print_separator()
    print("VICTORIAN NEWSPAPER BLOG - CURRENT COLOR COMBINATIONS")
    print_separator()

    # Define current color combinations from the blog
    combinations = [
        ("Body text", "#000000", "Victorian cream", "#ebe8e0"),
        ("Body text", "#000000", "Content area", "#f5f5f0"),
        ("Links", "#24599d", "Victorian cream", "#ebe8e0"),
        ("Links", "#24599d", "Content area", "#f5f5f0"),
        ("Link hover", "#a32c25", "Victorian cream", "#ebe8e0"),
        ("Code text", "#000000", "Code background", "#e2ded7"),
        ("Navigation", "#2a2a2a", "Nav background", "#f5f5f0"),
        ("Sidebar header", "#1a1a1a", "Sidebar bg", "#f5f5f0"),
        ("Victorian tag", "#333333", "Tag background", "#e8e5dd"),
        ("Skip link", "#ffffff", "Skip bg", "#24599d"),
        ("Table header (white)", "#ffffff", "Table header bg", "#697b92"),
        ("Table header (black)", "#000000", "Table header bg", "#697b92"),
    ]

    for fg_name, fg_color, bg_name, bg_color in combinations:
        analyze_color_pair(fg_name, fg_color, bg_name, bg_color, show_suggestions=False)

    print()
    print_separator()


def interactive_mode():
    """
    Interactive mode for testing custom color combinations.
    """
    print_separator()
    print("INTERACTIVE COLOR CONTRAST CHECKER")
    print_separator()
    print("\nEnter color pairs to test (or 'q' to quit)")
    print("Format: Hex colors like 'ffffff' or '#ffffff'\n")

    while True:
        try:
            fg = input("\nForeground color (text): ").strip()
            if fg.lower() in ('q', 'quit', 'exit'):
                break

            bg = input("Background color: ").strip()
            if bg.lower() in ('q', 'quit', 'exit'):
                break

            print_separator("-")
            analyze_color_pair("Text", fg, "Background", bg, show_suggestions=True)
            print_separator("-")

        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter valid hex colors (e.g., 'ffffff' or '#ffffff')")


def batch_test_mode(color_pairs):
    """
    Test a batch of color combinations.

    Args:
        color_pairs: List of tuples (fg_name, fg_color, bg_name, bg_color)
    """
    print_separator()
    print("BATCH COLOR CONTRAST ANALYSIS")
    print_separator()

    for fg_name, fg_color, bg_name, bg_color in color_pairs:
        analyze_color_pair(fg_name, fg_color, bg_name, bg_color)

    print()
    print_separator()


def main():
    """
    Main function - displays menu and handles user choice.
    """
    # If colors provided as command-line arguments, test them directly
    if len(sys.argv) >= 3:
        print("\n" + "=" * 90)
        print(" " * 25 + "WCAG CONTRAST RATIO CHECKER")
        print("=" * 90)
        fg = sys.argv[1]
        bg = sys.argv[2]
        analyze_color_pair("Text", fg, "Background", bg, show_suggestions=True)
        print()
        return

    print("\n" + "=" * 90)
    print(" " * 25 + "WCAG CONTRAST RATIO CHECKER")
    print("=" * 90)
    print("\nOptions:")
    print("  1. Test Victorian Blog current colors")
    print("  2. Interactive mode (test custom colors)")
    print("  3. Example: Test alternative color schemes")
    print("  q. Quit")
    print("\nTip: You can also run: python contrast_checker.py <fg-color> <bg-color>")

    choice = input("\nSelect option (1-3 or q): ").strip()

    if choice == '1':
        test_victorian_blog_colors()

    elif choice == '2':
        interactive_mode()

    elif choice == '3':
        # Example alternative color schemes to test
        print("\nTesting alternative color schemes...\n")
        alternatives = [
            ("Darker link", "#1a4570", "Victorian cream", "#ebe8e0"),
            ("Lighter bg", "#f8f8f5", "Body text", "#000000"),
            ("Warmer accent", "#8b4513", "Content area", "#f5f5f0"),
            ("Navy blue link", "#003366", "Victorian cream", "#ebe8e0"),
        ]
        batch_test_mode(alternatives)

    elif choice.lower() in ('q', 'quit', 'exit'):
        print("\nExiting...")

    else:
        print("\nInvalid option. Please try again.")
        main()


if __name__ == "__main__":
    main()
