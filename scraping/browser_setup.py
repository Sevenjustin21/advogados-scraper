from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    url = "https://portal.oa.pt/advogados/pesquisa-de-advogados/"
    driver.get(url)
    driver.maximize_window()

    try:
        cookie_close_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ws-cookie-alert__close-btn"))
        )
        cookie_close_btn.click()
    except Exception:
        pass

    try:
        labels = driver.find_elements(By.TAG_NAME, "label")
        for label in labels:
            if "Apenas Activos" in label.text:
                driver.execute_script("arguments[0].scrollIntoView(true);", label)
                label.click()
                print("[INFO] 成功勾选 'Apenas Activos' 复选框")
                break
        else:
            print("[WARN] 页面上未找到 'Apenas Activos' 复选框标签")
    except Exception as e:
        print(f"[ERROR] 勾选 'Apenas Activos' 失败：{e}")

    print("请在打开的浏览器页面中勾选验证码（I'm not a robot），完成验证后返回此控制台并按 Enter 继续...")
    input()

    return driver