from bs4 import BeautifulSoup
import requests

def scrape_auto_shops(num_shops):
    # Keep track of how many things have been scraped
    count = 0

    while count < num_shops:
        # Use f string to get the next page, starting with your current count
        html_text = requests.get(f"https://sacramento.craigslist.org/search/aos?s={count}").text
        soup = BeautifulSoup(html_text, 'lxml')

        shops = soup.find_all('li', class_="result-row")

        # If there are no more items, break out
        if len(shops) == 0:
            print("All out of shops!")
            return

        for shop in shops:
            # Add to count first, so print is right and if statement is right
            count += 1
            title = shop.find('a', class_="result-title hdrlnk").text

            # Need if else if there are variations, like sales or some things 
            # aren't always there
            if shop.find('span', class_="result-hood"):
                area = shop.find('span', class_="result-hood").text
                print(f'{count}: {title}\n{area}\n\n')
            else: 
                print(f'{count}: {title}\n\n')

            # Breaks out if you've hit the target number and there are still more
            if count == num_shops:
                return


scrape_auto_shops(1000)
