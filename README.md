# Vietnam-Apartment-Insights-Pipeline

## Table of Contents
- [Problem and Objective](#problem-and-objective)
- [Architecture](#architecture)
- [ETL Flow](#etl-flow)
- [Tableau Dashboard](#tableau-dashboard)
- 
## Problem and Objective

This section explains the problem statement and the objective of the project.

## Architecture

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

- Upon successful scraping of each page, the raw data is serialized as a **CSV file** and subsequently uploaded to an **Amazon S3 bucket** within the AWS environment.

- AWS Lambda functions are orchestrated to execute in response to S3 events, facilitating the transformation, deduplication, and loading of the raw data into a **cleaned S3 bucket** within the AWS ecosystem.

- Triggered by events from the cleaned S3 bucket, AWS SQS orchestrates the loading of cleaned data into **Snowflake utilizing Snowpipe**, ensuring efficient and reliable data ingestion into the Snowflake data warehousing platform.
  
- Finally, for comprehensive data visualization and analysis, leverage **Tableau** to directly connect to the Snowflake table, enabling the creation of dynamic dashboards and insightful visualizations to drive actionable insights.
- 
## Tableau Dashboard

This section discusses data modeling and the creation of the PowerBI dashboard.

