from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def claim_daily_reward():
    # Chrome options for headless browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Setup webdriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the website
        driver.get("https://pay-va.nvsgames.com/topup/262304/ph-en?is_new_user=0&tab=purchase")
        
        # Wait for page to load
        time.sleep(3)
        
        # Find and enter player ID using the ID selector
        player_id_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "role_id_input"))
        )
        player_id_field.clear()
        player_id_field.send_keys("MattSwans#21334")
        
        # Click Confirm button - using multiple selector strategies for reliability
        try:
            # First try by direct button selector
            confirm_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#role_id > div > div > span > span > span > div > button"))
            )
            confirm_button.click()
        except:
            # Fallback to XPath if CSS selector fails
            try:
                confirm_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='role_id']/div/div/span/span/span/div/button"))
                )
                confirm_button.click()
            except:
                # Last resort - try to find any button with "Confirm" text
                confirm_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Confirm')]"))
                )
                confirm_button.click()
        
        # Wait for authentication to process
        time.sleep(3)
        
        # Take screenshot after login for debugging
        driver.save_screenshot("after_login.png")
        
        # Wait and click Free Draw button
        try:
            free_draw_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#signInLottery > div > div.index__drawButton--ZO0Zn"))
            )
            free_draw_button.click()
        except Exception as e:
            print(f"Error finding Free Draw button: {e}")
            driver.save_screenshot("free_draw_error.png")
            # Try scrolling to find the button
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.save_screenshot("after_scroll.png")
            # Try again
            free_draw_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#signInLottery > div > div.index__drawButton--ZO0Zn"))
            )
            free_draw_button.click()
        
        # Wait and click "Let's Go!" claim button
        claim_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".LuckDrawModal__jumpBtn--jV9z6"))
        )
        claim_button.click()
        
        print("Daily reward claimed successfully!")
        driver.save_screenshot("reward_claimed.png")
        
    except Exception as e:
        print(f"Error claiming reward: {e}")
        driver.save_screenshot("error_state.png")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    claim_daily_reward()
