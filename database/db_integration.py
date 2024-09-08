from datetime import datetime
import pandas as pd
from email_excp import *
import pyodbc
import sqlalchemy

class DB_INTEGRATION():
    def __init__(self, server, database, login_name,password):
        connection_string = f'Driver={{SQL Server}};Server={server};Database={database};UID={login_name};PWD={password}'
        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()
    
    def commit(self):
        self.conn.commit()

    def insert_data_frame_to_database(self, ProductID, provider_name, dataframe):
        try:
            if dataframe is not None:
                for index, row in dataframe.iterrows():
                    self.cursor.execute("EXEC WebScrapping.InsertWebScrapData ?, ?, ?,?,?",
                    (ProductID,
                        provider_name,
                        row['seller'],
                        row['price'],
                        row['warranty']
                        )
                    )
                    self.commit()
        except Exception as e:
            print("Error Insert DB: " + str(e))

    def insert_url(self, ProductID, ProviderID, url):
        try:
            self.cursor.execute("EXEC WebScrapping.InsertURL  ?,?,?",
                (ProductID,
                ProviderID,
                 url
                )
            )
            self.commit()
        except Exception as e:
            print("Error Insert DB: " + str(e))
            
    def insert_product_to_scrape(self, ProductID, ProductName, IsActive):
        try:
            self.cursor.execute("EXEC WebScrapping.InsertProductToScrape ?, ?,?",
                (ProductID,
                ProductName,
                    IsActive
                )
            )
            self.commit()
        except Exception as e:
            print("Error Insert DB: " + str(e))

    def update_product_to_scrape(self, ProductID, IsActive):
        try:
            self.cursor.execute("EXEC WebScrapping.UpdateProductToScrape ?, ?",
                (ProductID,
                IsActive
                )
            )
            self.commit()
        except Exception as e:
            print("Error Insert DB: " + str(e))

    def url_extract(self):
        try:
            query = """SELECT  ProductID ,ProductName , Digikala , Torob , Emalls , Mobile140,Technolife,Hamrahtel
                            FROM 
        	                    WebScrapping.ProductsToScrap
                            WHERE
        	                    IsActive = 1
                            order by ProductID
        """
            df_url = pd.read_sql(query, self.conn)
            return df_url

        except Exception as e:
            msg = f"Subject: {SUBJECT}\r\n\r\n{message}"
            send_email_obj = SendEmail(SENDER,RECIEVERS)
            send_email_obj.send_email(msg)

    def close_data_base_connection(self):
        self.cursor.close()
        self.conn.close()




