from scrappers.scrape import *
from email_excp.constants import *
from email_excp.send_email import *


class ScrapeHamrahtel(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)

    def scrape_price(self):
        temp = self.scrape_by_Xpath('//*[@id="__next"]/main/section/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div/div/div').text
        if temp is not None:
            lines_with_toman = [line for line in temp.split('\n') if 'تومان' in line]
            if len(lines_with_toman)>0:
                price_pr = lines_with_toman[len(lines_with_toman)-1]
                price_en = convert_numbers.persian_to_english(price_pr)+'0'
                return price_en
            else:
                return None
        else:
            return None

    def scrape_warranty(self):
        pass

    def scrape_all_data(self):
        try:
            # Create a list to store the scraped data for each shop
            scraped_data_list = [] 
            scraped_data = {
                    'price': self.scrape_price(),
                    'warranty': None,
                    'seller': 'hamrahtel',
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