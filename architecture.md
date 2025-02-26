# OSV Data Lake Architecture

## Overview
This architecture ingests OSV vulnerability data, processes it using Apache Spark, and stores it in a Delta Lake for efficient querying.

## Components
- **Airflow DAG:** Fetches data daily from OSV API.
- **Azure Storage:** Stores raw JSON data.
- **Apache Spark:** Processes and transforms the data.
- **Delta Lake:** Stores transformed data with versioning.
- **Terraform:** Deploys infrastructure on Azure.

## Architecture Diagram
