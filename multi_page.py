from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False) #<--- set the browser. Chrome = Chromiun. Set Headless = false to see our work
    page = browser.new_page()
    page.goto('https://www.nytimes.com/books/best-sellers/hardcover-nonfiction/',
    timeout=0) #<--- website to scrap
   
    html_articles = []

    for i in range(3):
       articles = page.locator('section ol[data-testid="topic-list"]') #<-- Locate the html tag from the part of the website you want to scrap
       html_articles.append(articles.inner_html())
       page.locator('nav[aria-labelledby="best-sellers-navigation"] a ').nth(0).click() #<--- find all 'a' tag inside the 

    with open('all_articles.html', 'w+', encoding='utf-8') as f: #<-- create a new html file named all_articles.html
        full_html_articles = "".join(html_articles) #<-- join all html scrapped from pg. 1-3  in the html_articles list to one string
        f.write(full_html_articles)   #<-- then write joined htmls it to our file
    browser.close()