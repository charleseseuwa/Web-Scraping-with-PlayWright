
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #<--- set the browser. Chrome = Chromiun. Set Headless = false to see our work
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.nytimes.com/books/best-sellers/hardcover-nonfiction/',
    timeout=0) #<--- website to scrap
    # page.screenshot(path = 'New_York_Time_Best_Seller.png')  #<-- Take a quick screenshot of the webpage we're trying to scrap
    articles = page.locator('ol[data-testid="topic-list"]')

    with open('articles.html', 'w+', encoding='utf-8') as f:
        f.write(articles.inner_html())
    browser.close()