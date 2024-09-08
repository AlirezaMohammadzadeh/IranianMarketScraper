from .scrape import *
from email_excp.constants import *
from email_excp.send_email import *


class ScrapeEmalls(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)

    def find_shops(self):
        try:
            shop_list = self.find_elements_by_class_name('container top-detail')
            print(shop_list.text)
        except:
            return []
        return shop_list

    def emalls_fix_url(self, url):
        url = url.replace('%25','%')
        return url

    
    def get_row_details(self, row):
        shop_details = {
            'shop_name': None,
            'warranty': None,
        }
        try:
            temp_provider = row.find_element(By.CLASS_NAME, 'shop-logo-wrapper')
            shop_name = temp_provider.find_element(By.CLASS_NAME, 'shopnamespan').text.replace('\n', '')
            shop_details['shop_name'] = shop_name
        except Exception as e:
            pass
        
        try:
            temp_detail = row.find_element(By.CLASS_NAME, 'shop-prd-info')
            warranty = temp_detail.find_element(By.CLASS_NAME, 'guarantee')
            if warranty is not None:
                warranty_str = warranty.text.replace('\n', '')
                shop_details['warranty'] = warranty_str
        except Exception as e:
            send_email(str(e))
        
        return shop_details
    
    def get_shop_price(self, row):
        price_details = {
        'price': None,
        'discount_percent': None,
        'before_discount_price': None
        }   
        try:
            temp_price = row.find_element(By.CLASS_NAME, 'shop-price')
            price_str = temp_price.text 
            discount_percent=''
            before_discount_price=''
            try:
                discount_temp = temp_price.find_element(By.CLASS_NAME, 'shop-price-discount-box')
                discount_percent = discount_temp.find_element(By.CLASS_NAME, 'shop-price-discount').text
                before_discount_price = discount_temp.find_element(By.TAG_NAME, 'del').text
            except:
                pass
            price_str = price_str.replace(discount_percent, '')
            price_str = price_str.replace(before_discount_price, '')    
            price_details['price'] = convert_numbers.persian_to_english(price_str)
            price_details['discount_percent'] = discount_percent
            price_details['before_discount_price'] = before_discount_price
        except Exception as e:
            send_email(str(e))

        return price_details

    
    def click_emalls(self):
        try:
            more_button = self.driver.find_element(By.XPATH, '//*[@id="btnshowhide"]') 
            more_button.click()
        except Exceprtion as e:
            pass


    def scrape_all_data(self):
        try:
            #self.click_emalls()
            #get shop list
            shop_list = self.find_shops()
            # Create a list to store the scraped data for each shop
            scraped_data_list = []
            for shop in shop_list: 
                scraped_data = {
                    'price': self.get_shop_price(shop)['price'],
                    'warranty': self.get_row_details(shop)['warranty'],
                    'seller': self.get_row_details(shop)['shop_name'],
                }
                price = scraped_data['price']
                if price is not None and price !='':
                    scraped_data['price'] = toman_to_rial(price)
                    scraped_data_list.append(scraped_data)
            # Convert the list of dictionaries to a pandas DataFrame
            if len(scraped_data_list) == 0:
                return None
            else:
                df = pd.DataFrame(scraped_data_list, index=range(len(scraped_data_list)))
                return df
            
        except Exception as e:
            print(str(e))
            return None







  