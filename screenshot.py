import os
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

def take_screenshot():
    # 1. Create the 'output' folder if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Set up the timestamped filename
    # Example: screenshot_2026-04-16_17-00.png
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filepath = os.path.join(output_dir, f"screenshot_{timestamp}.png")

    with sync_playwright() as p:
        # We add an 'argument' that tells Chrome NOT to announce it's a bot
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        # We create a 'context' that mimics a real Windows PC
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        
        page = context.new_page()

        # Final 'stealth' trick: manually set the webdriver property to undefined
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        print(f"Opening website...")
        # CHANGE THE URL BELOW TO YOUR TARGET
        page.goto("https://globalsumudflotilla.org/tracker/", wait_until="networkidle")
        
        print("Waiting 45 seconds for everything to settle...")
        time.sleep(45) 
        
        print(f"Taking screenshot: {filepath}")
        page.screenshot(path=filepath, full_page=False)
        
        browser.close()
        print("Success!")

if __name__ == "__main__":
    take_screenshot()
