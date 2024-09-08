from .scrape import *
from email_excp.constants import *
from email_excp.send_email import *



class ScrapeDigikala(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)
             

    def scrape_price(self,soup):
        price = None
        try:
            page = soup.find('div',class_ = 'grow min-w-0')
            page_detail = page.find('div',class_ = 'styles_InfoSection__leftSection__0vNpX')
            page_price = page_detail.find('div',class_ = 'relative w-full lg:px-4 lg:pb-2')
            price_pr = page_price.find('div',class_ = 'flex items-center justify-end w-full gap-1').text

            price = convert_numbers.persian_to_english(price_pr)+'0' 

        except Exception as price_exception:
            print(str(price_exception))
        return price


    def scrape_warranty(self,soup):
        warranty = None
        try:
            page = soup.find('div',class_ = 'grow min-w-0')
            warranty = page.find('div',class_ = 'w-full px-4 flex items-center').text

        except Exception as warranty_exception:
            print(warranty_exception)
        
        return warranty

    def scrape_seller(self,soup):
        seller = None
        try:
            page = soup.find('div',class_ = 'grow min-w-0')
            detail_page = page.find('div',class_ = 'py-3 flex grow flex pt-0 pb-4')
            seller_page = detail_page.find('div',class_ = 'flex items-center mb-2 lg:mb-1')
            seller = seller_page.find('p',class_ = 'text-neutral-700 ml-2 text-subtitle').text

        except Exception as seller_exception:
            pass

        return seller


    
    #def fix_url(self, url):
    #    try:
    #        url = url.replace('www', 'api')
    #        url = url.replace('dkp-', '')
    #        count = 0
    #        length = 0
    #        for i in range(len(url)):
    #            if url[i] == '/':
    #                count += 1
    #            length += 1
    #            if count == 5:
    #                break
    #        url = url[0:length]
    #        count = 0
    #        length = 0
    #        for x in range(len(url)):
    #            if url[x] == '/':
    #                count += 1
    #            length += 1
    #            if count == 3:
    #                break
    #        url = url[0:length] + 'v1/' + url[length:]
    #        return url
    #    except Exception as e:
    #        pass
#

    def scrape_all_data(self):
        try:
            soup = BeautifulSoup(self.driver.page_source , 'html.parser')
            scraped_data = {
                'price': self.scrape_price(soup),
                #'rate': self.scrape_rate(),
                'warranty': self.scrape_warranty(soup),
                'seller': self.scrape_seller(soup),
                #'colors': self.scrape_colors(),
            }
            price = scraped_data['price']
            if price is not None and price !='':
                df = pd.DataFrame([scraped_data], index=[None])
                return df
            else:
                return None
        except Exception as e:
            print(str(e))

