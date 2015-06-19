# Web Crawler Using Python
The crawler starts gathering information from the relevant pages that are given at the beginning of the crawling process. When a new page is encountered, crawler communicates with the classifier to determine its relevancy. If a page is relevant then the distiller checks it to determine whether it is a hub page or not. If a hub page is encountered, all the links made from it are extracted and inserted into a crawl list.

During the crawling process, the crawler collects metadata about the conferences specified in the relevant pages by exploiting anchor texts and <title> tag of the conference announcement pages. The metadata obtained for each conference is stored in a relational database management system.
