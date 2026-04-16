import os
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

def take_screenshot():
    # 1. Setup folder and filename
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filepath = os.path.join(output_dir, f"screenshot_{timestamp}.png")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        # We'll use a standard 1080p viewport
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        
        page = context.new_page()

        # Stealth: Hide automation
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        print(f"Opening website...")
        # CHANGE THE URL BELOW
        page.goto("https://globalsumudflotilla.org/tracker/", wait_until="networkidle")
        
        # --- THE ZOOM LOGIC ---
        # 0.6 = 60% zoom. Change this to 0.5 for more zoom out, or 0.8 for less.
        zoom_level = 0.6 
        print(f"Setting zoom to {int(zoom_level * 100)}%...")
        page.evaluate(f"document.body.style.zoom = '{zoom_level}'")
        
        print("Waiting 45 seconds for content to settle...")
        time.sleep(45) 
        
        print(f"Saving zoomed-out screenshot: {filepath}")
        # 'full_page=False' takes just the visible area. 
        # Change to 'True' if you want the entire scrolling length of the site.
        page.screenshot(path=filepath, full_page=False)
        
        browser.close()
        print("Done!")

if __name__ == "__main__":
    take_screenshot()
