from .scrape import *
from email_excp.constants import *
from email_excp.send_email import *

class ScrapeTorob(WebScraper):
    def __init__(self, driver_path, options=None):
            super().__init__(driver_path, options)
        
    def scrape_price(self,shop):
        price = None
        try:
            class_name_purchase = 'purchase-info'
            sell_detail = shop.find_element_by_class_name(class_name_purchase)
            class_name_price = 'price'
            price = sell_detail.find_element_by_class_name(class_name_price).text
            price_en = convert_numbers.persian_to_english(price)
            return price_en
        except Exception as e:
            pass

    def scrape_warranty(self,shop):
        warranty_str = None
        try:
            class_name_warranty = 'product-description'
            warranty = shop.find_element_by_class_name('product-description')
            warranty_str = warranty.text
        except Exception as e:
            pass
        
        return warranty_str
    
    def scrape_shop_name(self,shop):
        shop_name = None
        try:
            class_name_shop_name = 'shop-info'
            shop_name = shop.find_element_by_class_name(class_name_shop_name).text
        except Exception as e:
            pass

        return shop_name
    
    def click_torob(self):
        try:             
            #click for more
            class_name_click = 'show-more-btn'
            self.click_by_class_name(class_name_click)
        except:
            pass


    def scrape_all_data(self):
        try:
            self.click_torob()
            #find all shops
            class_name_shops = 'shop-card'
            shop_list = self.driver.find_elements_by_class_name(class_name_shops)
            scraped_data_list = []
            for shop in shop_list:
                scraped_data = {
                    'price': self.scrape_price(shop),
                    'warranty': self.scrape_warranty(shop),
                    'seller': self.scrape_shop_name(shop),
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
            send_email_obj = SendEmail(SENDER,RECIEVERS)
            send_email_obj.send_email(str(e))
            return None
 