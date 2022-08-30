# bitcoin_price_2022
Bitcoin price data - 2022

The data was extracted through web scraping (Selenium - Python) from the site CoinMarketCap and saved in an AWS S3 Bucket.

After the extraction process, I used the Glue resource of AWS to process the data with Spark and save the data in Parquet format in another bucket.
