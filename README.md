# Youtube Influencer Search Engine
A data pipeline for a search engine to detect youtube influencers.

1. [Overview](README.md#overview)
2. [Data](README.md#data)
3. [Pipeline](README.md#pipeline)

<img src="img/demoPic.png" width="800">

## Overview

This project is part of my Insight Data Engineering fellowship in Silicon Valley for Winter 2018. The project takes youtube data from Youtube API, along with web scrapes, and ingests it for use in a influencer search engine application. 

## Data

The data comes form the youtube API and Web scraper. 
For my project, I am going to use small size of data as sample data, but I choose my technologies to be scalable and able to handle the full dataset, while still providing low-latency responses to queries.

## Pipeline 

### Ingestion:
Kafka
### Data Format:
Right now it is Jason beacuse Youtbue API generates data in Jason format. But Jason is slow to read. So this will probably change.
### File System:
AWS S3
### Stream Processing Or Batch Processing [?]
### Data Store [?]
.
.

	
