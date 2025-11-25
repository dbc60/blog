# Contrast Checker Script

Python script for calculating WCAG 2.1 color contrast ratios to ensure accessibility compliance.

## Usage

### Quick Test (Command Line)

Test any two colors directly:

```bash
python contrast_checker.py '#000000' '#ebe8e0'
```

Output:
```
Text (#000000) on Background (#ebe8e0)
  Contrast Ratio: 17.15:1
  Compliance: AAA-normal, AAA-large (Excellent!)
```

### Interactive Menu

Run without arguments to see the menu:

```bash
python contrast_checker.py
```

**Options:**
1. **Test Victorian Blog current colors** - Tests all 12 color combinations currently used
2. **Interactive mode** - Enter colors one pair at a time
3. **Example alternative schemes** - See suggestions for alternative color palettes

### Examples

**Test if a darker link color works:**
```bash
python contrast_checker.py '#1a4570' '#ebe8e0'
# Result: 8.06:1 (AAA ✓✓ - even better than current!)
```

**Test a potential gray accent:**
```bash
python contrast_checker.py '#888888' '#ebe8e0'
# Result: 2.90:1 (FAILS - too light)
```

**Test alternative backgrounds:**
```bash
python contrast_checker.py '#000000' '#f8f8f5'
# Result: 19.68:1 (AAA ✓✓ - excellent)
```

## WCAG Standards

The script checks against these standards:

| Level | Normal Text | Large Text (18pt+/14pt+ bold) |
|-------|-------------|-------------------------------|
| **AA** | 4.5:1 | 3.0:1 |
| **AAA** | 7.0:1 | 4.5:1 |

## Features

- ✓ Calculates exact WCAG 2.1 contrast ratios
- ✓ Tests compliance for AA and AAA levels
- ✓ Provides suggestions for failing colors
- ✓ Batch testing for multiple color pairs
- ✓ Interactive mode for experimentation
- ✓ Pre-loaded with Victorian blog colors

## Current Blog Results

Running option 1 shows all current color combinations:

- **Excellent (AAA ✓✓):** Body text, navigation, headers, tags, code blocks (10.04:1 - 19.20:1)
- **Good (AA ✓):** Links, link hover (5.73:1 - 6.52:1)
- **Marginal (⚠):** White on table headers (4.33:1 - AA-large only)

## Dependencies

- Python 3.6+
- No external libraries required (uses standard library only)

## Tips

### Finding the Right Color

If a color fails WCAG:

1. **For text:** Darken it by reducing the hex values
   - `#888888` → `#666666` → `#444444`

2. **For backgrounds:** Lighten it by increasing the hex values
   - `#e0e0e0` → `#f0f0f0` → `#f8f8f8`

3. **Test incrementally:** Use the command line mode to quickly iterate
   ```bash
   python contrast_checker.py '#666666' '#ebe8e0'
   python contrast_checker.py '#555555' '#ebe8e0'
   python contrast_checker.py '#444444' '#ebe8e0'
   ```

### Color Picker Integration

Use with online color pickers:
1. Pick a color in your browser's DevTools or at [colorhexa.com](https://www.colorhexa.com/)
2. Copy the hex code
3. Test immediately: `python contrast_checker.py '#yourcolor' '#background'`

## License

Created for douglascuthbertson.com accessibility improvements (2025-11-25)
Free to use and modify for accessibility testing.
