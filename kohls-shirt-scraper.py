from bs4 import BeautifulSoup
import requests

def scrape_kohls_shirts(num_shirts):
    count = 0

    while count < num_shirts:
        html_text = requests.get("https://www.kohls.com/catalog/mens-button-down-shirts-tops-" +
            "clothing.jsp?CN=Gender:Mens+Silhouette:Button-Down%20Shirts+Category:Tops+Department:" +
            "Clothing&cc=mens-TN3.0-S-buttondownshirts&kls_sbp=56751120711696885714221506018546775523" +
            f"&PPP=48&WS={count}&S=1&sks=true").text
        soup = BeautifulSoup(html_text, 'lxml')

        shirts = soup.find_all('li', class_="products_grid")

        if len(shirts) == 0:
            print('All out of shirts!')
            return

        for shirt in shirts:
            count += 1
            title = shirt.find('p').text.strip()
            price = None

            if shirt.find('span', class_="prod_price_amount red_color"):
                price = shirt.find('span', class_="prod_price_amount red_color").text
            else:
                price = shirt.find('span', class_="prod_price_amount").text

            print(f"{count}: {title} costs {price}!\n")

            if count == num_shirts:
                return

scrape_kohls_shirts(400)