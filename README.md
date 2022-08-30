# bitcoin_price_2022
Bitcoin price data - 2022

The data was extract through web scraping (Selenium - Python) from site CoinMarketCap and saved in a AWS S3 Bucket.

After the extraction process I used the Glue resource of AWS to process the data with Spark and save the data in parquet format in another bucket.
