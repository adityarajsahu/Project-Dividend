import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    r = requests.get(url)
    html_content = r.content

    soup = BeautifulSoup(html_content, 'html.parser')
    date_time = soup.select("li.clearfix > span")
    heading = soup.select("li.clearfix > h2 > a")
    paragraphs = soup.select("li.clearfix > p:nth-of-type(1)")

    list_of_dict = []
    for i in range(len(date_time) - 1):
        date_time_str = str(date_time[i + 1])
        s1 = date_time_str.index('<')
        start = date_time_str.index('>')
        end = date_time_str.index('<', s1 + 1)
        date_time_str = date_time_str[start + 1:end]

        heading_str = str(heading[i + 1])
        s1 = heading_str.index('<')
        start = heading_str.index('>')
        end = heading_str.index('<', s1 + 1)
        heading_str = heading_str[start + 1:end]

        paragraph_str = str(paragraphs[i + 1])
        s1 = paragraph_str.index('<')
        start = paragraph_str.index('>')
        end = paragraph_str.index('<', s1 + 1)
        paragraph_str = paragraph_str[start + 1:end]

        list_of_dict.append({
            'date': date_time_str,
            'header': heading_str,
            'para': paragraph_str
        })
    return list_of_dict

def scrape_market_turnover(url):
    r = requests.get(url)
    html_content = r.content

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.select('table.mctable1 > tbody')[0]
    rows = table.contents

    tags = []
    for i in range(1, len(rows), 2):
        # print(rows[i])
        for item in rows[i].children:
            if item.text != '\n':
                tags.append(item.text)
                # print(type(item.text))
    # print(tags)

    list_of_dict = []
    for i in range(0, len(tags), 4):
        list_of_dict.append({
            'index': tags[i],
            'price': tags[i + 1],
            'change': tags[i + 2],
            'percent': tags[i + 3]
        })
    # print(list_of_dict)

    return list_of_dict