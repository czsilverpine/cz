# Web Crawler Using Python
The crawler starts gathering information from the relevant pages that are given at the beginning of the crawling process. When a new page is encountered, crawler communicates with the classifier to determine its relevancy. If a page is relevant then the distiller checks it to determine whether it is a hub page or not. If a hub page is encountered, all the links made from it are extracted and inserted into a crawl list.

During the crawling process, the crawler collects metadata about the conferences specified in the relevant pages by exploiting anchor texts and <title> tag of the conference announcement pages. The metadata obtained for each conference is stored in a relational database management system.

# My Crawler
I mainly research the web site www.last.fm, where people can share their music to each other freely and also can make friends by the same interest about music. We set one username=’Bookman1974’ in http://www.last.fm/community/users . We want to find all web pages of his friends, so we set the other class MyFriends. We also want to know all information of music which he listened to during the period of time, so we set a class MyTracks.
