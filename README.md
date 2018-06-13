# Web-scraper-crawler-python
A python web crawler for automatic download of font file

A crawler for the website https://fontlibrary.org which download all fonts (currently ~1100 fonts) available using BeautifulSoup and urllib.

It can be easily modified to crawl another website.

Steps :

- Iterate over catalogue page to get all font links
- Iterate over font links list to get download link
- Iterate over download link list with wget command to download to directory
