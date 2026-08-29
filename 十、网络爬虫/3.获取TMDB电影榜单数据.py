import requests
from lxml import html
import csv

# 定义常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TOP_MOVIES_URL = "https://www.themoviedb.org/movie/top-rated"
MOVIE_PATH_SAVE = "movies/movies_info.csv"


def get_info_movie(complete_url) -> dict:
    """
    获取电影详细信息
    :param complete_url:
    :return:
    """
    # 发送获取电影详细页的请求
    if complete_url is None:
        return {}
    movie_resp = requests.get(complete_url)
    document = html.fromstring(movie_resp.text)

    # 获取电影详情信息
    movie_names = document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    movie_years = document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')
    movie_dates = document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[2]/text()')
    movie_types = document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[3]/a/text()')
    movie_times = document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()')
    movie_scores = document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_languages = document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_directors = document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    movie_authors = document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[3]/p[1]/a/text()')
    movie_slogans = document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')
    movie_introduction = document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')

    # 封装电影详情信息并返回
    movie_info = {
        '电影名': movie_names[0],
        '年份': movie_years[0],
        '上映时间': movie_dates[0],
        '类型': ','.join(movie_types) if len(movie_types) > 0 else '',
        '时常': movie_times[0],
        '评分': movie_scores[0],
        '语言': movie_languages[0],
        '导演': movie_directors[0] if len(movie_directors) > 0 else '',
        '编剧': movie_authors[0] if len(movie_authors) > 0 else '',
        '宣传语': movie_slogans[0],
        '介绍': movie_introduction[0]
    }
    return movie_info


def save_csv(movie_info_list):
    """
    将电影信息保存到csv文件中
    :param movie_info_list:
    :return:
    """
    if movie_info_list is None or len(movie_info_list) == 0:
        return
    with open(MOVIE_PATH_SAVE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=movie_info_list[0].keys())
        writer.writeheader()  # 写入表头
        writer.writerows(movie_info_list)  # 写入表行数据


def main():
    """
    爬虫脚本执行主入口
    :return:
    """
    # 发请求获取响应体对象
    print("开始获取电影列表数据...")
    response = requests.get(TOP_MOVIES_URL, timeout=60)
    # 解析网页获取文本对象
    document = html.fromstring(response.text)
    # 获取电影列表数据
    movies_div_list = document.xpath(
        '/html/body/div[2]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div')

    # 遍历电影列表，获取其详细信息
    movie_info_list = []
    for item in movies_div_list:
        href = item.xpath('./div/div/a/@href')
        complete_url = TMDB_BASE_URL + href[0]
        print(f"正在获取电影信息: {complete_url}")
        movie_info = get_info_movie(complete_url)
        movie_info_list.append(movie_info)

    # 将电影信息保存到csv文件中
    print("电影信息获取完成，正在保存数据...")
    save_csv(movie_info_list)


# 模块功能自测
if __name__ == '__main__':
    print("开始执行...")
    main()
    print("执行完成...")
