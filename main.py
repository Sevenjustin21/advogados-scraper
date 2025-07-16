from scraping.browser_setup import init_browser
from scraping.name_search_scraper import search_and_extract
from scraping.save_raw_text import save_results
from parsing.txt_to_excel import parse_txt_to_excel

if __name__ == "__main__":
    driver = init_browser()
    results = search_and_extract(driver)
    save_results(results)
    parse_txt_to_excel()