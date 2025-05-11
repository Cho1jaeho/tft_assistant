import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import json

options = uc.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko-KR"})
driver = uc.Chrome(options=options)

driver.get("https://www.metatft.com/comps")
time.sleep(5)

deck_blocks = driver.find_elements(By.CLASS_NAME, "CompRow")
results = {}

for deck in deck_blocks[:7]:
    try:
        # 덱 이름
        name = deck.find_element(By.CLASS_NAME, "Comp_Title").text.strip()

        # 아이템 추출
        item_imgs = deck.find_elements(By.CLASS_NAME, "Item_img")
        items = [img.get_attribute("alt") for img in item_imgs[:6]]

        # 저장
        results[name] = {
            "core_items": items
        }
    

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

# 저장
with open("data/decks.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ decks.json 저장 완료")
