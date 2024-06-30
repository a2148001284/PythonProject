"""
v2ex上的Python板块
"""
import time
import looter as lt

domain = 'https://www.v2ex.com'
total = []


def crawl(url):
    time.sleep(1)
    tree = lt.fetch(url)
    items = tree.css('#TopicsNode .cell')
    for item in items:
        data = {}
        data['title'] = item.css('span.item_title a::text').extract_first()
        data['author'] = item.css('span.small.fade strong a::text').extract_first()
        data['source'] = f"{domain}{item.css('span.item_title a::attr(href)').extract_first()}"
        reply = item.css('a.count_livid::text').extract_first()
        data['reply'] = int(reply) if reply else 0
        total.append(data)


if __name__ == '__main__':
    tasklist = [f'{domain}/go/css?p={n}' for n in range(1, 572)]
    [crawl(task) for task in tasklist]
    lt.save(total, name='v2ex.csv', sort_by='reply', order='desc')
