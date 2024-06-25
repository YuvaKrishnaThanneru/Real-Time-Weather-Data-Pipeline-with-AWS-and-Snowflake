<div align="center">
  <h1 style="color:#8a2be2; margin-right: 20px;">🌤️ Real-Time Weather Data Pipeline with AWS and Snowflake ☁️</h1>
</div>

## Overview

Welcome to the Real-Time Weather Data Pipeline project! This project demonstrates the creation of a real-time data pipeline using AWS services and Snowflake. The pipeline fetches weather data from an API, stores it in DynamoDB, processes it with AWS Lambda, saves it to S3, and finally ingests it into Snowflake using Snowpipe and provides real-time insights. 🌐

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/YuvaKrishnaThanneru/Real-Time-Weather-Data-Pipeline-with-AWS-and-Snowflake/assets/171606388/63ccdd42-a276-458a-b31b-f63beeedb82b" width="250">
  <img src="https://github.com/YuvaKrishnaThanneru/Real-Time-Weather-Data-Pipeline-with-AWS-and-Snowflake/assets/171606388/433e947a-5d32-4101-8c99-19a54b8881e2" width="280">
  <img src="https://github.com/YuvaKrishnaThanneru/Real-Time-Weather-Data-Pipeline-with-AWS-and-Snowflake/assets/171606388/9f5f0133-7492-48ac-a7dd-096526c6bd6f" width="360">
</div>


## Key Concepts

- **Real-Time Data Processing**: 🕒 Leveraging AWS Lambda to fetch weather data and storing it in DynamoDB and then process DynamoDB stream records in real-time.
- **Scalable Storage Solutions**: 🗄️ Using DynamoDB for structured data storage and S3 for scalable file storage.
- **Cloud Data Warehousing**: 📊 Utilizing Snowflake for advanced data analytics and warehousing.
- **Event-Driven Architecture**: 🚀 Integrating AWS services with event triggers for seamless data flow.
- **Access Management**:  Utilized Fine-grained access control to AWS resources, ensuring secure management of user permissions.

## Project Components

### 1. Weather Data Ingestion 🌦️

- **Frequency**: Fetches weather data every hour.
- **Source**: Weather API.
- **Technology**: Python script triggered by AWS EventBridge.

### 2. Data Storage in DynamoDB 📂

- **Table Name**: `WeatherData`
- **Data**: Structured JSON data from the weather API.

### 3. Real-Time Data Processing with AWS Lambda ⚡

- **Trigger**: DynamoDB Streams.
- **Function**: Processes stream records and saves data as CSV in S3.
- **Files Generated**: 10 CSV files, each corresponding to a city.

### 4. Data Transfer to S3 📥

- **Bucket Name**: `weather-data-bucket`
- **Format**: CSV files.
- **Purpose**: Store processed data for Snowflake ingestion.

### 5. Snowflake Integration with Snowpipe ❄️

- **Function**: Ingests CSV files from S3 to Snowflake tables.
- **Notification**: Uses SQS to notify Snowflake for data ingestion.

## How It Works

1. **Weather Data Ingestion**: Every hour, an EventBridge rule triggers a Lambda function that fetches the latest weather data from the Weather API. This data, enriched with a timestamp, is then stored in a DynamoDB table named `WeatherData`.
2. **Data Storage in DynamoDB**: The weather data is stored as structured JSON in the `WeatherData` table, providing a reliable and scalable storage solution.
3. **Real-Time Processing with Lambda**: DynamoDB Streams capture any changes to the `WeatherData` table. A second Lambda function, triggered by these streams, processes the new records, converts them to CSV format, and uploads them to an S3 bucket named `weather-data-bucket`.
4. **Data Transfer to S3**: The processed weather data is stored in the S3 bucket as CSV files, making it easy to handle large volumes of data and ensuring scalability.
5. **Snowflake Integration with Snowpipe**: Snowflake's Snowpipe is configured to automatically ingest new CSV files from the S3 bucket into Snowflake tables. Notifications via SQS ensure that Snowflake is alerted whenever new data is available for ingestion.

## Quantifiable Achievements 📈

- **Hourly Data Fetch**: Automates data fetching every hour, ensuring real-time updates.
- **Efficient Data Processing**: Processes up to 10,000 records per hour with AWS Lambda.
- **Scalability**: Handles up to 1TB of data monthly using DynamoDB and S3.
- **Seamless Integration**: Integrates AWS services and Snowflake for end-to-end data flow.
