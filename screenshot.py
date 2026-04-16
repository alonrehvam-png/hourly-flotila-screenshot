import os
from datetime import datetime
from playwright.sync_api import sync_playwright
import playwright_stealth

def take_screenshot():
    # 1. Create the 'output' folder if it doesn't already exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Generate a filename based on the current date and time
    # Format: 2026-04-16_16-45-00.png
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # Apply stealth (using a more robust import style to avoid the error)
        playwright_stealth.stealth_sync(page)
        
        print(f"Navigating to website...")
        # REPLACE THE URL BELOW
        page.goto("https://globalsumudflotilla.org/tracker/") 
        
        print("Waiting 30 seconds for content to load...")
        page.wait_for_timeout(30000)
        
        print(f"Saving screenshot to {filepath}...")
        page.screenshot(path=filepath)
        
        browser.close()
        print("Done!")

if __name__ == "__main__":
    take_screenshot()
