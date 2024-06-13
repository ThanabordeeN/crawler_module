import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import asyncio
import aiohttp

async def get_content(url_list):
    """Fetches and returns the content of web pages asynchronously."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        list_of_content = []
        for url in url_list:
            tasks.append(asyncio.create_task(fetch_content(session, url)))
        list_of_content = await asyncio.gather(*tasks)
    return list_of_content

async def fetch_content(session, url):
    headers = {
        "X-With-Generated-Alt": "true",
    }
    async with session.get(f"https://r.jina.ai/{url}", headers=headers) as response:
        return await response.text()
def get_page_paths(base_url):
    """Crawls a website and returns a list of unique page paths."""
    visited_urls = set()  
    url_path = set()
    def crawl(url):
        if url in visited_urls:
            return 
        visited_urls.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
            print(url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return 

        soup = BeautifulSoup(response.content, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)  # Handle relative links

            if base_url in absolute_url:
                url_path.add(absolute_url)

    crawl(base_url)

    return url_path

async def main():
    base_url = "https://jina.ai/"
    paths = get_page_paths(base_url)
    content = await get_content(paths)
    print("\nFound page paths:")
    for path in paths:
        print(path)
    return {"URL_PATH":list(paths) , "Content":content}

if __name__ == "__main__":
    data = asyncio.run(main())
    