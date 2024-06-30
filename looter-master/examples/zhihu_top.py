"""
知乎最高点赞的答案排行
"""
import requests
import looter as lt

domain = 'https://www.zhihu.com'
encoding = 'utf-8'


def crawl(url):
    items = requests.get(url, headers=lt.DEFAULT_HEADERS).json()['data']
    for item in items:
        target = item['target']
        question = target.get('question')
        if not question:  # 只抓视频： or not target.get('topic_thumbnails_extra_info'):
            continue
        data = {}
        data['title'] = question['title']
        data['source'] = f"{domain}/question/{question['id']}/answer/{target['id']}"
        data['vote'] = target['voteup_count']
        yield data


if __name__ == '__main__':
    tasklist = [f'{domain}/api/v4/topics/19776749/feeds/essence?&offset={10 * n}&limit=10' for n in range(100)]
    total = lt.crawl_all(crawl, tasklist)
    lt.save(total, name='zhihu_top.csv', sort_by='vote', order='desc')
