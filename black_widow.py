import os
import re

def getLinks(count, queue):
    """
    Returns a list of hyperlink references found in a webpage.
    Parameters:
        count (int): The number of the downloaded webpage
        queue (list): Current list of unvisited hyperlinks
    Returns: queue with additional links from webpage.
    """
    page = open('./downloads/'+str(count+1)+'.html', 'r', encoding='ISO-8859-1') # Latin-1 encoding prevents decoding errors
    attributes = re.findall(r"""href=(["'])(.*?)\1""", page.read()) # Find all occurrences of href attribute using regex
    for attribute in attributes:
        url = attribute[1]
        queue.append(url)
    return queue

if __name__ == '__main__':
    web_crawl = [] # List of visited URLs
    count = 0 # Incremented for each url visited
    queue = [] # Queue of unvisited links

    if not os.path.exists('downloads'): # Directory of downloaded webpages
        os.mkdir('downloads')
    url = input("Enter URL: ")
    queue.append(url)

    while len(web_crawl) < 100:
        url = queue.pop(0) # Breadth first search of URLs
        command = 'wget  -q -O ./downloads/' + str(count+1) + '.html ' + url
        run = os.system(command) # Make an attempt to download page
        if run == 0:
            if url.rstrip('/') not in web_crawl: web_crawl.append(url.rstrip('/')) # Append to list if no exception occurs
            queue = getLinks(count, queue) # Enqueue more links to be visited
            count += 1
    
    for output in web_crawl:
        print(output)
