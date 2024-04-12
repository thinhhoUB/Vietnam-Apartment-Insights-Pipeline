# Vietnam-Apartment-Insights-Pipeline

## Table of Contents
- [Problem and Objective](#problem-and-objective)
- [Architecture](#architecture)
- [Overview](#overview)
- [ETL Flow](#etl-flow)
- [Tableau Dashboard](#tableau-dashboard)
- [How to Run](#how-to-run)
  - [Set up the Crawler](#set-up-the-crawler)
  - [Create Azure Resources](#create-azure-resources)
  - [Set up ADLS Credentials](#set-up-adls-credentials)
  - [Test and Debug our Data Pipeline](#test-and-debug-our-data-pipeline)
  - [Deploy the Crawler in Azure Functions](#deploy-the-crawler-in-azure-functions)
  - [Set up Databricks](#set-up-databricks)
## Problem and Objective

This section explains the problem statement and the objective of the project.

## Architecture

The pipeline scrapes data from the Batdongsan website by PropertyGuru and consists of various modules and technologies:

- **Scraping Data:** Python script is used to scrape data from the Batdongsan website.

- **AWS S3:** Stores the scraped data.

- **AWS Lambda:** Triggered by S3 events to transform the scraped data.

- **Docker:** Containerizes the source code folder and deploys the image to AWS Lambda for auto-scaling data transformation.

- **Cleaned Data:** Stored in another S3 bucket after transformation.

- **AWS SQS:** Triggered by S3 events to load cleaned data into Snowflake using Snowpipe.

- **Snowflake:** A cloud-based data warehousing platform used to store and analyze data.

- **Data Visualization:** Comprehensive data visualization created from Snowflake data using Tableau.

## Overview

This section provides an overview of how the project works and its main components.

## ETL Flow

This section outlines the ETL (Extract, Transform, Load) process in the project.

## Tableau Dashboard

This section discusses data modeling and the creation of the PowerBI dashboard.

## How to Run

This section provides instructions on how to run the project on your local machine.

### Set up the Crawler

Instructions for setting up the web crawler.

### Create Azure Resources

Instructions for creating Azure resources.

### Set up ADLS Credentials

Instructions for setting up Azure Data Lake Storage credentials.

### Test and Debug our Data Pipeline

Instructions for testing and debugging the data pipeline.

### Deploy the Crawler in Azure Functions

Instructions for deploying the web crawler to Azure Functions.

### Set up Databricks

Instructions for setting up Databricks.
