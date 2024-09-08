from scrappers.scrape import *
from email_excp.constants import *
from email_excp.send_email import *
import re



class ScrapeTechnolife(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)

    def scrape_price(self):
        temp = self.scrape_by_Xpath('//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div').text
        if temp is not None:
            lines = temp.strip().split('\n')
            # Access the third line from the last
            price_pr = lines[-3]
            if price_pr is not None:
                price_en = convert_numbers.persian_to_english(price_pr)+'0'
                return price_en
            else:
                return None
        else:
            return None

    def scrape_warranty(self):
        temp = self.scrape_by_Xpath('//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div').text
        if temp is not None:
            # Regular expression to find the line containing the word "گارانتی"
            pattern = re.compile(r'^.*گارانتی.*$', re.MULTILINE)
            # Find all lines that match the pattern
            matches = pattern.findall(temp)
            if matches[0] is not None:
                return matches[0]
            else:
                return None
        else:
            return None

    def scrape_all_data(self):
        try:
            # Create a list to store the scraped data for each shop
            scraped_data_list = [] 
            scraped_data = {
                    'price': self.scrape_price(),
                    'warranty': self.scrape_warranty(),
                    'seller': 'technolife',
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