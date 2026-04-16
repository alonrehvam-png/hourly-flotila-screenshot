from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def take_screenshot():
    with sync_playwright() as p:
        # We sometimes need to run headless=False or use a different browser channel to bypass strict checks, 
        # but GitHub Actions requires headless. Let's try stealth first.
        browser = p.chromium.launch(headless=True)
        
        # Adding user agent info makes it look more like a real computer
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # Apply stealth mechanics to hide the fact that this is Playwright
        stealth_sync(page)
        
        print("Loading website...")
        page.goto("https://example.com") # REMEMBER TO CHANGE THIS
        
        print("Waiting 30 seconds...")
        page.wait_for_timeout(30000)
        
        print("Taking screenshot...")
        page.screenshot(path="screenshot.png")
        
        browser.close()
        print("Done!")

if __name__ == "__main__":
    take_screenshot()
