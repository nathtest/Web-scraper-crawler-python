from bs4 import BeautifulSoup
import urllib.request
import fnmatch
import requests
import os

list_link = []

# gathering all links of all catologue page
for i in range(1, 48):  # max page of the site
    resp = urllib.request.urlopen("https://fontlibrary.org/en/catalogue?order=&page=" + str(i))
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

    print("Scraping page " + str(i) + "/48 ...")
    for link in soup.find_all('a', href=True):
        list_link.append(link['href'])

# filtering to have only font links
filtered = fnmatch.filter(list_link, 'https://fontlibrary.org/en/font/*')

# remove duplicate
filtered = list(set(filtered))

print("Found " + str(len(filtered)) + " font link")

filtered_download = []

# gathering all download links of all font link
for i in range(len(filtered)):
    html = requests.get(filtered[i]).text
    soup = BeautifulSoup(html)

    tags = soup.findAll("a", href=True)

    list_download = []
    for link in tags:
        list_download.append(link['href'])

    # filtering to have only download link
    filtered_download.extend(fnmatch.filter(list_download, '/assets/downloads/*'))
    print("Getting download link " + str(i))

    # remove duplicate
    filtered_download = list(set(filtered_download))

    # download font zip to directory /home/user/Download/
    for url in filtered_download:
        url_link = "https://fontlibrary.org/" + url
        print('Downloading %s' % url_link)
        os.system('wget %s -P /home/user/Download/' % url_link)

    filtered_download = []
