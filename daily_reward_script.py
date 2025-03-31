from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def claim_daily_reward():
    # Chrome options for headless browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Setup webdriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the website
        driver.get("https://pay-va.nvsgames.com/topup/262304/ph-en?is_new_user=0&tab=purchase")
        
        # Wait and click Free Draw button
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
    
    except Exception as e:
        print(f"Error claiming reward: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    claim_daily_reward()
