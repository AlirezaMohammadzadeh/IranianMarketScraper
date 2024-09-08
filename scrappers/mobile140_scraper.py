from .scrape import *
from email_excp.constants import *
from email_excp.send_email import *



class ScrapeMobile140(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)

    def scrape_price(self):
        price_pr = self.scrape_by_class_name('single__product__price--new').text
        if price_pr is not None:
            price_en = convert_numbers.persian_to_english(price_pr)+'0' 
            return price_en
        else:
            return None
        

    def scrape_warranty(self):
        warranty = self.scrape_by_class_name('single__product__guarantee')
        if warranty is not None:
            return warranty.text
        else:
            return ''

    def scrape_all_data(self):
        try:
            # Create a list to store the scraped data for each shop
            scraped_data_list = [] 
            scraped_data = {
                    'price': self.scrape_price(),
                    'warranty': self.scrape_warranty(),
                    'seller': 'mobile140',
                }
            scraped_data_list.append(scraped_data)
            # Convert the list of dictionaries to a pandas DataFrame
            if len(scraped_data_list) == 0:
                return None
            else:
                df = pd.DataFrame(scraped_data_list, index=range(len(scraped_data_list)))
                return df
            
        except Exception as e:
            pass