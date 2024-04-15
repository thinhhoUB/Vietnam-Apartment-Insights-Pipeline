# Vietnam-Apartment-Insights-Pipeline

## Table of Contents
- [Problem and Objective](#problem-and-objective)
- [Architecture](#architecture)
- [ETL Flow](#etl-flow)
- [Tableau Dashboard](#tableau-dashboard)
  
## Problem and Objective

This section explains the problem statement and the objective of the project.

## Architecture

<img width="1437" alt="Screen Shot 2024-04-15 at 3 29 19 PM" src="https://github.com/thinhhoUB/Vietnam-Apartment-Insights-Pipeline/assets/80074386/dd9aceff-ec34-4edb-867f-e5e8aa839394">

The pipeline scrapes data from the Batdongsan website by PropertyGuru and consists of various modules and technologies:

- **Python Scraping Script:** is used to scrape data from the Batdongsan website.

- **AWS S3:** Stores the scraped data.

- **AWS Lambda:** Triggered by S3 events to transform the scraped data.

- **Docker:** Containerizes the source code folder and deploys the image to AWS Lambda for auto-scaling data transformation.

- **Cleaned Data:** Stored in another S3 bucket after transformation.

- **AWS SQS:** Triggered by S3 events to load cleaned data into Snowflake using Snowpipe.

- **Snowflake:** A cloud-based data warehousing platform used to store and analyze data.

- **Data Visualization:** Comprehensive data visualization created from Snowflake data using Tableau.

## ETL Flow

- To initiate the pipeline, execute the Python file **web_scraping.py**.
<img width="1160" alt="Screen Shot 2024-04-15 at 2 21 58 PM" src="https://github.com/thinhhoUB/Vietnam-Apartment-Insights-Pipeline/assets/80074386/30c2766a-34b1-4456-ba2a-647a9595eaba">

- Upon successful scraping of each page, the raw data is serialized as a **CSV file** and subsequently uploaded to an **Amazon S3 bucket** within the AWS environment.
<img width="1281" alt="Screen Shot 2024-04-12 at 5 41 41 PM" src="https://github.com/thinhhoUB/Vietnam-Apartment-Insights-Pipeline/assets/80074386/eaec8794-a2c3-4ef7-a30d-3276068301d0">

- AWS Lambda functions are orchestrated to execute in response to S3 events, facilitating the transformation, deduplication, and loading of the raw data into a **cleaned S3 bucket** within the AWS ecosystem.
<img width="1108" alt="Screen Shot 2024-04-12 at 5 42 10 PM" src="https://github.com/thinhhoUB/Vietnam-Apartment-Insights-Pipeline/assets/80074386/cad0891a-2c1b-4b32-aad6-b781d189facd">

- Triggered by events from the cleaned S3 bucket, AWS SQS orchestrates the loading of cleaned data into **Snowflake utilizing Snowpipe**, ensuring efficient and reliable data ingestion into the Snowflake data warehousing platform.
  <img width="1161" alt="Screen Shot 2024-04-12 at 5 41 29 PM" src="https://github.com/thinhhoUB/Vietnam-Apartment-Insights-Pipeline/assets/80074386/55aa4f7a-758d-4ca4-9566-39b85b37f892">

- Finally, for comprehensive data visualization and analysis, leverage **Tableau** to directly connect to the Snowflake table, enabling the creation of dynamic dashboards and insightful visualizations to drive actionable insights.

## Tableau Dashboard

<img width="1440" alt="Screen Shot 2024-04-15 at 2 16 23 PM" src="https://github.com/thinhhoUB/Vietnam-Apartment-Insights-Pipeline/assets/80074386/a75b90e8-6bb2-40ad-8f15-4737545e0062">


