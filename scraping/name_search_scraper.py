from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search_and_extract(driver):
    results = []

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(f"\n========== 🔍 正在抓取字母: {letter} ==========")

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "n"))
        )
        name_input.clear()
        name_input.send_keys(letter)
        search_button = driver.find_element(By.CSS_SELECTOR, "button.ws-form__submit-btn")
        search_button.click()

        while True:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.search-results__results"))
                )
            except Exception:
                print("[WARN] 页面结果未能加载")

            time.sleep(1)
            results_area = driver.find_element(By.CSS_SELECTOR, "div.search-results__results")
            page_text = results_area.text.strip()

            print("\n========== 页面文本如下 ==========")
            print(page_text)
            print("========== ✅ 页面数据输出完成 ==========")

            results.append(page_text)

            try:
                pagination_buttons = driver.find_elements(By.CSS_SELECTOR, "a.ws-pagination__nav")
                found_next = False
                for btn in pagination_buttons:
                    try:
                        span = btn.find_element(By.TAG_NAME, "span")
                        if "icon-chevron-right" in span.get_attribute("class"):
                            btn.click()
                            time.sleep(1)
                            found_next = True
                            break
                    except:
                        continue
                if not found_next:
                    print("[INFO] 没有找到下一页按钮，可能是最后一页")
                    break
            except Exception as e:
                print(f"[WARN] 翻页失败：{e}")
                break

    print("\n✅ 所有 A-Z 页面抓取完毕，准备关闭浏览器并保存数据...")
    driver.quit()
    return results