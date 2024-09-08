# IranianMarketScraper

**IranianMarketScraper** is a web scraping tool designed to extract product information from major Iranian e-commerce sites, including Digikala, Mobile140, Technolife, Torob, Emalls, and Hamrahtel. This project collects and stores product data for market research, price comparison, and inventory management using SQL Server.

## Features

- **Multi-Site Support:** Scrapes product data from multiple Iranian e-commerce platforms.
- **Detailed Product Information:** Extracts names, prices, descriptions, ratings, and other relevant details.
- **Customizable Scraping:** Set criteria for data extraction, such as product categories and price ranges.
- **SQL Server Storage:** Stores extracted data in SQL Server for robust data management and querying.

## Technologies Used

- Python
- Selenium
- BeautifulSoup
- Requests
- SQL Server

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/IranianMarketScraper.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure database connection:** Update the configuration files to set up your SQL Server connection details.
4. **Configure scraping targets:** Set up your scraping preferences for each site in the configuration files.
5. **Run the scraper:**
   ```bash
   python run.py
   ```

## Supported Sites

- Digikala
- Mobile140
- Technolife
- Torob
- Emalls
- Hamrahtel

## Contributing

Contributions are welcome! Please submit issues, feature requests, or pull requests. Follow the project's coding guidelines for contributions.

## License

This project is licensed under the [MIT License](LICENSE).
