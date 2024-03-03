import requests
from bs4 import BeautifulSoup

def get_ebay_product_details(url):
    # Fetch HTML content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch page")
        return

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product details
    #title_elem = soup.find('h1', {'class': 'it-ttl'})
    #if title_elem:
     #   title = title_elem.text.strip()
   # else:
     #   title = "Title not found"

    desc_elem = soup.find('div', {'class': 'ux-layout-section-evo__item'})
    if desc_elem:
        description = desc_elem.text.strip()
    else:
        description = "Description not found"

    # Print product details in a human-readable format
    print("Product Title:")
    #print(title)
    print("\nProduct Description:")
    print(description)

# Example usage
url = "https://www.ebay.com/itm/394587291482?epid=2301759852&itmmeta=01HQYZVQ0B1J2E2E1X13P6RSDB&hash=item5bdf3c3f5a%3Ag%3APAEAAOSwDB9ln1p0&itmprp=enc%3AAQAIAAABEEGN6c9tllV%2FgS%2BiRXfjZ9Q5Dy4hxtQKOLokZ16AUc%2BrvmqOoDK%2FjUSAuzhclrVxoTpBOmt4fWGL4OJTKfbDAGVkz9n1Lsl0RgTKbNtY8qfSj%2BWyBCWuCD%2B24eEVq4XhK1E3nn1hxT8K07FWXYPMWbJ2scX21%2FBLSnP45%2FVs9RZYw%2FkC79kTsk4%2FneLUq7wfzruIP8qHCJJHS3cG1SRZqIpF%2FoOWWzF63BGdNIHWFZj%2B5vmP%2B3AKxsmKeXpvU870f1Dr8fHWlil9%2Feys8BF2IQ14Nk1URlDjd%2BVNjyU8tIO9E%2FJouUzCZhK2lwjOJGIN%2FwWLR1eV4WwVfrY4VZjgb%2BlMkatJxQhgisyuNaQyflyR%7Ctkp%3ABFBMnPDu379j&LH_BIN=1"
get_ebay_product_details(url)

