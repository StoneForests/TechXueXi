import requests
import json


def _get_links(base_url):
    news_url_json = requests.get(base_url).content.decode(
        "utf8")
    news_url = json.loads(news_url_json)["DataSet"]
    json_urls = []
    for i in news_url:
        json_urls.append("https://www.xuexi.cn/lgdata/" + i.split('!')[1])

    all_news_object = []
    for url in json_urls:
        choose_json_str = requests.get(url).content.decode("utf8")
        all_news_object.extend(json.loads(choose_json_str))
    new_list = sorted(all_news_object, key=lambda x: x.get("publishTime", "0"), reverse=False)
    return [news["url"] for news in new_list]


def get_article_links():
    try:
        # 跟xuexi_js项目一样的地址
        response = requests.get("https://www.xuexi.cn/lgdata/1jscb6pu1n2.json").content.decode("utf8")
        articles = json.loads(response)
        new_list = sorted(articles, key=lambda x: x.get("publishTime", "0"), reverse=False)
        return [news["url"] for news in new_list]
    # 以下地址获取到的文章不知道为啥无法用于积分
    # return _get_links("https://www.xuexi.cn/lgdata/896bddc5f57a423b857a85eb40f98945/72742e3e40c96ade71e42b6e7ed42419.json")
    except:
        print("=" * 60)
        print("get_article_links获取失败")
        print("=" * 60)
        raise


def get_video_links():
    try:
        return _get_links("https://www.xuexi.cn/lgdata/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.json")

        # 下面的方法只获取了20个地址返回，且是随机获取的，返回的地址可能有之前用过的，不能保证学习满积分
        # video_json = requests.get("https://www.xuexi.cn/lgdata/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.json").content.decode("utf8")
        # video=json.loads(video_json)["DataSet"]
        # json_urls = []
        # link = []
        # for i in video:
        #     json_urls.append("https://www.xuexi.cn/lgdata/"+i.split('!')[1])
        # while len(link) < 20:
        #     choose_json_url = random.choice(json_urls)
        #     choose_json_str = requests.get(choose_json_url).content.decode("utf8")
        #     pattern = r'https://www.xuexi.cn/[^,"]*'
        #     choose_links = re.findall(pattern, choose_json_str, re.I)
        #     if(len(choose_links) >= 5):
        #         choose_sample = random.sample(choose_links, 5)
        #         for c in choose_sample:
        #             link.append(c)
        # random.shuffle(link)
        # return link
    except:
        print("=" * 60)
        print("get_video_links获取失败")
        print("=" * 60)
        raise
    
