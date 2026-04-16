from playwright.sync_api import sync_playwright

def take_screenshot():
    # Start the Playwright browser
    with sync_playwright() as p:
        # Launch a hidden (headless) Chrome/Chromium browser
        browser = p.chromium.launch(headless=True)
        
        # Open a new tab and force a standard PC screen size
        page = browser.new_page(viewport={"width": 1920, "height": 1080}) 
        
        print("Loading website...")
        # REPLACE THE URL BELOW WITH YOUR TARGET WEBSITE
        page.goto("https://globalsumudflotilla.org/tracker/")
        
        print("Waiting 30 seconds for the page to fully load...")
        page.wait_for_timeout(30000) # 30,000 milliseconds = 30 seconds
        
        print("Taking screenshot...")
        page.screenshot(path="screenshot.png")
        
        # Close the browser
        browser.close()
        print("Done!")

if __name__ == "__main__":
    take_screenshot()
