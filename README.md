# Web Content Crawler

This Python script is designed to crawl a website and fetch the content of its pages asynchronously.

## Features

- Crawls a website and retrieves a list of unique page paths.
- Fetches the content of the pages asynchronously using the `aiohttp` library.
- Handles errors during the crawling and content fetching process.
- Returns the page paths and their corresponding content as a dictionary.

## Usage

To use the script, simply call the `crawler_domain` function with the base URL of the website you want to crawl:

```python
data = crawl_domain("https://pypi.org/project/beautifulsoup4/")
print(data)
```
This will output a dictionary containing the list of unique page paths and their corresponding content.

## Functions
### get_content(url_list):

This asynchronous function fetches the content of the web pages specified in the **url_list**
.

It uses the 
**aiohttp**
 library to make the requests concurrently.

The function returns a **list of the fetched content**.

### fetch_content(session, url):
This asynchronous function makes a GET request to the specified 
**url**
 using the provided 
session
.

It includes a custom header 
"X-With-Generated-Alt": "true"
.

The function returns the text content of the response.

### get_page_paths(base_url):

This function crawls the website starting from the 
**base_url**
.

It uses the requests
 library to fetch the web pages and the 
BeautifulSoup
 library to parse the HTML.

The function returns a set of unique page paths found during the crawling process.

### main(url):

This asynchronous function is the entry point for the script.

It calls 
get_page_paths
 to retrieve the list of unique page paths, then uses 
get_content
 to fetch the content of those pages.

The function returns a dictionary containing the page paths and their corresponding content.

### crawl_domain(url):
This function is a wrapper around the 
main
 function, which runs the asynchronous code using 
asyncio.run
.

It takes a URL as input and returns the data dictionary.

## Dependencies
- requests
- urllib
- BeautifulSoup4
- asyncio
- aiohttp

## License
This project is licensed under the MIT License.