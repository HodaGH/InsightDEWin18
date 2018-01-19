# Youtube Ingestion
I did a consulting project during my insight data engineering fellowship. The details of project and data pipeline won't be shared here. But an abstraction of my focus will be explained.

1. [Overview](README.md#overview)
2. [Data](README.md#data)
3. [Pipeline](README.md#pipeline)

<img src="img/demoPic.png" width="800">

## Overview

The goal of my project is to use and set up Youtube Data API (v3) and kafka to provide a real time and efficient ingestion system for youtube data. The goal is to set up youtube API to push notifications when any new video is posted to any channel. This method is more efficient than polling approach or retrieving all data related to all channels once awhile.

## Data

The data comes form the youtube API. For my project, I am going to use small size of data as sample data, but I choose my technologies to be scalable and able to handle the full dataset, while still providing low-latency responses to queries.

## Technologies
Google PubSub, Youtube Data API (v3), Google App Engine, Kafka, Flask, Python, AWS S3

### Ingestion:

	
