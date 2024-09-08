from .scrape import *
from .constants import *
from database.constants import *
from database.db_integration import *

    
def get_link(product_id,product_name,provider,provider_id):
    response = requests.get(BASE + f"ScrapeUrl/{product_name}/{provider}")
    if response.json()['Url'] is not None:
        url = response.json()['Url']
        #Insert data to DB
        insert_data_obj = DB_INTEGRATION(SERVER_NAME_BI,DATABASE_DW,LOGIN_NAME_BI,PASSWORD_BI)
        insert_data_obj.insert_url(product_id,provider_id,url)
        insert_data_obj.close_data_base_connection()
        return url
    


