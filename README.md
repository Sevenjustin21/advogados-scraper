\# 🕵️ Advogados Scraper



A modular Python project that extracts Portuguese lawyer data from \[portal.oa.pt](https://portal.oa.pt/advogados/pesquisa-de-advogados/) and exports it to a structured Excel file.



---



\## 🚀 Features



\- Automated browser control with Selenium

\- Iterative A–Z search with pagination support

\- Text extraction saved to `.txt`

\- TXT parsing and transformation to `.xlsx`

\- Modular file structure for scalability and maintainability



---



\## 📂 Project Structure



over\_project/

├── main.py

├── scraping/

│ ├── browser\_setup.py

│ ├── name\_search\_scraper.py

│ ├── save\_raw\_text.py

├── parsing/

│ └── txt\_to\_excel.py

├── utils/

│ └── excel\_helper.py

├── data/

│ ├── advogados\_raw.txt

│ └── advogados\_ativos.xlsx





---



\## 🛠 Installation



```bash

pip install -r requirements.txt

If requirements.txt not yet available, manually install:



pip install selenium openpyxl





▶️ Usage

1\.Run the script:



python main.py



2\.Manually complete CAPTCHA in the browser when prompted.



3\.After the full A–Z extraction, the following files will be generated:



* data/advogados\_raw.txt



* data/advogados\_ativos.xlsx



🧠 Tech Stack

* Python 3.10+
* Selenium (ChromeDriver)
* openpyxl



📄 License

This project is licensed under the MIT License.



\### ✅

