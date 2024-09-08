from database.constants import * 
from database.db_integration import *
from scrappers.digikala_scraper import *
from scrappers.emalls_scraper import *
from scrappers.torob_scraper import *
from scrappers.constants import *
from scrappers.google_search_scraper import *
from scrappers.mobile140_scraper import *
from scrappers.technolife_scraper import *
from scrappers.hamrahtel_scraper import *
from email_excp.constants import *
from email_excp.send_email import *
from eways.eways_db import *



#database connection
database_integr = DB_INTEGRATION(SERVER_NAME_BI, DATABASE_DW, LOGIN_NAME_BI,PASSWORD_BI)

def scrape_site(scrapper,url,provider_name,product_id):
    scrapper.scrape_data(url)
    df = scrapper.scrape_all_data()
    database_integr.insert_data_frame_to_database(product_id, provider_name, df)  

def main():
    try:
        #extract urls
        df_url = database_integr.url_extract()

        #create scrape objects
        mobile140_scraper = ScrapeMobile140(DRIVER_PATH)
        technolife_scraper = ScrapeTechnolife(DRIVER_PATH)
        hamrahtel_scraper = ScrapeHamrahtel(DRIVER_PATH)
        digikala_scraper = ScrapeDigikala(DRIVER_PATH)
    
        for index, row in df_url.iterrows():

            #retrieve rows data
            time.sleep(3)
            product_id = row["ProductID"]
            product_name = row["ProductName"]
            torob_url = row["Torob"]
            emalls_url = row["Emalls"]
            digikala_url = row["Digikala"]
            mobile140_url = row["Mobile140"]
            technolife_url = row["Technolife"]
            hamrahtel_url = row["Hamrahtel"]

            #digikala
            provider_name = 'digikala'
            provider_id = 1
            if (digikala_url):
                try:
                    #scrape data
                    scrape_site(digikala_scraper,digikala_url,provider_name,product_id)
                except Exception as e:
                    send_email_obj = SendEmail(SENDER,RECIEVERS)
                    send_email_obj.send_email(str(e))
            else:
                #get url
                digikala_url = get_link(product_id,product_name,provider_name,provider_id)
                if(digikala_url):
                    #scrape data
                    scrape_site(digikala_scraper,digikala_url,provider_name,product_id)
    

            #mobile140
            provider_name = 'mobile140'
            provider_id = 5
            if (mobile140_url):
                try:
                    #scrape data
                    scrape_site(mobile140_scraper,mobile140_url,provider_name,product_id)
                except Exception as e:
                    send_email_obj = SendEmail(SENDER,RECIEVERS)
                    send_email_obj.send_email(str(e))
            else:
                #get url
                mobile140_url = get_link(product_id,product_name,provider_name,provider_id)
                if(mobile140_url):
                    #scrape data
                    scrape_site(mobile140_scraper,mobile140_url,provider_name,product_id)


            #technolife
            provider_name = 'technolife'
            provider_id = 6
            if (technolife_url):
                try:
                    #scrape data
                    scrape_site(technolife_scraper,technolife_url,provider_name,product_id)
                except Exception as e:
                    send_email_obj = SendEmail(SENDER,RECIEVERS)
                    send_email_obj.send_email(str(e))
            else:
                #get url
                technolife_url = get_link(product_id,product_name,provider_name,provider_id)
                if(technolife_url):
                    #scrape data
                    scrape_site(technolife_scraper,technolife_url,provider_name,product_id)


            #hamrahtel
            provider_name = 'hamrahtel'
            provider_id = 7
            if (hamrahtel_url):
                try:
                    #scrape data
                    scrape_site(hamrahtel_scraper,hamrahtel_url,provider_name,product_id)
                except Exception as e:
                    send_email_obj = SendEmail(SENDER,RECIEVERS)
                    send_email_obj.send_email(str(e))
            else:
                #get url
                hamrahtel_url = get_link(product_id,product_name,provider_name,provider_id)
                if(technolife_url):
                    #scrape data
                    scrape_site(hamrahtel_scraper,hamrahtel_url,provider_name,product_id)




        #close database connection
        database_integr.close_data_base_connection()


        mobile140_scraper.stop_driver()
        technolife_scraper.stop_driver()
        hamrahtel_scraper.stop_driver()
        digikala_scraper.stop_driver()

    except Exception as e:  
        send_email_obj = SendEmail(SENDER,RECIEVERS)
        send_email_obj.send_email(str(e))

if __name__ == "__main__":
    main()