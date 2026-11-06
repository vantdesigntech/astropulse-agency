import os
from playwright.sync_api import sync_playwright

html_path = os.path.abspath(r"E:\WEBS\astropulse-agency\index.html")
file_url = f"file:///{html_path.replace(os.sep, '/')}"
output_dir = r"E:\WEBS\astropulse-agency"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # Desktop viewport matching the reference (1440px wide)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    print(f"Loading {file_url}...")
    page.goto(file_url, wait_until="networkidle")
    page.wait_for_timeout(1000)

    # 1. Capture Hero Section
    page.screenshot(path=os.path.join(output_dir, "verify_hero.png"), full_page=False)
    print("Saved verify_hero.png")

    # 2. Capture Full Page
    page.screenshot(path=os.path.join(output_dir, "verify_full.png"), full_page=True)
    print("Saved verify_full.png")

    # 3. Mobile Viewport (iPhone 14 / 390px)
    page.set_viewport_size({"width": 390, "height": 844})
    page.wait_for_timeout(500)
    page.screenshot(path=os.path.join(output_dir, "verify_mobile.png"), full_page=False)
    print("Saved verify_mobile.png")

    browser.close()
    print("Verification screenshots captured!")
