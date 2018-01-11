# InsightDEWin18
Company Description:
Makrwatch is an enterprise software that brands doing influencer marketing on YouTube use to identify YouTube creators, predict campaign results and optimize their ROI over time.  Makrwatch is a 1 year old product developed by themidgame, a Y Combinator backed company, and today is used by one of the largest sponsors of YouTube creators and other agencies partnering with brands.
Problem Description:
At Makrwatch we are indexing around 1.8 Million YouTube channels and every 2 weeks we are retrieving their latest 50 videos, which allows us to have around 50 Million YouTube videos indexed. To do so, we implement a Lambda Architecture. We extract the raw data from YouTube and process it through EMR using python. The results are batch views that are served through Cloudsearch as a serving layer. The problems we have with this approach are: We are wasting the majority of resources. Since not every channel posts videos every week or month, every time we update, we are retrieving the same data for many of the channels. Some information points from channels and videos is usually static (eg: descriptions, titles) while other information changes on a daily/hourly basis (eg: likes, view count etc..) The process is slow, expensive and therefore we cannot scale. Without having a good solution to this problem, we won’t be able to extend to indexing other resources from YouTube such as comments, since these can be on a greater quantity and change constantly.
Data Description:
The data is the information we can retrieve for each channel and video from YouTube’s official API: https://developers.google.com/youtube/v3/ 
The data comes in JSON format. Currently, each indexing represents around 80-100 GB’s of data. We will provide the data through AWS S3
Prior Work:
Through search.makrwatch.com you may see the end result of all the indexing and processing through a search for YouTube creators and for videos. 
Deliverable:
We would like to have the technology, engineering design and infrastructure required to implement a large real-time indexing data pipeline for YouTube. It is ok if the pipeline is used for a few thousand channels, as long as we can extend it to millions of channels. On the other hand, the deliverable should take on account that some resources have different time of information variability. For example, view counts change hourly while channel titles rarely change and Channel ID’s never change. 
Implementation:
Depending on the solution, we will either do a switch to the new way of indexing or start replacing certain parts.


