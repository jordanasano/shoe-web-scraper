from bs4 import BeautifulSoup
import requests

def scrape_kohls_shorts(num_shorts):
    count = 0

    while count < num_shorts:
        html_text = requests.get("https://www.kohls.com/catalog/mens-shorts-" +
        "bottoms-clothing.jsp?CN=Gender:Mens+Product:Shorts+Category:Bottoms+Depa" +
        "rtment:Clothing&cc=mens-TN3.0-S-shorts&kls_sbp=56751120711696885714221" +
        f"506018546775523&PPP=48&WS={count}&S=1&sks=true").text

        soup = BeautifulSoup(html_text, 'lxml')

        shorts = soup.find_all('li', class_="products_grid")

        if len(shorts) == 0:
            print("All out of shorts!")
            return

        for short in shorts:
            count += 1
            title = short.find('p').text.strip()
            price = None

            if short.find("span", class_="prod_price_amount red_color"):
                price = short.find("span", class_="prod_price_amount red_color").text
            else:
                price = short.find("span", class_="prod_price_amount").text

            print(f"{count}: {title} costs {price}!")

            if count == num_shorts:
                return

scrape_kohls_shorts(3000)